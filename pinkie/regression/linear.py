# File: linear.py
# Last Change: 29.10.2018
# Content: Linear Regression layout class
# Authors: Jonas Weimar,

import numpy as np



# => Simple Linear Regression Model
class SLRModel(object):

    # Initializer / Constructor:
    def __init__(self):
        self.coef = []


    # Hook methods for build in functions:
    def __str__(self):
        return "f(x) = {}x + {}".format(self.coef[0], self.coef[1])

    def __getitem__(self, key):
        return self.coef[key]


    # Public Methods
    def fit(self, x, y):
        self.coef.clear()

        n = np.size(x)
        x_mean, y_mean = np.mean(x), np.mean(y)

        ss_xy, ss_xx = np.sum(y*x - n*y_mean*x_mean), np.sum(x*x - n*x_mean*x_mean)

        m = ss_xy / ss_xx
        b = y_mean - m*x_mean

        self.coef = [m, b]

    def predict(self, x):
        result = []
        for row in x:
            result.append( (self.coef[0] * row + self.coef[1]) )
        return result
