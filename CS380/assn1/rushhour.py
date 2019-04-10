#!/usr/bin/env python3

import sys
import math

class Board:
    width, height = 6, 6
    boardArr = [[0 for i in range(width)] for j in range(height)]
    
    def __init__(self):
        self.width, self.height = 6, 6
        defaultString = "  o aa|  o   |xxo   |ppp  q|     q|     q"
        rows = defaultString.split('|')
        for i in range(len(rows)):
            row = rows[i]
            rowElements = list(row)
            self.boardArr[i] = rowElements

    
    def createBoard(self, inp): #inp will be the string from the cammand line argument
        rows = inp.split('|')
        for i in range(len(rows)):
            row = rows[i]
            rowElements = list(row)
            self.boardArr[i] = rowElements

    def printBoard(self):
        for row in self.boardArr:
            print row
    
    def isDone(self): # here I'm just ahrd coding the [2,5] position to be the winning one
        if self.boardArr[2][5] == 'x' and self.boardArr[2][4] == 'x':
            return True
        else:
            return False



        


#print 'Number of Arguments: ', len(sys.argv), '.'
#print 'Argument List:', str(sys.argv)
#print str(sys.argv[1])

command = str(sys.argv[1]) # storing the command

board = Board()

if len(sys.argv) > 2:
    boardString = str(sys.argv[2]) # storing the argument into an input string
    board.createBoard(boardString)

if command == "print":
    board.printBoard()
elif command == "done":
    print board.isDone()
