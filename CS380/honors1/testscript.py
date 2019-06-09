#!/usr/bin/env python3

import sys
import math
import Board 
import Car 
import MiscFunctions as misc
import Path
import RushHourGame

# command = str(sys.argv[1]) # storing the command

game = RushHourGame.RushHourGame()

# game.random()

game.minimax_pruning()

# start = time.time()

# xwin = 0
# ywin = 0
# draws = 0

# for i in range(100):
#     newGame = RushHourGame.RushHourGame()#'   |XO |   |   ')
#     w = newGame.minimax_pruning()
#     if w == 'x':
#         xwin += 1
#     elif w == 'y':
#         ywin += 1
#     elif w == None:
#         draws += 1

# print "x: ", xwin
# print "y: ", ywin
# print "There are no draws in these games."

# board = Board.Board()

# board.createBoard("      |      |xx    |     q|     q|     q")

# print board.stringifyBoard()

# print board.stringifyBoard()

# misc.printCLOSED(board.next())
# misc.printCLOSED(board.nextExcludingCar('q'))

# if len(sys.argv) > 2: # checking whether there's the optional argument for input
#     boardString = str(sys.argv[2]) # storing the argument into an input string
#     board.createBoard(boardString)

# if command == "random":
#     game.random()
# elif command == "minimax":
#     game.minimax()