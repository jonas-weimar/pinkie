from pinkie.regression import SLRModel
import matplotlib.pyplot as plt
import numpy as np


# instance your model
model = SLRModel()

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([24, 12, 32, 12, 43, 221, 421,1242,124,422])

plt.plot(x,y, 'ro')

# fit your training data
model.fit(x, y)

# get model function as string
# something like 'f(x) = 1.42x - 0.61'
function = str(model)

# get model coefficients as array
# something like '[1,42, -0.61]'
coef = model.coef

# let model guess upcoming values
guess = model.predict([1,10])

plt.plot([1,10],guess)

plt.show()
