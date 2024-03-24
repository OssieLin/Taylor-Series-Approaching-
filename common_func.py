import numpy as np
import matplotlib.pyplot as plot
from math import factorial

x = np.linspace(-15, 15, 100)  # generate a vector starting from -15 to 15 with 100 elements

figure, axis = plot.subplots()

def taylor_series(func, derivatives, x, n_terms):
    y = np.zeros(len(x), dtype=float)  # Initialize y as a float64 array
    for n in range(n_terms):
        # Calculate the nth derivative of the function at each point x
        y += derivatives(x, n)
        axis.clear()
        axis.plot(x, y)
        axis.set_xlabel('x')
        axis.set_ylabel(func)
        axis.set_title('Derivative terms: %s' % format(n + 1))

        # Set static plot limits
        axis.set_xlim(-15, 15)
        axis.set_ylim(-5, 5)

        axis.grid()  # Adding grid using axis object
        plot.draw()
        plot.pause(0.5)

    return y

def cos_derivatives(x, n):
    return np.array((-1) ** n * x ** (2*n) / factorial(2*n), dtype=float)

def sin_derivatives(x, n):
    return np.array((-1) ** n * x ** (2*n+1) / factorial(2*n+1), dtype=float)

def inverse_tan(x, n):
    return np.array((-1) ** n * x ** (2*n+1) / (2*n+1), dtype=float)

def e_derivatives(x,n):
    return np.array(x ** n / factorial(n), dtype=float)

taylor_series("ln(1+x)", e_derivatives, x, 5)
taylor_series("sin(x)", sin_derivatives, x, 5)
taylor_series("cos(x)", cos_derivatives, x, 5)
plot.show()