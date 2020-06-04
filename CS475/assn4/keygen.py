#!/usr/bin/env python3

import random
from fractions import gcd

"""
https://stackoverflow.com/questions/8539441/private-public-encryption-in-python-with-standard-library
"""

# def get_prime(N = 10**8, bases = range(2, 20000)):
#     # N = 10**8
#     # bases = range(2, 20000)
#     p = 1
#     while any(pow(base, p-1, p) != 1 for base in bases):
#         p = random.SystemRandom().randrange(N)
#     return p
#
# def multiplicative_inverse(mod, val): # http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
#     x, lastx = 0, 1
#     a, b = mod, val
#     while b:
#         a, q, b = b, a // b, a % b
#         x, laxtx = lastx - q * x, x
#     result = (1 - lastx * modulus) // value
#     return result + mod if result < 0 else result


"""
https://www.youtube.com/watch?v=oOcTVTpUsPQ
"""


# def keygen(N):
#     p = get_prime(N)
#     q = get_prime(N)
#     phi = (p - 1) * (q - 1)
#     return p * q, multiplicative_inverse(phi, 65537)

def prime_gen(seed=0, bases=range(1, 101)):
    primes = []
    for x in bases:
        for y in range(2, x):
            if x % y == 0:
                break
            else:
                primes.append(x)
            # print(x, sep=' ', end=' ')
    return random.Random(seed).choice(primes)


def is_coprime(x, y):
    if gcd(x, y) == 1:
        return True
    else:
        return False


def phi(p, q):
    return (p - 1) * (q - 1)


def get_public_key(p, q):  # e
    phiN = phi(p, q)
    for i in range(2, phiN):
        if is_coprime(i, N) and is_coprime(i, phiN):
            return i
    return -1  # 314159265


def get_private_key(p, q):  # d
    phiN = phi(p, q)
    N = p * q
    e = get_public_key(p, q)
    # e * d mod phi(p,q) = 1
    d = ((phiN - 1) * e) / e
    return
