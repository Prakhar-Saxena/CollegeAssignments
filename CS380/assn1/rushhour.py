#!/usr/bin/env python3

import sys
import math

# add a CLOSED set for duplicates/ or for states that we've already achieved

CarNotIn = 'Car not in the Board'

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

    def isCarInBoard(self, carCh):
        distinctElem = []
        for row in self.boardArr:
            for element in row:
                if element not in distinctElem:
                    distinctElem.append(element)
        distinctElem.remove(' ')
        if carCh not in distinctElem:
            return False
        else:
            return True

    def moveCar(self, carCh, direction, units):
        if self.isCarInBoard(carCh) == False:
            print 'MoveCar(): ',CarNotIn
            return
        

    def next_for_car(self, carCh): # can take arguments as character
        CLOSED = [] # list to store the states that have already been achieved
        if self.isCarInBoard( carCh) == False:
            print 'next_for_car(): ', CarNotIn
        car = Car(self.boardArr, carCh)
        car.printDetails()
        if car.orientation == 'horizontal':
            print 'eh'

    def next(self): # call next_for_car() for all the cars
        distinctElem = []
        for row in self.boardArr:
            for element in row:
                if element not in distinctElem:
                    distinctElem.append(element)
        distinctElem.remove(' ')
        for carCh in distinctElem:
            self.next_for_car(carCh)
        

def find(l, elem): # https://stackoverflow.com/questions/6518291/using-index-on-multidimensional-lists
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1

def findall(l, elem): # returns all the coordinates of a given car in an array
    returnList = []
    c = find(l, elem)
    if c == -1:
        return None
    while c != -1:
        x = c[0]
        y = c[1]
        returnList.append([x,y])
        l[x][y] = 'boi'
        c = find(l, elem)
    return returnList


class Car:
    carChar = ''
    end1 = [0,0]
    end2 = [0,0]
    length = 0
    orientation = "" #vertical or horizontal

    def __init__(self, boardArr, car): # takes the board and the car character
        self.carChar = car
        coordinates = findall(boardArr, car)
        self.end1 = coordinates[0]
        self.end2 = coordinates[len(coordinates)-1]
        self.length = len(coordinates)
        if self.end1[1] == self.end2[1]: # checking for orientation # if y coordinate is same
            self.orientation = 'vertical'
        elif self.end1[0] == self.end2[0]:
            self.orientation = 'horizontal'

    def printDetails(self):
        print 'Car Character: ', self.carChar
        print 'end1: ', self.end1
        print 'end2: ', self.end2
        print 'length: ', self.length
        print 'orientation: ', self.orientation
        

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
elif command == "next":
    board.next()
