## This program is inspired by the following video from numberphile --> https://www.youtube.com/watch?v=o8c4uYnnNnc

from matplotlib import pyplot as plt

def plotted_function(x):
    return x - non_zero_product(x)

def non_zero_product(x):
    product = 1
    for digit in str(x):
        if digit != '0':
            product *= int(digit)
    return product



X = range(5000)
Y = [plotted_function(x) for x in X]

plt.scatter(X, Y, s=1)
plt.show()

