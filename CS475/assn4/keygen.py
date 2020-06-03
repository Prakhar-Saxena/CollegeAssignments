import random

"""
https://stackoverflow.com/questions/8539441/private-public-encryption-in-python-with-standard-library
"""

def get_prime():
    N = 10**8
    bases = range(2, 20000)
    p = 1
    while any(pow(base, p-1, p) != 1 for base in bases):
        p = random.SystemRandom().randrange(N)
    return p

def multiplicative_inverse(mod, val):
    x, lastx = 0, 1
    a, b = mod, val
    while b:
        a, q, b = b, a // b, a % b
        x, laxtx = lastx - q * x, x
    result = (1 - lastx * modulus) // value
    return result + mod if result < 0 else result
