import pandas as pd


def display_biggest_corrs(X, feature_names=None, cutoff=.8):
    '''List variable pairs that are most correlated (above cutoff):
    Args:
        X: (df) of features
        feature_names: (list) of features to select
        cutoff: (float) cutoff for biggest correlations
    '''
    if feature_names is None:
        feature_names = X.columns
    corrs = X[feature_names].corr()
    filtered = corrs[(corrs != 1) & (corrs.abs() > cutoff)].stack().drop_duplicates()
    for k, v in filtered.iteritems():
        print '{}, {} -> {}'.format(k[0], k[1], v)
