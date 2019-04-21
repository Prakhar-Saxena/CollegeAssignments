#!/usr/bin/env python3

import sys
import math
import MiscFunctions as misc
import Board as Board

CarNotIn = 'Car not in the Board'

class Car:
    carChar = ''
    end1 = [0,0] #end1 comes before end2
    end2 = [0,0]
    length = 0
    orientation = "" #vertical or horizontal
    allCoordinates = []

    def __init__(self, boardArr, carCh): # takes the board and the car character
        if misc.isCarInBoard(boardArr, carCh) == False:
            print 'Car Constructer __init__() ', CarNotIn
            return
        self.carChar = carCh
        self.allCoordinates = misc.findAll(boardArr, carCh)
        self.end1 = self.allCoordinates[0] # end1 comes before end2
        self.end2 = self.allCoordinates[len(self.allCoordinates)-1]
        self.length = len(self.allCoordinates)
        if self.end1[1] == self.end2[1]: # checking for orientation # if y coordinate is same
            self.orientation = 'vertical'
        elif self.end1[0] == self.end2[0]:
            self.orientation = 'horizontal'

    def modifyCar(self, newCarCh, newAllCoordinates):
        self.allCoordinates = newAllCoordinates
        self.carCh = newCarCh
        self.end1 = self.allCoordinates[0]
        self.end2 = self.allCoordinates[len(self.allCoordinates) - 1]
        self.length = len(self.allCoordinates)
        if self.end1[1] == self.end2[1]: # checking for orientation # if y coordinate is same
            self.orientation = 'vertical'
        elif self.end1[0] == self.end2[0]:
            self.orientation = 'horizontal'

    def printDetails(self):
        print 'Car Character: ', self.carChar
        print 'All Coordinates: ', self.allCoordinates
        print 'end1: ', self.end1
        print 'end2: ', self.end2
        print 'length: ', self.length
        print 'orientation: ', self.orientation
