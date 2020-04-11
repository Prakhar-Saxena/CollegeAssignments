#!/usr/bin/env python3

from random import randint

def H(n):
    return n + 273

def generate(n):
    rndm = randint(0,100)
    list = []
    list.append(H(rndm))
    for i in range(1,n):
        list.append(H(list[i-1]))
    return list

print(generate(7))
g = generate(7)
f = open('pswd', 'w')
for i in g:
    f.write(str(i)+'\n')
