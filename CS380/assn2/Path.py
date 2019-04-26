#!/usr/bin/env python3

import sys
import math
import Board
import MiscFunctions as misc

class Path:
    boards = []

    def add(board):
        self.boards.append(board)
        return

    def clone(path):
        self.boards = path.boards
        return

    def last():
        return boards[len(boards)]

    def printPath():
        misc.printCLOSED(boards) #or boards.boardArr
        return
