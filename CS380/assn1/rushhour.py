#!/usr/bin/env python3

import sys
import math

class Board:
    width, height = 6, 6
    boardArr = [[0 for i in range(width)] for j in range(height)]
    
    def __init__(self):
        width, height = 6, 6
    
    def createBoard(self, inp): #inp will be the string from the cammand line argument
        rows = inp.split('|')
        for row in rows:
            rowElem = list(row)

        


#print 'Number of Arguments: ', len(sys.argv), '.'
#print 'Argument List:', str(sys.argv)
print str(sys.argv[1])

inputArg = str(sys.argv[1]) # storing the argument into an input string

arr = inputArg.split('|')
print arr
print len(arr)
for row in arr:
    rowElem = list(row)

print rowElem

board = Board()

board.createBoard(inputArg)
