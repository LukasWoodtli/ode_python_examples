import numpy

# f'(x) = -2 * x * f^3(x)
# => f'(x) = F(x,y) = -2xy^3


def F(x, y):
    return -2 * x * y**3


num_steps = 12
x_k = numpy.zeros(num_steps)
y_k = numpy.zeros(num_steps)

# initial value
x_k[0] = 0
y_k[0] = 1


step_size = 0.2
for i in range(num_steps - 1):
    x_k[i+1] = x_k[i] + step_size

    x = x_k[i]
    y = y_k[i]
    k_1 = F(x, y)
    k_2 = F(x_k[i+1], y_k[i] + step_size * k_1)

    y_k[i + 1] = y_k[i] + step_size / 2.0 * (k_1 + k_2)
    print(f"{x_k[i]}: {y_k[i]}")

