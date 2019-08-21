## This program is inspired by the following video from numberphile --> https://www.youtube.com/watch?v=pAMgUB51XZA

from matplotlib import pyplot as plt

def equation(prime):
    return prime - int(bin(prime)[-1:1:-1], 2)

def first_primes(how_many=5):
    primes = [2]
    hm_found = 1
    current_tested = 3
    while hm_found < how_many:
        for prime in primes:
            if current_tested % prime == 0:
                break
        else:
            primes.append(current_tested)
            hm_found += 1
        current_tested += 2
    return primes



X = first_primes(10000)
Y = [equation(prime) for prime in X]

plt.scatter(X, Y, s=1)
plt.show()
