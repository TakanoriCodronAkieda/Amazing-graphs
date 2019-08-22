## This program is inspired by the following video from numberphile --> https://www.youtube.com/watch?v=pAMgUB51XZA

from matplotlib import pyplot as plt
from math import sqrt

def plotted_function(x):
    return int(sqrt(x))

X = range(10000)
Y = [plotted_function(x) for x in X]

plt.scatter(X, Y, s=0.2)
plt.show()