from openalea.mtg import *
from openalea.mtg.traversal import pre_order2
from gafam import analysis, data
import numpy as np

fn = data.file('p1')

g=MTG(fn, has_date=True)
t = analysis.Tree2(g)

dates = t.dates()

lines = g.property('_line')
#vs18 = [v for v, d in dates.items() if d =='2018']
vs18 = [v for v, d in dates.items() if d !='2019']
vs19 = [v for v, d in dates.items()
                    if (d=='2019') or
                       (isinstance(lines.get(v), list))
               ]

""" Tree scale
- the function sum( ) applied to the leaf area of each GUs (of any order: no matter if A, B, C, D, E), giving a unique result per plant on 2018 and another on 2019;
- the function sum( ) applied to the length of each GUs (of any order: no matter if A, B, C, D, E), giving a unique result per plant on 2018 and another on 2019;
- the function count( ) applied to the list of all GUs (of any order: no matter if A, B, C, D, E), giving a unique result per plant on 2018 and another on 2019;
- the function count( ) applied to the list of all FL, giving a unique result per plant on 2018 and another on 2019;
- the same as for FL, also for VG, BL, EX;
- the function mean( ) applied to the angle of each +B, giving a unique result per plant on 2018 and another on 2019;
- the function mean( ) applied to the property nb_leaves of each GU (of any order: no matter if A, B, C, D, E) (!! only where this variable is populated !!!), giving a unique result per plant on 2018 and another on 2019;
- the same as for nb_leaves, also for nb_fruits, nb_flowers, fruit_drop.

"""

# H1 : Look only at 2018 GU and not others
# This is what is stored in the MTG
LA_2018 = sum(t.la18(v) for v in vs18) 

# LA_2019
LA_2019 = 0
la19 = g.property('leaf_area_2019')
for v in vs19:
    la19[v]= la19[v] if v in la19 else sum(la19.get(c,0) for c in g.components(v))
    LA_2019 += la19[v]

# H2 : Look only at all the GU with la18 filled before 2019

# Compute date
max_scale = g.max_scale()
for vid in g.vertices(scale=max_scale):
    cid = g.complex(vid)
    if (cid not in dates) and vid in dates:
        dates[cid]=str(min(int(dates[v]) for v in g.components(cid) if v in dates))


##############################################################


# Leaf Area
# Tree scale 

print('LA 2018', LA_2018)
print('LA 2019', LA_2019)

labels2018 = [g.label(v) for v in vs18]
labels2019 = [g.label(v) for v in vs19]
print('Labels 18: ', ','.join(labels2018))
print('Labels 19: ', ','.join(labels2019))

# Update and compute length for all UC
length = g.property('length')
len18 = sum(length[v] for v in vs18)

for vid in g.vertices(scale=max_scale-1):
    if (vid not in length):
        length[vid]=sum(length[v] for v in g.components(vid) if v in length)
        print (vid, length[vid])

# Q: Do we need to add the value of 2018?  
len19 = sum(length[v] for v in vs19)

# Trunk
trunk = g.Trunk(2)

# number of branches (+B)
branches =  [v for v in g.vertices(scale=2) if g.class_name(v)=='B' and g.edge_type(v)=='+']
print('# Branches : ', len(branches))

# angle of B : azimuth
azimuth = g.property('azimuth')
angle = [azimuth[v] for v in branches if v in azimuth]
# mean angle 
# TODO: no meaning of mean angle
print('Mean angle: ', np.mean(angle))
print('Median angle: ', np.median(angle))

## Trunk /main axis
trunk18 = [v for v in trunk if v in vs18]
trunk19 = [v for v in trunk if v in vs19]
len18 = sum(length[v] for v in trunk18)
len19 = sum(length[v] for v in trunk19)
print ('length 18 & 19', len18, len19)

br18 = {}
br19 = {}
# Leaf area per branch
setv18 = set(vs18) 
setv19 = set(vs19) 

# Compute LA19 on all components
for vb in branches:
    # compute the 2018 and 2019
    # sum the leaf area
    bvs = g.Descendants(vb)
    leaf_area_18 = sum(t.la18(b) for b in bvs if b in setv18)
    leaf_area_19 = sum(la19[b] for b in bvs if b in setv19)
    br18[vb] = leaf_area_18
    br19[vb] = leaf_area_19
    
print ('branchs 18', br18)
print ('branchs 19', br19)

# Final GU per year and branching order
# A, B, C, D, E
gu18 = dict(A=0, B=0, C=0, D=0, E=0)
gu19 = dict(A=0, B=0, C=0, D=0, E=0)

for v in vs18:
    name = g.class_name(v)
    gu18[name]+= t.la18(v)
for v in vs19:
    name = g.class_name(v)
    gu19[name]+= la19[v]

print('GU18', gu18)
print('GU19', gu19)


# Number of inflorescence
"is_flo"