import matplotlib.pyplot as plt
import pinkie as pk
import numpy as np

# initialize your model
# pk.mlp.Layer(neurons, activation function)
model = pk.mlp.Network([
	pk.mlp.Layer(1, None),
	pk.mlp.Layer(10, pk.mlp.activation.tanh),
	pk.mlp.Layer(1, pk.mlp.activation.tanh)
], learning_rate=1e-5)

# build your model - generates random weights
model.build()

# training data
x = np.linspace(0, 10, 80)
y = np.sin(x)
# show training data
plt.plot(x,y, 'ro')
# fit training data and train your model
model.fit(np.array( [ [x_] for x_ in x]), np.array( [ [y_] for y_ in y]), circles=10000000)

# let the model take the guess
y_p = model.guess([ [x_] for x_ in x])
# plot guess to show regression
plt.plot(x, [ y[0] for y in y_p], 'bo')

# show graph
plt.show()
