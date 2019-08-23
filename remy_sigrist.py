## This program is inspired by the following video from numberphile --> https://www.youtube.com/watch?v=j0o-pMIR8uk&

from matplotlib import pyplot as plt

def remy_sigrist(hm):
    sequence = [0]
    for i in range(2, hm + 1):
        current_bin = bin(i)[2:]
        possibles = list(range(len(sequence) + 1))
        for j, number in enumerate(sequence):
            if number not in possibles:
                continue
            other = bin(j + 1)[2:]
            current_bin, other = zero_pad(current_bin, other)
            for bit_1, bit_2 in zip(current_bin, other):
                if bit_1 == bit_2 == '1':
                    possibles.remove(number)
                    break
        sequence.append(possibles[0])
    return sequence

def zero_pad(str_1, str_2):
    if len(str_1) > len(str_2):
        return str_1, '0' * (len(str_1) - len(str_2)) + str_2
    return '0' * (len(str_2) - len(str_1)) + str_1, str_2


Y = remy_sigrist(1500)
X = range(len(Y))

plt.scatter(X, Y, s=.3)
plt.show()