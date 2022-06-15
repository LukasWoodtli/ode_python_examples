import matplotlib.pyplot as plt
import numpy

# f'(x) = f(x) + e^x

# euler
num_steps = 10
x = numpy.zeros(num_steps)
y = numpy.zeros(num_steps)

# Anfangsbedingung
x[0] = 0
y[0] = 1

h = 0.25  # step size

for i in range(1, num_steps):
    x[i] = x[i-1] + h
    y_k = y[i-1]
    y[i] = y_k + h * (y_k + numpy.exp(x[i-1]))


# exact calculation
y_exact = numpy.zeros(num_steps)

for i in range(num_steps):
    x[i] = i * h
    y_exact[i] = (1 + x[i]) * numpy.exp(x[i])


error = numpy.subtract(y_exact, y)

print(f"x: {x}")
print(f"y: {y}")
print(f"y_exact: {y_exact}")
print(f"error: {error}")

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.set_title('Euler method compared to exact calculation')
ax1.plot(x, y, '--', label="euler")
ax1.plot(x, y_exact, label="exact calculation")

ax1.legend()

ax2 = fig.add_subplot(2, 1, 2)
ax2.set_title('Error of the Euler method compared to exact calculation')
ax2.stem(x, error)


# set the spacing between subplots
plt.subplots_adjust(hspace=0.4)

plt.show()
