from math import pi
from path import Path
import pandas as pd
from collections import OrderedDict
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

def debug():
    fns = load_data()
    for fn in fns:
        print('\n'+'#'*20)
        print(fn)
        g=MTG(fn, has_date=True)
        g.display(max_scale=3)
        #x=raw_input('Yes?')

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
    

class A(object):
    def __init__(self, g):
        self.g = g
        self.is_dynamic()

    def __call__(self):
        return self.dataframe()

    def is_dynamic(self):
        """ Check if the MTG is dynamic or not. """
        g = self.g
        ps=g.properties()
        self.dynamic = False
        for p in ps:
            has_list = set(isinstance(x,list) for x in ps[p].values())
            if True in has_list:
                self.dynamic = True
                break

    def att(self, year, name, v, default=None):
        g = self.g
        p = g.property(name).get(v, default)
        if isinstance(p, list):
            p = dict(p)
            return p[year]
        else:
            return p

    def is_veg(self, year, v):
        cat = self.att(year, 'type', v, '')
        return cat.lower() == 'vg'
    def is_flo(self, year, v):
        cat = self.att(year, 'type', v, '')
        return cat.lower() == 'fl'
    def is_latent(self, year, v):
        cat = self.att(year, 'type', v, '')
        return cat.lower() == 'bl'
    def long(self, year, v):
        length = self.att(year, 'length', v, 0)
        return length >= 5
    def short(self, year, v):
        length = self.att(year, 'length', v, 0)
        return 0 <= length < 5
    def la18(self, v):
        return self.att('2018', 'leaf_area_2018', v, 0)
    def la19(self, v):
        return self.att('2019', 'leaf_area_2019', v, 0)

    def date(self, v):
        g=self.g

