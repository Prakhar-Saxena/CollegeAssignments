#!/usr/bin/env python3

import sys
import math
import MiscFunctions as misc
import Car as Car
from random import randint
import Path as Path
import copy as copy

# add a CLOSED set for duplicates/ or for states that we've already achieved

CarNotIn = 'Car not in the Board'

class Board:
    width, height = 6, 6
    #boardArr = [[0 for i in range(width)] for j in range(height)]
    #cars = []

    def __init__(self):
        self.width, self.height = 6, 6
        defaultString = "  o aa|  o   |xxo   |ppp  q|     q|     q" #default construction as directed
        self.boardArr = [[0 for i in range(self.width)] for j in range(self.height)]
        rows = defaultString.split('|')
        for i in range(len(rows)):
            row = rows[i]
            rowElements = list(row)
            self.boardArr[i] = rowElements
        self.cars = []
        cars = self.getCarsFromBoard()
        for carCh in cars:
            car = Car.Car(self.boardArr, carCh)
            self.cars.append(car)

    def __eq__(self, other):
        return self.boardArr == other.boardArr

    def createBoard(self, inp): #inp will be the string from the cammand line argument
        newBoardArr = []
        rows = inp.split('|')
        for i in range(len(rows)):
            row = rows[i]
            rowElements = list(row)
            newBoardArr.append(rowElements)
        for i in range(len(newBoardArr)):
            for j in range(len(newBoardArr[i])):
                self.boardArr[i][j] = newBoardArr[i][j]

    def modifyBoard(self, boardArr):
        self.boardArr = [[0 for i in range(self.width)] for j in range(self.height)]
        for i in range(len(boardArr)):
            for j in range(len(boardArr[i])):
                self.boardArr[i][j] = boardArr[i][j]
        
        '''for row in boardArr:
            a = []
            for element in row:
                a.append(element)
            self.boardArr.append(a)
            '''

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

    def getCarsFromBoard(self):
        distinctElements = []
        for row in self.boardArr:
            for element in row:
                if element not in distinctElements:
                    distinctElements.append(element)
        distinctElements.remove(' ')
        return distinctElements

    def getCar(self, carCh):
        for car in self.cars:
            if car.carChar == carCh:
                return car
        return 'No car like that.'

    def getCarOrientation(self, carCh):
        car = self.getCar(carCh)
        if car != 'No car like that.':
            return car.orientation
        return

    def clone(self, board): # cloning data from "board" to self)
        self.boardArr = [[0 for i in range(self.width)] for j in range(self.height)]
        for i in range(len(board.boardArr)):
            for j in range(len(board.boardArr[i])):
                self.boardArr[i][j] = board.boardArr[i][j]
        self.cars = board.cars

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
        #print 'Car INIT'
        #carInit.printDetails()
        #print 'Car FIN'
        #carFin.printDetails()
        initPos = misc.findAll(self.boardArr, carInit.carChar)
        finPos = carFin.allCoordinates
        for i in initPos:
            self.boardArr[i[0]][i[1]] = ' '
        for j in finPos:
            self.boardArr[j[0]][j[1]] = carFin.carChar

    def moveCar(self, carCh, direction, units):
        #' and i >=0 print carCh, direction, units
        if self.isCarInBoard(carCh) == False:
            print 'MoveCar(): ',CarNotIn
            return
        car = Car.Car(self.boardArr, carCh)
        boardClone = Board()
        boardClone.clone(self)
        # direction can only be 'up', 'down', 'left' and 'right'
        try:
            if direction == 'up' and car.orientation == 'vertical':
                for i in range(car.end1[0]-units, car.end1[0]): # checking for path hindrances # from 0 to the start of the car
                    if self.boardArr[i][car.end1[1]] != ' ' or i < 0 or i > 5:
                        #print 'moveCar(): cannot move car - path hindrance'
                        return
                newCar = Car.Car(self.boardArr, carCh)
                newCoordinates = []
                for i in range(car.end1[0] - units, car.end2[0] - units + 1):
                    newCoordinates.append([i, car.end1[1]])
                newCar.modifyCar(carCh, newCoordinates)
                self.replaceCarPos(car, newCar)
            elif direction == 'down' and car.orientation == 'vertical':
                for i in range(car.end2[0] + 1, car.end2[0] + units + 1):
                    if self.boardArr[i][car.end1[1]] != ' ' or i < 0 or i > 5:
                        #print 'moveCar(): cannot move car - path hindrance'
                        return
                newCar = Car.Car(self.boardArr, carCh)
                newCoordinates = []
                for i in range(car.end1[0] + units, car.end2[0] + units + 1):
                    newCoordinates.append([i, car.end1[1]])
                newCar.modifyCar(carCh, newCoordinates)
                self.replaceCarPos(car, newCar)
            elif direction == 'left' and car.orientation == 'horizontal':
                for i in range(car.end1[1]-units, car.end1[1]):
                    if self.boardArr[car.end1[0]][i] != ' ' or i < 0 or i > 5:
                        #print 'moveCar(): cannot move car - path hindrance'
                        return
                newCar = Car.Car(self.boardArr, carCh)
                newCoordinates = []
                for i in range(car.end1[1] - units, car.end2[1] - units + 1):
                    newCoordinates.append([car.end1[0], i])
                newCar.modifyCar(carCh, newCoordinates)
                self.replaceCarPos(car, newCar)
            elif direction == 'right' and car.orientation == 'horizontal':
                for i in range(car.end2[1] + 1, car.end2[1] + units + 1):
                    if self.boardArr[car.end2[0]][i] != ' ' or i < 0 or i > 5:
                        #print 'moveCar(): cannot move car - path hindrance'
                        return
                newCar = Car.Car(self.boardArr, carCh)
                newCoordinates = []
                for i in range(car.end1[1] + units, car.end2[1] + units + 1):
                    newCoordinates.append([car.end1[0], i])
                newCar.modifyCar(carCh, newCoordinates)
                self.replaceCarPos(car, newCar)
            #else:
                #print 'cme',
                #print 'car is horizontal/vertical and you\'re tring to move it vertically/horizontally.'
            #self.printBoard()
            return self.boardArr
        except IndexError:
            pass
            #print 'eh.. IndexError'

    def next_for_car(self, carCh): # can take arguments as character
        CLOSED = [] # list to store the states that have already been achieved
        if misc.isCarInBoard(self.boardArr, carCh) == False:
            print 'next_for_car(): ', CarNotIn
        car = Car.Car(self.boardArr, carCh)
        cloneBoard = Board()
        #car.printDetails()
        if car.orientation == 'horizontal':
            directions = ['left', 'right']
            for direction in directions:
                for i in range(1,5):
                    cloneBoard.clone(self)
                    newBoardArr = cloneBoard.moveCar(carCh, direction, i)
                    #cloneBoard.printBoard()
                    if newBoardArr not in CLOSED and newBoardArr is not None:
                        #print newBoardArr
                        #CLOSED.append(cloneBoard)
                        CLOSED.append(newBoardArr)
        elif car.orientation == 'vertical':
            directions = ['down', 'up']
            for direction in directions:
                for i in range(1,5):
                    cloneBoard.clone(self)
                    newBoardArr = cloneBoard.moveCar(carCh, direction, i)
                    #cloneBoard.printBoard()
                    if newBoardArr not in CLOSED and newBoardArr is not None:
                        #print newBoardArr
                        #CLOSED.append(cloneBoard)
                        CLOSED.append(newBoardArr)
        #CLOSED.remove(None)
        #print CLOSED
        #misc.printCLOSED(CLOSED)
        #for board in CLOSED:
            #print board
            #board.printBoard()
            #misc.printBoardArr(board)
            #for row in board:
                #print row
            #print
        return CLOSED

    def next(self): # call next_for_car() for all the cars
        CLOSED = []
        #CLOSED.append('kms')
        #print 'CLOSED HERE: ', CLOSED
        distinctElements = []
        for row in self.boardArr:
            for element in row:
                if element not in distinctElements:
                    distinctElements.append(element)
        distinctElements.remove(' ')
        for carCh in distinctElements:
            next_for_car_CLOSED = self.next_for_car(carCh)
            for movedBoard in next_for_car_CLOSED:
                CLOSED.append(movedBoard)
            #CLOSED.append(self.next_for_car(carCh))
            #print 'in Loop: ',CLOSED
        #CLOSED.remove(None)
        #for board in CLOSED:
            #misc.printBoardArr(board)
        #CLOSED.remove([])
        #misc.printCLOSED(CLOSED)
        return CLOSED

    def nextBoards(self): # returns the 1D board Object list instead of 3D list
        boardArrs = self.next()
        boards = []
        for boardArr in boardArrs:
            board = Board()
            board.modifyBoard(boardArr)
            boards.append(board)
        return boards
    
    def random(self, N):
        CLOSED = []
        CLOSED.append(self.boardArr)
        cars = self.getCarsFromBoard()
        cloneBoard = Board()
        #for i in range(6):
            #for j in range(6):
                #bitch.boardArr[i][j] = self.boardArr[i][j]
        cloneBoard.clone(self)

        while True:
            if cloneBoard.isDone() == True:
                misc.printCLOSED(CLOSED)
                return
            if len(CLOSED) == N:
                misc.printCLOSED(CLOSED)
                return

            nextBoards = cloneBoard.next()
            boardIndex = randint(0,len(nextBoards)-1)
            nextBoard = nextBoards[boardIndex]
            if nextBoard not in CLOSED:
                CLOSED.append(nextBoard)
            cloneBoard.boardArr = nextBoard
        

        # The Code commented out underneath is for me to remember what an idiot i am.
            '''
            #print len(CLOSED)
            #newBoard = Board()
            
            if cloneBoard.isDone() == True:
                misc.printCLOSED(CLOSED)
                return
            if len(CLOSED) == 3:
                misc.printCLOSED(CLOSED)
                return

            #newBoard.printBoard()

            carIndex = randint(0,len(cars)-1)
            carToMove = cars[carIndex]
            carOrientation = self.getCarOrientation(carToMove)
            directionIndex = randint(0,1)
            units = randint(1,4)

            if carOrientation == 'vertical':
                directions = ['up','down']
                direction = directions[directionIndex]
                newBoardArr = cloneBoard.moveCar(carToMove, direction, units)
                #print newBoardArr
                if newBoardArr not in CLOSED and newBoardArr is not None:
                    CLOSED.append(newBoardArr)
            elif carOrientation == 'horizontal':
                directions = ['left','right']
                direction = directions[directionIndex]
                newBoardArr = cloneBoard.moveCar(carToMove, direction, units)
                #print newBoardArr
                cloneBoard.boardArr = newBoardArr
                if newBoardArr not in CLOSED and newBoardArr is not None:
                    CLOSED.append(newBoardArr)
            #misc.printBoardArr(newBoardArr)
            '''

    def graph(self):
        paths = []
        cloneBoard.clone(self)
        i = 0
        while True:
            path = Path()
            path.add(cloneBoard.boardArr)
            nextBoards = cloneBoard.next()
            for board in nextBoards:
                clonePath = Path()
                clonePath.clone(path)
                clonePath.add(board)
                paths.append(clonePath)
    
    def bfs(self):
        openPaths = []
        closedBoards = []
        path = Path.Path()
        cloneBoard = Board()
        cloneBoard.clone(self)
        path.add(cloneBoard)
        openPaths.append(path)
        openPaths[0].last().printBoard()
        i = 0
        while True:
            if openPaths[0].last().isDone() == True:
                openPaths[0].printPath()
                print i
                return openPaths[0]
            cloneBoard.modifyBoard(openPaths[0].last().boardArr)
            nextBoards = cloneBoard.nextBoards()
            for board in nextBoards:
                #board.printBoard()
                if board not in closedBoards:
                    clonePath = Path.Path()
                    clonePath.clone(path)
                    clonePath.add(board)
                    openPaths.append(clonePath)
            closedBoards.append(openPaths[0].last())
            newPaths = openPaths[1:]
            openPaths = newPaths
            i += 1

'''
        if cloneBoard.isDone() == True:
            cloneBoard.printBoard()
            return
        i = 0
        while True:
            nextBoards = cloneBoard.nextBoards()
            for board in nextBoards:
                path = Path()
                path.add(cloneBoard)
                path.add(board)
                paths.append(path)






        path = Path()
        pathIndex = 0
        cloneBoard.clone(self)
        while True:
            if cloneBoard.isDone() == True:
                cloneBoard.printBoard()
                return
            pathBoards = cloneBoard.next()
            for i in pathBoards:
                newBoard = Board()
                newBoard.boardArr = i
                path
'''
