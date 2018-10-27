# File: network.py
# Last Change: 23.10.2018
# Content: Network layout class
# Authors: Jonas Weimar,

from termcolor import colored
from tqdm import tqdm
import numpy as np
import random as rn



# => Modular neural network
class Network(object):

    # Initializer / Constructor:
    def __init__(self, shape, path="settings.npy", learning_rate=1):
        self.id = hash(id(self))
        self.path = path
        self.weights = []
        self.shape = shape
        self.size = len(shape)
        self.learning_rate = learning_rate


    # Hook methods for build in functions:
    def __str__(self):
        return "Network: " + self.id

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        return self.shape[key]

    def __setitem__(self, key):
        self.__warning("You cannot directly set Network-Shape objects.")


    # Private methods:
    def __feed(self, X):
        # transfer X matrix to layer
        self.shape[0].values = X
        # calculate network output layer by layer
        for i in range(len(self.weights)):
            self.shape[i+1].values = self.shape[i+1].activation(np.dot(self.shape[i].values, self.weights[i]))
        # return outputs
        return self.shape[-1].values

    def __improve(self, X, Y):
        deltas = []
        output = self.__feed(X)
        # caluclate network error based on output
        # calculate delta based on error and add to deltas matrix
        self.network_error = Y - output
        deltas.append( self.network_error * self.shape[-1].activation(output, derivative=True) )
        # backpropagate through network
        for i in range(len(self.weights)-1):
            error = deltas[i].dot(self.weights[-(i+1)].T)
            deltas.append( error * self.shape[-(i+2)].activation(self.shape[-(i+2)].values, derivative=True) )
        # turn deltas to match layer
        deltas = deltas[::-1]
        # tune weights with the dot product of layers and deltas
        # intensity depends on learnin rate
        for i in range(len(self.weights)):
            self.weights[i] += self.learning_rate * self.shape[i].values.T.dot(deltas[i])

    def __error(self, message, start=""):
        print(colored('{}Error:'.format(start), 'red'), message)

    def __warning(self, message, start=""):
        print(colored('{}Warning:'.format(start), 'yellow'), message)

    def __information(self, message, start=""):
        print(colored('{}Information:'.format(start), 'cyan'), message)

    def __success(self, message, start=""):
        print(colored('{}Success:'.format(start), 'white'), message)


    # Public methods:
    def setID(self, id):
        self.id = id

    def getID(self):
        return self.id

    def getShape(self):
        return self.shape

    def loadState(self):
        self.weights = np.load(self.path)
        self.__information("State '{}' is loaded into network.".format(self.path))

    def loadForeignState(self, path):
        self.weights = np.load(path)
        self.__information("Foreign state '{}' is loaded into network.".format(path))

    def saveState(self):
        np.save(self.path, self.weights)
        self.__information("State saved to '{}'.".format(self.path))

    def build(self):
        for i in range(len(self.shape)-1):
            w = np.random.random((self.shape[i].neurons, self.shape[i+1].neurons))
            self.weights.append(w)
        self.__information("Network was build by your configurations.\n")

    def fit(self, X, Y, circles=1000):
        self.__information("Training process started:")
        try:
            for _ in tqdm(range(circles)):
                self.__improve(X, Y)
            self.__success("Network is now trained on your configurations.\n")
        except Exception as e:
            self.__error(e, start="Training")

    def guess(self, X):
        try:
             output = self.__feed(X)
             self.__success("Network calculated output.")
             return output
        except Exception as e:
            self.__error(e)