class Tree(A):

    def dataframe(self):
        """ Extract Tree level information
        return a dataframe

        Algorithms
        ----------
            - apple_tree: 
                Apple tree number
            - trt: 
                treatment or NCI category
            - NCI: 
                Neighbourhood crowding index value
            - TSA_2018: 
                Trunk section area: pi*diameter_b_2018**2/4 (cm2)
            - TSA_2019: 
                Trunk section area: pi*diameter_b**2/4 (cm2)
            - L_shoot_V/F_2018/2019: 
                Number of vegetative of floral long shoots (>=5cm) in 2018 and 2019
            - S_shoot_V/F_2018/2019: 
                Number of vegetative of floral short shoots (<5cm) in 2018 and 2019
            - nb_V_2018/2019: 
                Number of vegetative buds in 2018 and 2019
            - nb_F_2018/2019: 
                Number of floral buds in 2018 and 2019
            - nb_L_2018/2019: 
                Number of latent buds in 2018 and 2019
            - LA_2018/2019: 
                Leaf area (cm2) in 2018 and 2019
            - Elongation : 
                longueur du tronc (A1+A2+A3+dernier /S) / diametre base  (A1)
            - Tapper : 
                (diametre base (A1) - diametre sommet) / longueur total 

        """        
        g = self.g

        apple_tree = g.index(1) 
        trt = 'ac' 
        NCI = '' 

        pnames = g.property_names()

        # Trunk section area: pi*diameter_b_2018**2/4 (cm2)
        A1 = g.node(2)

        if 'diameter_b2018' in g[2]:
            TSA_2018 = pi * (A1.diameter_b2018)**2 / 4.
        else:
            TSA_2018 = pi * (A1.diameter_2018)**2 / 4.

        #Trunk section area: pi*diameter_b**2/4 (cm2)
        TSA_2019 = pi * (A1.diameter_b)**2 / 4.

        #  Number of vegetative of floral long shoots (>=5cm) in 2018 and 2019
        # Colonne type pour le type et length pour la longueur pour 2018 
        # mes informations sont a l'echelle B dans la plupart des cas 
        # (peut etre des cas a l'echelle S). Pour 2019 a l'echelle S

        # cat = g.property('type')
        # length = g.property('length')
        # leaf_area18 = g.property('leaf_area_2018')
        # leaf_area19 = g.property('leaf_area_2019')

        # 'BL', 'EX', 'FL', 'Fl', 'VG'
        # is_veg = lambda x: cat.get(x, '').lower() =='vg'
        # is_flo = lambda x: cat.get(x, '').lower() =='fl'
        # is_latent = lambda x: cat.get(x, '').lower() =='bl'
        # long = lambda x: length.get(x,0) >= 5
        # short = lambda x: 0<= length.get(x,-1) < 5
        # la18 = lambda x: leaf_area18.get(x,0)
        # la19 = lambda x: leaf_area19.get(x,0)
        
        dates = g.property('Date')
        lines = g.property('_line')
        vs18 = [v for v, d in dates.items() if d =='2018'] 
        vs19 = [v for v, d in dates.items() 
                    if (d =='2019') or 
                       (d =='2018' and isinstance(lines.get(v), list))
               ] 
        L_shoot_V_2018 = sum(1 for v in vs18 
                                if self.is_veg('2018', v) and 
                                   self.long('2018', v)
                            ) 
        L_shoot_F_2018 = sum(1 for v in vs18 
                                if self.is_flo('2018', v) and 
                                   self.long('2018', v)
                            )
        L_shoot_V_2019 = sum(1 for v in vs19
                                if self.is_veg('2019', v) and 
                                   self.long('2019', v)
                            ) 
        L_shoot_F_2019 = sum(1 for v in vs19 
                                if self.is_flo('2019', v) and 
                                   self.long('2019', v)
                            )

        #  Number of vegetative of floral short shoots (<5cm) in 2018 and 2019
        S_shoot_V_2018 = sum(1 for v in vs18 
                                if self.is_veg('2018', v) and 
                                   self.short('2018', v)
                            ) 
        S_shoot_F_2018 = sum(1 for v in vs18 
                                if self.is_flo('2018', v) and 
                                   self.short('2018', v)
                            )
        S_shoot_V_2019 = sum(1 for v in vs19
                                if self.is_veg('2019', v) and 
                                   self.short('2019', v)
                            ) 
        S_shoot_F_2019 = sum(1 for v in vs19 
                                if self.is_flo('2019', v) and 
                                   self.short('2019', v)
                            )
        
        # Number of vegetative buds in 2018 and 2019
        nb_V_2018 = sum(1 for v in vs18 if self.is_veg('2018', v))
        nb_V_2019 = sum(1 for v in vs19 if self.is_veg('2019', v))
        
        # Number of floral buds in 2018 and 2019
        nb_F_2018 = sum(1 for v in vs18 if self.is_flo('2018', v))
        nb_F_2019 = sum(1 for v in vs19 if self.is_flo('2019', v))

        # Number of latent buds in 2018 and 2019
        # Bug: latent bugs have not always a date
        nb_L_2018 = sum(1 for v in vs18 if self.is_latent('2018', v))
        nb_L_2019 = sum(1 for v in vs19 if self.is_latent('2019',v))

        # Leaf area (cm2) in 2018 and 2019
        # 
        LA_2018 = sum(self.la18(v) for v in vs18)
        LA_2019 = sum(self.la19(v) for v in vs19)

        # longueur du tronc (A1+A2+A3+dernier /S) / diametre base  (A1)
        trunk = g.Trunk(2)
        assert(len(trunk) == 4)

        length = g.property('length')
        trunk_len = [length.get(v, 0) for v in trunk]
        last_S = g.components(trunk[-1])[-1]
        trunk_len[-1] = length.get(last_S, 0)
        total_length = sum(trunk_len)

        Elongation = total_length / A1.diameter_b 
        # (diametre base (A1) - diametre sommet) / longueur total 
        
        A3 = g.node(trunk[2])
        Tapper = (A1.diameter_b - A3.diameter_b) / total_length


        df = pd.DataFrame( OrderedDict(
            apple_tree=[apple_tree],
            trt=[trt],
            NCI=[NCI],
            TSA_2018=[TSA_2018],
            TSA_2019=[TSA_2019],
            L_shoot_V_2018=[L_shoot_V_2018],
            L_shoot_V_2019=[L_shoot_V_2019],
            L_shoot_F_2018=[L_shoot_F_2018],
            L_shoot_F_2019=[L_shoot_F_2019],
            S_shoot_V_2018=[S_shoot_V_2018],
            S_shoot_V_2019=[S_shoot_V_2019],
            S_shoot_F_2018=[S_shoot_F_2018],
            S_shoot_F_2019=[S_shoot_F_2019],
            nb_V_2018=[nb_V_2018],
            nb_V_2019=[nb_V_2019],
            nb_F_2018=[nb_F_2018],
            nb_F_2019=[nb_F_2019],
            nb_L_2018=[nb_L_2018],
            nb_L_2019=[nb_L_2019],
            LA_2018=[LA_2018],
            LA_2019=[LA_2019],
            Elongation=[Elongation],
            Tapper=[Tapper],
            ),
            columns='apple_tree trt NCI TSA_2018 TSA_2019 L_shoot_V_2018 L_shoot_V_2019 '
            'L_shoot_F_2018 L_shoot_F_2019 S_shoot_V_2018 S_shoot_V_2019 S_shoot_F_2018 S_shoot_F_2019 '
            'nb_V_2018 nb_V_2019 nb_F_2018 nb_F_2019 nb_L_2018 nb_L_2019 LA_2018 LA_2019 '
            'Elongation Tapper '.split(' '))
        return df

