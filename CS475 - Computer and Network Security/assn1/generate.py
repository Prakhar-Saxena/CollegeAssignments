#!/usr/bin/env python3

from random import randint

from H import H
from misc import fileWriterList, fileWriterNum

def generate(n):
    rndm = randint(10000,100000)
    list = []
    list.append(H(rndm))
    for i in range(1,n):
        list.append(H(list[i-1]))
    return list

def doit(n):
    g = generate(n)
    fileWriterList(g[:-1],'user_passwords')
    fileWriterNum(g[len(g)-1], 'server_password')

doit(10)
