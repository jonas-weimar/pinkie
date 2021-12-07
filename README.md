# The Pinkie Library

## What is Pinkie
Pinkie may be the smallest and most usless machine learning library. Including the
following machine learning models:

### Multilayer Perceptron (MLP)
"A multilayer perceptron (MLP) is a class of feedforward artificial neural network.
An MLP consists of, at least, three layers of nodes:
an input layer, a hidden layer and an output layer." ~ Wikipedia, 27. Oct. 2018.
```python
  from pinkie import mlp

  model = mlp.Network([
    mlp.Layer(80*80, None),
    mlp.Layer(512, mlp.activation.relu),
    mlp.Layer(10, mlp.activation.tanh)
  ], learning_rate=1e-3, path="settings.npy")

  # build / compile your Network
  model.build()

  # train and save
  model.fit(x_train, y_train, circles=1000)
  model.saveState()

  # or load and predict
  # you can predict without loading and saving if you fit first
  model.loadState() # or model.loadForeignState(path)
  guess = model.guess(x_topredict)
```

### One Nearest Neighbour (ONN)
"The most intuitive nearest neighbour type classifier is the 1NN classifier
that assigns a point x to the class of its closest neighbour in the feature space [...]." ~ Wikipedia, 27. Oct. 2018.
```python
  from pinkie.knn import NNClassifier

  model = NNClassifier()
  model.setID(ID) # give your classifier an id

  # train your model
  model.fit(x_train, y_train)

  # predict one nearest neighbour
  guess = model.predict(x_test)
```

### Simple Linear Regression (SLR)
"In statistics, linear regression is a linear approach to modelling
the relationship between a scalar response (or dependent variable)
and one or more explanatory variables (or independent variables).
The case of one explanatory variable is called simple linear regression." ~ Wikipedia, 27. Oct. 2018.
```python
from pinkie.regression import SLRModel

model = SLRModel()

# fit your data
model.fit(x_train, y_train)

# model coefficients
coef = model.coef

# predict new data
guess = model.predict(x_predict)
```

To install Pinkie:
```
  pip install git+https://github.com/jonas-weimar/pinkie.git
```
