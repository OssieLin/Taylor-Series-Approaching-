import numpy as np
import matplotlib.pyplot as plot
from math import factorial

x = np.linspace(-10, 10, 100)  # generate a vector starting from -10 to 10 with 100 elements

figure, axis = plot.subplots()


def cos(x):
    y = np.zeros(len(x))  # initialize y inside the function
    for n in range(0, 10):
        # cos(x)
        taylor_term = (-1) ** n * x ** (2 * n) / factorial(2 * n)
        y += taylor_term

        axis.clear()
        axis.plot(x, y)
        axis.set_xlabel('x')
        axis.set_ylabel('cos(x)')
        axis.set_title('Terms: %s' % format(n + 1))

        plot.xlim(min(x), max(x))
        plot.ylim(-2, 2)

        plot.grid()
        plot.draw()
        plot.pause(0.5)

    print(y)



