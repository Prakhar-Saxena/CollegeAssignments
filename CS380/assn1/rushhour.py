#!/usr/bin/env python3

import sys
import math

# add a CLOSED set for duplicates/ or for states that we've already achieved

class Board:
    width, height = 6, 6
    boardArr = [[0 for i in range(width)] for j in range(height)]
    
    def __init__(self):
        self.width, self.height = 6, 6
        defaultString = "  o aa|  o   |xxo   |ppp  q|     q|     q" #default construction as directed
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
        print '  - - - - - -  '
        for i in range(len(self.boardArr)):
            row = self.boardArr[i]
            print '|',
            for element in row:
                print element,
            if i == 2: # exit position in the board
                print ' '
            else:
                print '|'
        print '  - - - - - -  '
    
    def isDone(self): # here I'm just ahrd coding the [2,5] position to be the winning one
        if self.boardArr[2][5] == 'x' and self.boardArr[2][4] == 'x': # assuming the car is just two characters long
            return True
        else:
            return False

    def next_for_car(self, car): # can take arguments as character
        for row in self.boardArr:
            if car not in row:
                print 'car not in the baord'
                break
                return
        

def find(l, elem): # https://stackoverflow.com/questions/6518291/using-index-on-multidimensional-lists
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1

def findall(l, elem):
    returnList = []
    c = find(l, elem)
    while c != -1:
        x = c[0]
        y = c[1]
        returnList.append([x,y])
        l[x][y] = 'boi'
        c = find(l, elem)
    return returnList


class Car:
    end1 = [0,0]
    end2 = [0,0]
    length = 0

    def __init__(self, board, car): # takes the board and the car character
        

#print 'Number of Arguments: ', len(sys.argv), '.'
#print 'Argument List:', str(sys.argv)
#print str(sys.argv[1])


command = str(sys.argv[1]) # storing the command

board = Board()

if len(sys.argv) > 2: # checking whether there's the optional argument for input
    boardString = str(sys.argv[2]) # storing the argument into an input string
    board.createBoard(boardString)

if command == "print":
    board.printBoard()
elif command == "done":
    print board.isDone()
