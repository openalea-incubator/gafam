from analysis import *

def test1():
    fns = [Path(u'data/mtg_gafam/p1.txt'),
    Path(u'data/mtg_gafam/p3.txt'),
    Path(u'data/mtg_gafam/p12.txt'),
    Path(u'data/mtg_gafam/p28.txt'),
    Path(u'data/mtg_gafam/p30.txt'),
    Path(u'data/mtg_gafam/p32.txt'),
    Path(u'data/mtg_gafam/p34.txt'),
    Path(u'data/mtg_gafam/p42.txt'),
    Path(u'data/mtg_gafam/p44.txt'),
    Path(u'data/mtg_gafam/p60.txt'),
    Path(u'data/mtg_gafam/p68.txt'),
    Path(u'data/mtg_gafam/p97.txt'),
    Path(u'data/mtg_gafam/p98.txt'),
    Path(u'data/mtg_gafam/p126.txt'),
    Path(u'data/mtg_gafam/p140.txt')]

    d = dict()
    for fn in fns:
        g=MTG(fn, has_date=True)
        l = [g.label(v) for v in g.vertices_iter(scale=2) if g.class_name(v)=='S']
        if l: d[fn] = l

    print(d)
    return d

def test2():
    fns = load_data()
    errors = []
    for fn in fns:
        labels = set()
        g=MTG(fn, has_date=True)
        diameter = g.property('diameter')
        diameter_b = g.property('diameter_b')
        labels.update(set(g.class_name(g.parent(v)) for v in diameter_b))
        labels.update(set(g.class_name(g.parent(v)) for v in diameter))

        if 'B' in labels:
            errors.append(fn)
    print(errors)
    return labels

def test3():
    # analysis branch scale

    fn = Path(u'data/mtg_gafam/p97.txt')
    g=MTG(fn, has_date=True)

    # dates 
    dates = g.property('Date')
    dates = dict(
        (v, dates.get(v, dates.get(g.complex(v))))
        for v in g
    )

    # height
    def _heights():
        v = next(g.component_roots_at_scale_iter(0, scale=3))
        height = dict()
        for v in traversal.pre_order2(g, v):
            height[v] = height.get(g.parent(v), -1)+1
        return height


    trunk = g.Trunk(2)

    brs = [b for v in trunk for b in g.Sons(v, EdgeType='+')]
    #brs.insert(0,2)

    vtrunk = g.Trunk(3)
    #vbrs = [b for v in vtrunk for b in g.Sons(v, EdgeType='+')]


    anchors = dict((b, b-1) for b in brs if g.parent(b))
    heights = _heights()

    # Branch Heights
    tip_height = float(heights[vtrunk[-1]])
    b_dists = [(heights[anchors[v]]+1)/tip_height for v in brs]


    # diameter
    d18 = g.property('diameter_b2018').copy()
    d18.update(g.property('diameter_2018'))
    d19 = g.property('diameter_b')
    #def diam(v, year):

def test4()
    fn = Path(u'data/mtg_gafam/p97.txt')
    g=MTG(fn, has_date=True)
    A1 = g.node(2)
    trunk = g.Trunk(2)
    A1 = g.node(trunk[0])
    A3 = g.node(trunk[2])
