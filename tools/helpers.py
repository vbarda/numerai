def binarize(ser):
    '''transform series of floats into binary 0 (if <= .5) or 1 (if > .5)'''
    return (ser > .5).astype(int)
