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

    def clone(self, board): # cloning data from "board" to self)
        self.width = board.width
        self.height = board.height
        self.boardArr = board.boardArr

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

    def replaceCarPos(self, carInit, carFin): # to be only used in moveCar()
        initPos = findAll(self.boardArr, carInit.carCh)
        finPos = carFin.allCoordinates
        for i in initPos:
            self.boardArr[i[0]][i[1]] = ' '
        for j in finPos:
            self.boardArr[j[0]][j[1]] = carFin.carCh

    def moveCar(self, carCh, direction, units):
        if self.isCarInBoard(carCh) == False:
            print 'MoveCar(): ',CarNotIn
            return
        car = Car(self.boardArr, carCh)
        print car.end1
        boardClone = Board()
        boardClone.clone(self)
        # direction can only be 'up', 'down', 'left' and 'right'
        if direction == 'up' and car.orientation == 'vertical':
            for i in range(car.end1[0]-units, car.end1[0]): # checking for path hindrances # from 0 to the start of the car
                if self.boardArr[i][car.end1[1]] != ' ':
                    print 'moveCar(): cannot move car - path hindrance'
                    return
            newCar = Car()
            newCoordinates = []
            for i in range(car.end1[0] - units, car.end2[0] - units):
                newCoordinates.append([i, car.end1[1]])
            newCar.modifyCar(carCh, newCoordinates)
            self.replaceCarPos(car, newCar)
        elif direction == 'down' and car.orientation == 'vertical':
            for i in range(car.end2[0] + 1, car.end2[0] + units):
                if self.boardArr[i][car.end1[1]] != ' ':
                    print 'moveCar(): cannot move car - path hindrance'
                    return
            newCar = Car()
            newCoordinates = []
            for i in range(car.end1[0] + units, car.end2[0] + units):
                newCoordinates.append([i, car.end1[1]])
            newCar.modifyCar(carCh, newCoordinates)
            self.replaceCarPos(car, newCar)
        elif direction == 'left' and car.orientation == 'horizontal':
            for i in range(car.end1[1]-units, car.end1[1]):
                if self.boardArr[car.end1[0]][i] != ' ':
                    print 'moveCar(): cannot move car - path hindrance'
                    return
            newCar = Car()
            newCoordinates = []
            for i in range(car.end1[1] - units, car.end2[1] - units):
                newCoordinates.append([car.end1[0], i])
            newCar.modifyCar(carCh, newCoordinates)
            self.replaceCarPos(car, newCar)
        elif direction == 'right' and car.orientation == 'horizontal':
            for i in range(car.end2[1] + 1, car.end2[1] + units):
                if self.boardArr[car.end2[0]][i] != ' ':
                    print 'moveCar(): cannot move car - path hindrance'
                    return
            newCar = Car()
            newCoordinates = []
            for i in range(car.end1[1] + units, car.end2[1] + units):
                newCoordinates.append([car.end1[0], i])
            newCar.modifyCar(carCh, newCoordinates)
            self.replaceCarPos(car, newCar)


    def next_for_car(self, carCh): # can take arguments as character
        CLOSED = [] # list to store the states that have already been achieved
        if isCarInBoard(self.boardArr, carCh) == False:
            print 'next_for_car(): ', CarNotIn
        car = Car(self.boardArr, carCh)
        car.printDetails()
        if car.orientation == 'horizontal':
            print 'eh'

    def next(self): # call next_for_car() for all the cars
        distinctElements = []
        for row in self.boardArr:
            for element in row:
                if element not in distinctElements:
                    distinctElements.append(element)
        distinctElements.remove(' ')
        for carCh in distinctElements:
            self.next_for_car(carCh)
        
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
    end1 = [0,0] #end1 comes before end2
    end2 = [0,0]
    length = 0
    orientation = "" #vertical or horizontal
    allCoordinates = []

    def __init__(self, boardArr, carCh): # takes the board and the car character
        if isCarInBoard(boardArr, carCh) == False:
            print 'Car Constructer __init__() ', CarNotIn
            return
        self.carChar = carCh
        self.allCoordinates = findall(boardArr, carCh)
        self.end1 = self.allCoordinates[0] # end1 comes before end2
        self.end2 = self.allCoordinates[len(self.allCoordinates)-1]
        self.length = len(self.allCoordinates)
        if self.end1[1] == self.end2[1]: # checking for orientation # if y coordinate is same
            self.orientation = 'vertical'
        elif self.end1[0] == self.end2[0]:
            self.orientation = 'horizontal'

    def modifyCar(self, newCarCh, newAllCoordinates):
        self.carCh = newCarCh
        self.end1 = newAllCoordinates[0]
        self.end2 = newAllCoordinates[len(newAllCoordinates) - 1]
        self.length = len(newAllCoordinates)
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


