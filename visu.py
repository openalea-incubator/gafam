from openalea.mtg import *
from openalea.mtg.plantframe import plantframe, dresser
from openalea.plantgl.all import Viewer, PglTurtle

MIN_LENGTH = 0.1


def repare_mtg(g):
    """ When there are missing component, try to add ghost ones, that is topologically correct element
    to have a complete MTG.
    """
    missings = [v for v in g.vertices(scale=2) if g.nb_components(v) == 0]
    if not missings:
        return g

    anchors = [v-1 for v in missings]
    if anchors:
        assert list(set(g.scale(a) for a in anchors)) == [3]

    parent_missing = [g.complex(a) for a in anchors]
    succ_missing = [(v+1 if v+1 in g else None) for v in missings]
    child_to_connect =  [g.component_roots_iter(v).next() for v in succ_missing]
    ghosts = []

    et = g.property('edge_type')
    for i in range(len(missings)):
        vid, mid = g.add_child_and_complex(anchors[i], complex=missings[i], edge_type='+', label='S0')
        et[missings[i]] = '+'
        g.replace_parent(child_to_connect[i], vid)
        ghosts.append(vid)

    for i, v in enumerate(missings):
        assert g.edge_type(v) == '+'

        assert g.nb_components(v) == 1
        assert g.children(v)[0] == succ_missing[i]
        assert ghosts[i] == g.parent(child_to_connect[i])

        assert v in g.children(parent_missing[i])
        assert succ_missing[i] not in g.children(parent_missing[i])

    for p in set(parent_missing):
        g._children[p].sort()
    return g


def Mtg(fn):
    g = MTG(fn)
    g = repare_mtg(g)
    return g


def LocalAxis(g, vid):
    """ Return the S at scale 3 that composed the main axis of vid. """
    v = g.component_roots_iter(vid).next()
    return list(algo.axis(g, v, RestrictedTo='SameComplex'))


def compute_length(g):
    lengths = g.property('length')
    length = lengths.copy()

    # scale = 2
    for v in g.vertices_iter(scale=2):
        if v not in length:
            length[v] = sum(length.get(c, MIN_LENGTH) for c in g.components(v))

    # Scale 3
    vs3 = [v for v in g.vertices(scale=3) if v not in length]
    complex_s3 = list(set(g.complex(v) for v in vs3))
    complex_s3.sort()

    # Manage the trunk in a different way that other axes.
    length_graftpoint_ram = g.property('length_graftpoint_ram')
    assert len(length_graftpoint_ram) == 1
    v0 = list(length_graftpoint_ram)[0]
    l0 = length_graftpoint_ram[v0]

    trunk = LocalAxis(g, v0)
    length[trunk[0]] = l0

    len_trunk = length[v0]
    n = len(trunk) - 1
    delta_l = max(len_trunk / float(n), MIN_LENGTH)
    for v in trunk[1:]:
        length[v] = delta_l

    # Manage all the other axes
    complex_s3.remove(v0)

    for c in complex_s3:
        axis = LocalAxis(g, c)
        _len = length[c]
        length_unknown = [v for v in axis if v not in length]
        length_to_share = _len - sum(length.get(v,0.) for v in axis)
        delta_length = length_to_share / float(len(length_unknown))
        for v in length_unknown:
            length[v] = delta_length

    return length



def plot(g, *args, **kwds):
    """ Plot a MTG.

    :Optional Parameters:
        - origins : list of 3D points
        - visitor : a function f(g, v, turtle)
            This function is called for each vertex of the MTG.
        - gc : (bool) generalised cylinder
        - turtle: specify the turtle object

    """
    # diameters
    drf = dresser.DressingData(DiameterUnit=1, MinLength=dict(S=MIN_LENGTH, A=MIN_LENGTH, B=MIN_LENGTH))
    diam_top = g.property('diameter_a')
    diam_bot = g.property('diameter_b')
    diam_mean = g.property('diameter')

    def diam(v):
        if v in diam_top:
            return diam_top[v]
        elif v in diam_mean:
            return diam_mean[v]
        else:
            vs = g.Successor(v)
            if vs in diam_bot:
                return diam_bot[vs]

    pf = PlantFrame(g, Length='length',
                    TopDiameter=diam,
                    BottomDiameter='diameter_b',
                    DressingData=drf)


    # computed properties
    _origin = (0.,0.,0.)
    diameters = pf.compute_diameter()
    pf._diameter = diameters

    max_scale = g.max_scale()
    lengths = compute_length(g)
    points = None
    origins = kwds.get('origins', [_origin])

    def plantframe_visitor(g, v, turtle):
        radius = diameters.get(v)
        if radius:
            radius = radius /2.
        elif g.scale(v) < max_scale:
            try:
                vm = g.component_roots_at_scale_iter(v, scale=max_scale).next()
                radius = diameters.get(vm, 0.)/2.
            except:
                radius = 0.

        if points:
            pt = points.get(v)
            if not pt and g.scale(v) != max_scale:
                try:
                    vm = g.component_roots_at_scale_iter(v, scale=max_scale).next()
                    pt = points.get(vm)
                except: pass

            if pt:
                turtle.setId(v)
                turtle.lineTo(pt, radius)
        else:

            turtle.setId(v)

            if g.edge_type(v) == '+':
                turtle.down(60)
                turtle.f(diameters.get(g.parent(v), 0.4)/2.)
            if lengths:
                turtle.F(lengths[v])
            if radius:
                turtle.setWidth(radius)
            turtle.rollL()


    visitor = kwds.get('visitor', plantframe_visitor)
    gc = kwds.get('gc', True)
    _turtle = kwds.get('turtle', None)
    scale = kwds.get('scale', max_scale)
    if not _turtle:
        _turtle = PglTurtle()

    roots = g.roots(scale=scale)
    for i, rid in enumerate(roots):
        if len(origins) > i:
            origin = origins[i]
        else:
            origin = (0,0,0)
        _turtle.move(origin)
        d = diameters.get(rid)
        if not d and scale != max_scale:
            try:
                vm = g.component_roots_at_scale_iter(rid, scale=max_scale).next()
                d = diameters.get(vm)
            except:
                pass

        if d:
            _turtle.setWidth(d)
        turtle.traverse_with_turtle(g, rid, visitor=visitor, turtle=_turtle, gc=gc)

    scene = _turtle.getScene()

    if kwds.get('display',True):
        Viewer.display(scene)
    return scene


