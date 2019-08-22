## This program is inspired by the following video from numberphile --> https://www.youtube.com/watch?v=pAMgUB51XZA

from matplotlib import pyplot as plt
from math import gcd

def plotted_function(x, previous_y):
    if gcd(x, previous_y) == 1:
        return previous_y + x + 1
    common_factor = gcd(x, previous_y)
    return int(previous_y / common_factor)

X = range(1200)
Y = [1, 1]
for i in range(2, 1200):
    Y.append(plotted_function(i, Y[i - 1]))

plt.scatter(X, Y, s=1)
plt.show()


