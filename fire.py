## This program is inspired by the following video from numberphile --> https://www.youtube.com/watch?v=o8c4uYnnNnc&

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

X = []
Y = []

index = count()

limit = 100000
step = 50

def fire_sequence_1(hm):
    sequence = [1, 1]
    for i in range(2, hm):
        testing = 1
        while True:
            for step in range(1, len(sequence) // 2 + 1, 1):
                if testing - sequence[-step] == sequence[-step] - sequence[-step * 2]:
                    break
            else:
                sequence.append(testing)
                break
            testing += 1
    return sequence

def fire_sequence():
    while True:
        testing = 1
        while True:
            for step in range(1, len(Y) // 2 + 1, 1):
                if testing - Y[-step] == Y[-step] - Y[-step * 2]:
                    break
            else:
                Y.append(testing)
                yield testing
                break
            testing += 1

def animate(i):
    if i == limit // step:
        ani.event_source.stop()
    for n in range(step):
        X.append(next(index))
        next(fire_sequence())

    plt.cla()
    plt.scatter(X, Y, s=.1)

ani = FuncAnimation(plt.gcf(), animate)
plt.show()