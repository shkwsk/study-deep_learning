# coding: utf-8
import numpy as np

def mean_squared_error(y, t):
    '''2乗和誤差'''
    return 0.5 * np.sum((y-t) ** 2)


def cross_entropy_error(y, t):
    '''交差エントロピー誤差'''
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
