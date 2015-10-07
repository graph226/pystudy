from numpy import*
from matplotlib import pyplot as plt

x = linspace(-pi,pi,50)

y = sin(x)

plt.plot(x, y, color="k", marker="o")

plt.show()
