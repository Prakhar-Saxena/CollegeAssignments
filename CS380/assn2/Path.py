#!/usr/bin/env python3

import sys
import math
import Board
import MiscFunctions as misc

class Path:
    boards = []

    def __init__(self):
        boards = []

    def add(self, board):
        self.boards.append(board)
        return

    def clone(self, path):
        self.boards = path.boards
        return

    def last(self):
        return self.boards[len(self.boards)-1]

    def printPath(self):
        misc.printCLOSED(self.boards) #or boards.boardArr
        return
