import time
import numpy as np
import matplotlib.pyplot as plot
from math import factorial

print("Do you know Taylor Series? (Enter yes or no)")
inp = input("")

if inp == "no":
    print("Taylor series is a general way to represent a complicated function with infinite power series.")
    time.sleep(0.8)
    print("It's the way how our graphing calculator can generate graphs!")
else:
    print("Nice!")
    time.sleep(0.8)

print("Taylor series can be expressed with: ")

taylor_series = r"$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n$"

fig, ax = plot.subplots(figsize=(6, 3))
ax.text(0.5, 0.5, taylor_series, fontsize=16, ha='center', va='center', wrap=True)
ax.axis('off')
ax.set_title("General form of Taylor series: ")
plot.show()
time.sleep(0.8)

print("This program visualizes how more terms of derivatives will approach the original function!")
print("Here is an showcase of approaching cos(x) with different terms of derivatives: ")
time.sleep(1)

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

cos(x)

time.sleep(1)

print()

