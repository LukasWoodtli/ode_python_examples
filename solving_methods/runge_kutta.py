import numpy

# f'(x) = f(x) + e^x
from matplotlib import pyplot as plt


def F(x, y):
    return y + numpy.exp(x)


num_steps = 12
x_k = numpy.zeros(num_steps)
y_k = numpy.zeros(num_steps)

# initial value
x_k[0] = 0
y_k[0] = 1


# step_size
h = 0.2
for i in range(num_steps - 1):
    x_k[i+1] = x_k[i] + h

    x = x_k[i]
    y = y_k[i]
    k_1 = F(x, y)
    k_2 = F(x + h/2., y + h/2. * k_1)
    k_3 = F(x + h/2., y + h/2. * k_2)
    k_4 = F(x + h, y + h * k_3)

    y_k[i + 1] = y_k[i] + h/6. * (k_1 + 2 * k_2 + 2 * k_3 + k_4)


# exact calculation
y_exact = numpy.zeros(num_steps)

for i in range(num_steps):
    y_exact[i] = (1 + x_k[i]) * numpy.exp(x_k[i])


error = numpy.subtract(y_exact, y_k)

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.set_title('Runge-Kutta method compared to exact calculation')
ax1.plot(x_k, y_k, '--', label="runge-kutta")
ax1.plot(x_k, y_exact, 'o', label="exact calculation")

ax1.legend()

ax2 = fig.add_subplot(2, 1, 2)
ax2.set_title('Error of the Runge-Kutta method compared to exact calculation')
ax2.stem(x_k, error)


# set the spacing between subplots
plt.subplots_adjust(hspace=0.4)

plt.show()

