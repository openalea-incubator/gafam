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


    
