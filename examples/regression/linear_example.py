from pinkie.regression import SLRModel
import numpy as np


# instance your model
model = SLRModel()

x = np.array([1,2,3,4,5,6,7])
y = np.array([24, 12, 32, 12, 43, 221, 421])

# fit your training data
model.fit(x, y)

# get model function as string
# something like 'f(x) = 1.42x - 0.61'
function = str(model)

# get model coefficients as array
# something like '[1,42, -0.61]'
coef = model.coef

# let model guess upcoming values
guess = model.predict([8, 9, 10])