class Branches(A):

    def dataframe(self):
        """
        - BSA_2018/2019: 
            Branch section area: pi*diameter_b**2/4 (cm2) or diameter if diameter_b has no value 
            Information  at scale +B in column diameter_b or diameter if no diamter_b
        - B_dist: 
            branch distance on the trunk (0 base of the tree 1 apex of the tree)
        - B_lgth_2018/2019: 
            branch length (cm) in 2018 (2017+2018) and 2019 (2017+2018+2019)
        - L_shoot_V/F_2018/2019: 
            Number of vegetative of floral long shoots (>=5cm) on the branch in 2018 and 2019
        - S_shoot_V/F_2018/2019: 
            Number of vegetative of floral short shoots (<5cm) on the branch in 2018 and 2019
        - nb_V_2018/2019: 
            Number of vegetative buds on the branch in 2018 and 2019
        - nb_F_2018/2019: 
            Number of floral buds on the branch in 2018 and 2019
        - nb_L_2018/2019: 
            Number of latent buds on the branch in 2018 and 2019
        - LA_2018/2019: 
            Leaf area (cm2) in 2018 and 2019
        - Elongation : 
            longueur de la branche / diametre base de la branche
        - Tapper : 
            (diametre base de la branche (2017 ou 2018) - diametre sommet de la branche(2019)) / longueur total de la branche

        """
        g = self.g
        
        apple_tree = g.index(1)

        # Extract branches
        brs = [v for v in g.vertices(scale=2) if g.edge_type(v)=='+']
        brs.insert(0,2)

        BSA_2018
        BSA_2019
        B_dist
        B_lgth_2018
        B_lgth_2019
        L_shoot_V_2018
        L_shoot_V_2018
        L_shoot_F_2019
        L_shoot_F_2019

        S_shoot_V_2018
        S_shoot_V_2018
        S_shoot_F_2019
        S_shoot_F_2019
        nb_V_2018
        nb_V_2019
        nb_F_2018
        nb_F_2019
        nb_L_2018
        nb_L_2019

        LA_2018
        LA_2019

        Elongation
        Tapper


        columns= """
        BSA_2018
        BSA_2019
        B_dist
        B_lgth_2018
        B_lgth_2019
        L_shoot_V_2018
        L_shoot_V_2018
        L_shoot_F_2019
        L_shoot_F_2019
        S_shoot_V_2018
        S_shoot_V_2018
        S_shoot_F_2019
        S_shoot_F_2019
        nb_V_2018
        nb_V_2019
        nb_F_2018
        nb_F_2019
        nb_L_2018
        nb_L_2019
        LA_2018
        LA_2019
        Elongation
        Tapper
        """.split()
        df = pd.DataFrame( OrderedDict(
            apple_tree=[apple_tree],
            trt=[trt],
            NCI=[NCI],
            TSA_2018=[TSA_2018],
            TSA_2019=[TSA_2019],
            L_shoot_V_2018=[L_shoot_V_2018],
            L_shoot_V_2019=[L_shoot_V_2019],
            L_shoot_F_2018=[L_shoot_F_2018],
            L_shoot_F_2019=[L_shoot_F_2019],
            S_shoot_V_2018=[S_shoot_V_2018],
            S_shoot_V_2019=[S_shoot_V_2019],
            S_shoot_F_2018=[S_shoot_F_2018],
            S_shoot_F_2019=[S_shoot_F_2019],
            nb_V_2018=[nb_V_2018],
            nb_V_2019=[nb_V_2019],
            nb_F_2018=[nb_F_2018],
            nb_F_2019=[nb_F_2019],
            nb_L_2018=[nb_L_2018],
            nb_L_2019=[nb_L_2019],
            LA_2018=[LA_2018],
            LA_2019=[LA_2019],
            Elongation=[Elongation],
            Tapper=[Tapper],
            ),
            columns=columns)
        return df


def forest(fns=None):
    if fns is None:
        fns=load_data()

    dfs = []
    errors=[]
    for fn in fns:
        try:
            g=MTG(fn, has_date=True)
            df = Tree(g)()
            dfs.append(df)
        except:
            print('#'*80)
            print('Error with file {}'.format(fn))
            print('#'*80)
            print()
            errors.append(fn)
            continue

    all_df = pd.concat(dfs, axis=0, ignore_index=True)
    all_df.to_csv('trees.csv', sep=';', index=False)
    

    return all_df, errors
