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

def date(g):
    dates = g.property('Date')
    dates = dict(
        (v, dates.get(v, dates.get(g.complex(v))))
        for v in g
    )
    nd = [v for v in g.vertices(scale=2) if dates.get(v) is None]
    for v in nd:
        for c in g.components(v):
            d = dates.get(c)
            if d:
                dates[v] = d
                break

    return dates

def height(g):
    v = next(g.component_roots_at_scale_iter(0, scale=3))
    height = dict()
    for v in traversal.pre_order2(g, v):
        height[v] = height.get(g.parent(v), -1)+1
    return height

def att(g, year, name, v, default=None):
    p = g.property(name).get(v, default)
    if isinstance(p, list):
        p = dict(p)
        return p[year]
    else:
        return p

def test3():
    # analysis branch scale

    fn = Path(u'data/mtg_gafam/p97.txt')
    g=MTG(fn, has_date=True)

    # dates 
    dates = date(g)

    # height
    heights = height(g)

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

def test_diam(fn=None, threshold=10):
    if fn is None:
        fn = Path(u'data/mtg_gafam/p97.txt')
        fn = Path(u'data/mtg_gafam/p1.txt')
    g=MTG(fn, has_date=True)

    dates = date(g)
    # diameter
    d18 = g.property('diameter_b2018').copy()
    d18.update(g.property('diameter_2018'))
    d19 = g.property('diameter_b').copy()
    d19.update(g.property('diameter'))

    #def diam(v, year):

    trunk = g.Trunk(2)
    
    brs = [b for v in trunk for b in g.Sons(v, EdgeType='+')]

    #dm = lambda v: max(d18.get(x,0) for x in g.Axis(v))
    #bsa18 = [dm(b) for b in brs]

    def length(v, y='2018'):
        l0 =  att(g, y,'length',v,0)
        if l0 == 0:
            l0 = max(att(g, y,'length', b, 0) for b in g.components(v))
        return l0

    #OK
    nod =[b for b in brs if (not d18.get(b, d19.get(b))) 
                            and not(0 < length(b) < threshold)
                            and dates.get(b) !='2019']
    

    return nod, g

def error_diams(threshold=10):
    fns = load_data()
    errors = []
    text = []
    for fn in fns:
        nod, g = test_diam(fn, threshold=threshold)
        if nod:
            errors.append(fn)
            l = [g.label(v) for v in nod]
            l.insert(0, fn.name)
            text.append(' '.join(l))
    text = '\n'.join(text)
    return errors, text

def test_length():
    fn = Path(u'data/mtg_gafam/p97.txt')
    g=MTG(fn, has_date=True)

    dates = date(g)
    trunk = g.Trunk(2)
    brs = [b for v in trunk for b in g.Sons(v, EdgeType='+')]
    br18 = lambda b: [v for v in g.Axis(b) if dates.get(v) in ['2017', '2018']]
    br19 = lambda b: g.Axis(b)

    _len = lambda y, l: sum(att(g, y, 'length', v) for v in l)

    l18= [_len('2018', br18(b)) for b in brs]
    l19= [_len('2019', br19(b)) for b in brs]