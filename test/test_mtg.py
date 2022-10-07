from gafam.analysis import *
from gafam.data import file

def test_forest():
    df, errors = forest()
    return df, errors

def test_branch():
    df, errors = branches()
    # Errors to fix : p9, p52, p141
    assert(len(errors) > 3)

    return df, errors

def test_p9():
    fn = file('p9')
    g = MTG(fn, has_date=True)
    g.display(max_scale=3)