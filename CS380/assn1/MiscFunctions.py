#!/usr/bin/env python3

import sys
import math
import Board

CarNotIn = 'Car not in the Board'

def isCarInBoard(boardArr, carCh): # returns whether the passed car character is in the passed board array
    distinctElements = []
    for row in boardArr:
        for element in row:
            if element not in distinctElements:
                distinctElements.append(element)
    distinctElements.remove(' ')
    if carCh not in distinctElements:
        return False
    else:
        return True

def find(l, elem): # https://stackoverflow.com/questions/6518291/using-index-on-multidimensional-lists
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1

def findAll(l, elem): # returns all the coordinates of a given car in an array
    returnList = []
    cloneL = [] #copying the array
    for row in l:
        a = []
        for e in row:
            a.append(e)
        cloneL.append(a)
    c = find(cloneL, elem)
    if c == -1:
        return None
    while c != -1:
        x = c[0]
        y = c[1]
        returnList.append([x,y])
        cloneL[x][y] = 'not here'
        c = find(cloneL, elem)
    return returnList

def printBoardArr(boardArr):
    print '  - - - - - -  '
    for i in range(len(boardArr)):
        row = boardArr[i]
        print '|',
        for element in row:
            print element,
        if i == 2: # exit position in the board
            print ' '
        else:
            print '|'
    print '  - - - - - -  '
