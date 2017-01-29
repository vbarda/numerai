import pandas as pd


def binarize(ser):
    '''transform series of floats into binary 0 (if <= .5) or 1 (if > .5)'''
    return (ser > .5).astype(int)


def _convert_columns_to_categorical(df):
    '''convert columns to pd.Categorical'''
    out = df.copy()
    for col in out:
        out[col] = pd.Categorical(out[col]).codes
    return out


def convert_str_columns_to_categorical(df):
    '''convert all string columns to categorical'''
    return pd.concat([df.select_dtypes(include=['object']).pipe(_convert_columns_to_categorical),
                      df.select_dtypes(exclude=['object'])], axis=1)[df.columns]  # to preserve ord.
