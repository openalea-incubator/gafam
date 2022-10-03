import os, glob
from path import Path

data_dir = Path(os.path.dirname(__file__)).abspath()

def files():
    fns = data_dir.glob('*.txt')
    fns = sorted(fns, key= lambda x:int(x.name.split('.')[0][1:]))
    return fns

