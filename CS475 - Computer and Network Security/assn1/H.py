#!/usr/bin/env python3

def H(n):
    sum_dig = 0
    i = n
    while i:
        sum_dig = sum_dig + int(i % 10)
        i = int(i / 10)
    return int(n + sum_dig)
