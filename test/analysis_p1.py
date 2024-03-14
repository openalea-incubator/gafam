from openalea.mtg import *

from gafam import analysis
from gafam.data import file

fn = file('p1')
g = MTG(fn, has_date=True)

t = analysis.Tree2(g)
dates = t.dates()
df = t.dataframe()

lines = g.property('_line')

vs18 = [v for v, d in dates.items() if d =='2018']
vs19 = [v for v, d in dates.items()
                    if (d=='2019') or
                       (isinstance(lines.get(v), list))
               ]

LA_2018 = sum(t.la18(v) for v in vs18) 

# LA_2019
LA_2019 = 0
la19 = g.property('leaf_area_2019')
for v in vs19:
    la19[v]= la19[v] if v in la19 else sum(la19.get(c,0) for c in g.components(v))
    LA_2019 += la19[v]


print('LA 2018', LA_2018)
print ('Tree LA18', g[1]['leaf_area_2018'])
print('LA 2019', LA_2019)
print ('Tree LA19', g[1]['leaf_area_2019'])

labels18 = {}
for label in list('ABCDE'):
    labels18[label] = [v for v in vs18 if g.class_name(v) ==label]
print(labels18)


labels19 = {}
for label in list('ABCDE'):
    labels19[label] = [v for v in vs19 if g.class_name(v) ==label]

print(labels19)

_la18 = 0
for label in labels18:
    print('%s18'%label,)
    x = sum(map(t.la18, labels18[label]))
    print(x)
    _la18+=x
print('LeafSurface 18', _la18)
