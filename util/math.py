import numpy as np
from itertools import product

# Convolution
def conv(fil, ker):
    # Get filter size
    fil_w, fil_h = fil.shape

    # Get kernel size
    ker_w, ker_h = ker.shape

    # NOTE: Height and width of our returned convolution matrix, assuming stride=1:
    height = ker_h - fil_h + 1
    width = ker_w - fil_w + 1

    conv_mat = np.zeros((width, height))
    for w, h in product(range(width), range(height))
        ker_c = ker[w:(w+3), h:(h+3)]
        conv_mat[w][h] = np.sum(np.multiply(fil, ker_c))

    return conv_mat

