# The Pinkie Framework

## What is Pinkie
Pinkie is a small machine learning library. Written to be understood.
Yet it has two classifiers - One Nearest Neighbour & Multilayer Perceptron.
Both very useful. You can extend them, you can use them, you can help me make them better and more efficient.

### Multilayer Perceptron (MLP) - Classifier
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

  # give your classifier an id
  model.setID(ID)

  # train and save
  model.fit(x_train, y_train, circles=1000)
  model.saveState()

  # or load and predict
  # you can predict without loading and saving if you fit first
  model.loadState() # or model.loadForeignState(path)
  guess = model.guess(x_topredict)
```

### One Nearest Neighbour (1NN) Classifier
"The most intuitive nearest neighbour type classifier is the 1NN classifier
that assigns a point x to the class of its closest neighbour in the feature space [...]." ~ Wikipedia, 27. Oct. 2018.
```python
  from pinkie.knn import Classifier

  model = Classifier()
  model.setID(ID) # give your classifier an id

  # train your model
  model.fit(x_train, y_train)

  # predict one nearest neighbour
  guess = model.predict(x_test)
```



## Why use Pinkie
Why not? - It's new. It's not the best. It's not from Google. - But why wouldn't you.
You can use your own activation functions or use the build in ones,
you can implement new classifiers, you can tune the build in ones.
And we can build a well working machine learning library on our own.
Let's make this project a great library for everyone.

To install Pinkie:
```
  pip install git+https://github.com/jonas-weimar/pinkie.git
```
