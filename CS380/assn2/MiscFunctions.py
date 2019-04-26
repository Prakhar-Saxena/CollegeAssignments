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
    #print boardArr
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

def printClosed5AtATime(closed):
    #closed.pop(0)
    for i in range(len(closed)):
        print '  - - - - - -  ',
    print ''
    for i in range(len(closed[0])): # number of rows = 6
        #print closed
        for board in closed:
            print '|',
            #print board
            row = board[i]
            for elem in row:
                print elem,
            print '|',
        print ''
    for i in range(len(closed)):
        print '  - - - - - -  ',
    print ''

def printCLOSED(closed):
    count = 0
    boardsPerLine = 6
    numOfLines = (int) (len(closed)/boardsPerLine)
    cloneClosed = closed
    while count < (numOfLines * boardsPerLine):
        newClosed = closed[count:(count+boardsPerLine)]
        printClosed5AtATime(newClosed)
        count += boardsPerLine
    newClosed = closed[count:len(closed)]
    printClosed5AtATime(newClosed)

'''
    try:
        while True:
            newClosed = closed[(count):(count + 5)]
            printClosed5AtATime(newClosed)
            for i in range(5):
                print ''
            numOfLines+=1
    except:
        pass
'''
