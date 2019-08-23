## This program is inspired by the following video from numberphile --> https://www.youtube.com/watch?v=j0o-pMIR8uk&

from matplotlib import pyplot as plt
from copy import copy

def hofstadter(n_terms):
    sequence = [1, 1]
    for i in range(2, n_terms):
        num_1 = sequence[-sequence[-1]]
        num_2 = sequence[-sequence[-2]]
        sequence.append(num_1 + num_2)
    return sequence

X = range(1000000)
Y = hofstadter(1000000)

plt.scatter(X, Y, s=.1)
plt.show()


