# File: layer.py
# Last Change: 23.10.2018
# Content: layer layout class
# Authors: Jonas Weimar,

import numpy as np
import random as rn



class Layer(object):
    """
        Network layer layout

        Each layer stores processed values, his size (neurons) and its activation function
        if activation function is not callable return none as value
    """
    def __init__(self, neurons, activation):
        self.values = []
        self.neurons = neurons
        self.activation = activation if callable(activation) else None
