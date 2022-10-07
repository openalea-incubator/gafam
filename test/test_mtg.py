from gafam.analysis import *

def test_forest():
    df, errors = forest()
    return df, errors

def test_branch():
    df, errors = branches()
    # Errors to fix : p9, p52, p141
    assert(len(errors) > 3)

    return df, errors

