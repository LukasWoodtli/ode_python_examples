import matplotlib.pyplot as plt
import numpy

# These plots of slope fields are experimental

# y * y' + x = 0
# => y' = -x / y
import numpy as np

x = numpy.linspace(-6, 6, 20)
y = numpy.linspace(-6, 6, 20)
X, Y = numpy.meshgrid(x, y)

U = numpy.ones(X.shape)
V = numpy.ones(X.shape)
dy = numpy.divide(-X, Y, where=~np.isclose(Y, np.zeros_like(Y)))
angles = np.degrees(np.arctan(dy))

plt.figure(1)
plt.quiver(X, Y, U, V, angles=angles, headwidth=1)


# f'(x) = (f(x) / x) + (x / 2)
# y' = (y / x) + (x / 2)
x = numpy.linspace(-1, 4, 20)
y = numpy.linspace(-3, 1, 20)
X, Y = numpy.meshgrid(x, y)

U = numpy.ones(X.shape)
V = numpy.ones(X.shape)
dy = numpy.divide(Y, X, where=~np.isclose(X, np.zeros_like(X))) + (X / 2)
angles = np.degrees(np.arctan(dy))

plt.figure(2)
plt.quiver(X, Y, U, V, angles=angles, headwidth=1)


plt.show()
