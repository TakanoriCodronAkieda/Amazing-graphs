## This program is inspired by the following video from numberphile --> https://www.youtube.com/watch?v=j0o-pMIR8uk&

from matplotlib import pyplot as plt
from copy import copy

def stern_sequence(hm):
    sequence = [1, 1]
    last_added = [1, 1]
    for i in range(hm):
        holes = len(last_added) - 1
        for j in range(1, holes + 1):
            last_added.insert(j * 2 - 1, last_added[j * 2 - 2] + last_added[j * 2 - 1])
        sequence.extend(last_added)
    return sequence

Y = stern_sequence(15)
X = range(len(Y))

plt.scatter(X, Y, s=.1)
plt.show()