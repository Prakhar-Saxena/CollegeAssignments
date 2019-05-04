#!/usr/bin/env python3

import sys
import math
import Board
import MiscFunctions as misc

class Path:
    #boards = []

    def __init__(self):
        self.boards = []

    def add(self, board):
        self.boards.append(board)

    def clone(self, path):
        #self.boards = []
        self.boards = path.boards

    def last(self):
        if len(self.boards) < 1:
            return
        return self.boards[len(self.boards)-1]

    def printPath(self):
        boardArrs = []
        for board in self.boards:
            boardArrs.append(board.boardArr)
        misc.printCLOSED(boardArrs) #or boards.boardArr
