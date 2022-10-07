from openalea.mtg import *

fn = 'p52.txt'

g=MTG(fn, has_date=True)
date = g.property('realisation')
vids = []
for v in g.roots_iter(3):
    if g.class_name(v) == g.class_name(v-1):
        if date.get(v) == 2019 and date.get(v-1)==2018:
            vids.append(v)

print ' '.join(g.label(v) for v in vids)

vids = []
for v in g.roots(3):
    p1,p2 = v-1, v-2
    if g.scale(p1) == g.scale(p2) and g.scale(v) == g.scale(p1)+1:
        vids.append(v)

l = list(set(g.roots(3)[1:])-set(vids))
print ' '.join(g.label(v) for v in l)
"""
# Erruer 

' '.join(
    g.label(x) 
    for x in g.roots_iter(3) 
    if '.' in g.index(x))
# S18, S65, S107.1, S134.1, S140.1, S144.1,
S151.1 S155.1
 S159.1 S200.1 S203.1 S205.1 S207.1
 S239.1 S241.1 S247.1 S249.1 S251.1 
 S260.1 S264.1 S268.1 S294.1 S297.1 
 S302.1 S304.1 S306.1 S308.1 S328.1 
 S345.1 S349.1 S355.1 S367.1 S373.1 
 S376.1 S379.1 S381.1 S404.1 S406.1 
 S420.1 S422.1 S427.1 S433.1 S435.1 
 S459.1 S461.1 S463.1 S473.1 S493.1 
 S512.1 S524.1 S542.1 S547.1 S551.1 
 S558.1 S565.1 S570.1 S572 S574.1 S591.1 
 S593.1 S595.1 S631.1 S633.1 S635.1 
 S637.1 S639.1 S641.1 S643.1 S645.1 S647.1 
 S649.1 S659.1 S661.1 S663.1 S669.1 
 S700.1 S702.1 S704.1 S706.1 
 S713.1 S715.1 S717.1 S721.1 S735.1 
 S743.1 S746.1 S772.1 
 
 S780 S782 S786.1 
 S801.1 S803.1 S809.1 S811.1 S821.1 
 S824.1 S826.1 S828.1 S836.1 S842.1 S844.1 
 S890.1 S892.1 S896.1 S902.1 S909.1 S911.1 
 
 S930.1 S932.1 S934.1 S938.1 S940.1 S942.1

"""