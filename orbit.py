# PROBLEM 1
#
# Modify the orbit function below to model
# one revolution of the moon around the earth,
# assuming that the orbit is circular.
#
# Use the math.cos(angle) and math.sin(angle)
# functions in order to accomplish this.

import math
import matplotlib
import matplotlib.pyplot
import numpy

moon_distance = 384e6  # m


def orbit():
    num_steps = 50
    x = numpy.zeros([num_steps + 1, 2])
    step_angle = numpy.pi * 2 / num_steps

    ###Your code here.
    for step in range(num_steps + 1):
        angle = step * step_angle
        x[step, 0] = math.cos(angle) * moon_distance
        x[step, 1] = math.sin(angle) * moon_distance

    return x


x = orbit()


def plot_me():
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()


plot_me()

