# File: activation.py
# Last Change: 23.10.2018
# Content: activation functions
# Authors: Jonas Weimar,

import numpy as np
from random import uniform



def randlin(x, derivative=False):
    if derivative:
        return uniform(0.,1.)
    return uniform(0.,1.) * x


def sigmoid(x, derivative=False):
    if derivative:
        return x * (1.0 - x)
    return 1.0/(1+ np.exp(-x))


def tanh(x, derivative=False):
    if derivative:
        return (1-np.power(x,2))
    return np.tanh(x)


def linear(x, derivative=False, alpha=1):
    if derivative:
        return alpha
    return alpha * x


def relu(x, derivative=False, alpha=1):
    if derivative:
        x[x<=0] = 0
        x[x>0] = alpha
        return x
    return np.maximum(0, alpha*x)


def leakyrelu(x, derivative=False, alpha=1):
    if derivative:
        x[x==0] = 0
        x[x<0] = 0.2
        x[x>0] = alpha
        return x
    x[x==0] = 0
    x[x<0] = 0.2 * x
    x[x>0] = alpha * x
    return x
