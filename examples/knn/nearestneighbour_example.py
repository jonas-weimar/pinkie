from pinkie.knn import NNClassifier
from sklearn.datasets import load_iris

# instance model
model = NNClassifier()

# load data set iris
iris = load_iris()

# cut to fit just 140 first
X = iris.data[:140]
Y = iris.target[:140]

# fit training data into our model
model.fit(X,Y)

# test model
print(model.predict(iris.data[140:]))
print(iris.target[140:])
