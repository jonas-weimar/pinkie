# File: nearestneighbour.py
# Last Change: 25.10.2018
# Content: Nearest Neighbour layout class
# Authors: Jonas Weimar,

from scipy.spatial import distance
from termcolor import colored
import numpy as np



# => Nearest Neighbour Classifier
class Classifier(object):

    # Initializer / Constructor:
    def __init__(self):
        self.id = hash(id(self))


    # Hook methods for build in functions:
    def __str__(self):
        return "Classifier: " + self.id


    # Private methods
    def __information(self, message, start=""):
        print(colored('{}Information:'.format(start), 'cyan'), message)

    def __success(self, message, start=""):
        print(colored('{}Success:'.format(start), 'white'), message)

    def __closest(self, row):
        best_dist = distance.euclidean(row, self.x_train[0])
        best_index = 0
        for i in range(len(self.x_train)):
            dist = distance.euclidean(row, self.x_train[i])
            if dist < best_dist:
                self.__information("Found new Group to fit: {}".format(self.x_train[i]))
                best_dist = dist
                best_index = i
        return self.y_train[best_index]


    # Public methods
    def setID(self, id):
        self.id = id

    def getID(self):
        return self.id

    def fit(self, X_train, Y_train):
        self.x_train = X_train
        self.y_train = Y_train


    def predict(self, X_predict):
        predictions = []
        for row in X_predict:
            predictions.append(self.__closest(row))
        self.__success("Prediction was made")
        return predictions
