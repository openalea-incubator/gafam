from path import Path
import pandas as pd
from openalea.mtg import *

def load_data():
    "Return a list of MTGs"
    d = Path('data')/'mtg_gafam'
    fns = d.glob('*.txt')
    fns = sorted(fns, key= lambda x:int(x.name.split('.')[0][1:]))
    return fns

def missing_components(g):
    missings = [v for v in g.vertices(scale=2) if g.nb_components(v) == 0]
    return missings

def check_miss(g):
    m = missing_components(g)
    anchors = [v-1 for v in m]
    #Previous element is either of scale 1 or scale 3
    # If scale is 1, then the main axe is not decomposed: impossible
    # if scale is 2, then 2 successives branches are not decomposed: error?
    # Finally, if scale is 3, this is the anchor where we want to add a ghost node
    scale2 = list(a+1 for a in anchors if g.scale(a)==2) 
    return scale2

def check_roots(g, scale=2):
    return [v for v in g.vertices_iter(scale=scale) if v!=scale and g.parent(v) is None]


# Check voir test

def tree(g):
    """
    Extract information at tree scale:
        * apple_tree: 
            Apple tree number
        * trt: 
            treatment or NCI category
        * NCI: 
            Neighbourhood crowding index value
        * TSA_2018: 
            Trunk section area: 
            $\pi*diameter_b_2018^2/4$ (cm2)
        * TSA_2019: 
            Trunk section area: $\pi*diameter_b^2/4$ (cm2)
        * L_shoot_V/F_2018/2019: 
            Number of vegetative of floral long shoots (>=5cm) in 2018 and 2019
        * S_shoot_V/F_2018/2019: 
            Number of vegetative of floral short shoots (<5cm) in 2018 and 2019
        * nb_V_2018/2019: 
            Number of vegetative buds in 2018 and 2019
        * nb_F_2018/2019: 
            Number of floral buds in 2018 and 2019
        * nb_L_2018/2019: 
            Number of latent buds in 2018 and 2019
        * LA_2018/2019: 
            Leaf area (cm2) in 2018 and 2019

    """
    pass


###############################################################################

def error_date(g):
    """ Extract all the same vertices at dat 2018 an 2019
    that are not the same  (define with *)
    """

    date = g.property('realisation')
    
    vids = []
    for v in g.roots_iter(3):
        if g.class_name(v) == g.class_name(v-1):
            if date.get(v) == 2019 and date.get(v-1)==2018:
                vids.append(v)

    roots = g.roots_iter(3)
    roots.next()

    # We search all the patterns that are not A<A/U
    for v in roots:
        p1,p2 = v-1, v-2
        if (g.scale(p1) != g.scale(p2)) or (g.scale(v) != g.scale(p1)+1):
            vids.append(v)

    vids = list(set(vids))
    vids.sort()

    return [g.label(v) for v in vids]

def errors_to_csv(filename='errors.csv'):
    fns = load_data()
    dfs = []
    for fn in fns: 
        try:
            g = MTG(fn, has_date=True)
            name = fn.name
            errors = error_date(g)
            df = pd.DataFrame(dict(name=name, vertex=errors))
            dfs.append(df)
        except:
            print('Error: {}'.format(fn))
            continue
    
    df = pd.concat(dfs, ignore_index=True, axis=0)
    #df.to_csv(filename, sep=';', index=False)
    return df
    
    