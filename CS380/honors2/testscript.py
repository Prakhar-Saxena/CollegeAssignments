#!/usr/bin/env python3

import Board as Board
import Path as Path

board = Board.Board()
board.createBoard("      |      |xx  bp|    bp|    bp|      ")

board.astar()

#print board.h()

'''
width, height = 6, 6
boardArr = [[0 for i in range(width)] for j in range(height)]

boardString = "  o aa|  o   |xxo   |ppp  q|     q|     q"
def createB(string):
    rows = string.split('|')
    for i in range(len(rows)):
        row = rows[i]
        rowElements = list(row)
        boardArr[i] = rowElements
    return boardArr

def printBoard(arr):
    print '  - - - - - -  '
    for i in range(len(arr)):
        row = arr[i]
        print '|',
        for element in row:
            print element,
        if i == 2: # exit position in the board
            print ' '
        else:
            print '|'
    print '  - - - - - -  '


def find(l, elem): # https://stackoverflow.com/questions/6518291/using-index-on-multidimensional-lists
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1

def findall(l, elem):
    x = find(l, elem)
    print "x = ", x
    print l[x[0]][x[1]]
    returnList = []
    c = find(l, elem)
    while c != -1:
        x = c[0]
        y = c[1]
        returnList.append([x,y])
        l[x][y] = 'boi'
        c = find(l, elem)
    return returnList


arr = createB(boardString)
printBoard(arr)

fa = findall(arr,'q')
print fa
print len(fa)
print fa[0]
print fa[2]
print fa[len(fa)-1]
'''
