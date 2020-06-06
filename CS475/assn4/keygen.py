#!/usr/bin/env python3

import random
from fractions import gcd

"""
https://www.youtube.com/watch?v=oOcTVTpUsPQ
"""


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
    return d
