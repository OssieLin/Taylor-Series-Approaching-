import time
import numpy as np
import matplotlib.pyplot as plot
from math import factorial

print("Do you know Taylor Series? (Enter y for yes, n for no)")
inp = input("")

if inp == "n":
    print("Taylor series is a general way to represent a complicated function with infinite power series.")
    time.sleep(0.8)
    print("It's the way how our graphing calculator can generate graphs!")
    time.sleep(0.8)
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
time.sleep(1)

x = np.linspace(-15, 15, 100)  # generate a vector starting from -15 to 15 with 100 elements

figure, axis = plot.subplots()

def taylor_series(func, derivatives, x, n_terms):
    y = np.zeros(len(x), dtype = float)  # Initialize y as a float64 array

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
    return np.array((-1) ** n * x ** (2*n) / factorial(2*n), dtype = float)

def sin_derivatives(x, n):
    return np.array((-1) ** n * x ** (2*n+1) / factorial (2*n+1), dtype = float)

def arctan_derivatives(x, n):
    return np.array((-1) ** n * x ** (2*n+1) / (2*n+1), dtype = float)

def e_derivatives(x,n):
    return np.array((x ** n) / factorial(n), dtype=float)


while True:
    print("Please choose a function and enter how many derivatives you want to take to approach a specific function from the following!")

    functions = ["sin(x)- choice 1", "cos(x)- choice 2", "arctan(x, n)- choice 3", "e^x"]
    print(functions)

    print("Your choice: (Please enter 1 to 4)")
    inp = input("")

    print("How many derivatives do you want to take?")
    dev = int(input())
    time.sleep(0.8)

    d = dev

    if inp == "1":
        a = "sin(x)"
        b = sin_derivatives
        taylor_series(a, b,x ,d)
    elif inp == "2":
        a = "cos(x)"
        b = cos_derivatives
        taylor_series(a, b, x, d)
    elif inp == "3":
        a = "arctan(x)"
        b = arctan_derivatives
        taylor_series(a, b, x, d)
    else:
        a = "e^x"
        b = e_derivatives
        taylor_series(a, b, x, d)
    time.sleep(0.8)

    print("Do you want to continue? (Enter y for yes, n for no)")
    choice = input("").lower()
    if choice != "y":
        print("Thank you for using the program!")
        time.sleep(0.8)
        print("Hopefully it helps you when learning the taylor series and understanding its significance!")
        time.sleep(0.8)
        break
plot.show()
plot.clf()

