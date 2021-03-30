#!/usr/bin/env python3

import sys
import math
import Board 
import Car 
import MiscFunctions as misc
import Path
import RushHourGame

command = str(sys.argv[1]) # storing the command

game = RushHourGame.RushHourGame()

board = Board.Board()

if len(sys.argv) > 2: # checking whether there's the optional argument for input
    boardString = str(sys.argv[2]) # storing the argument into an input string
    board.createBoard(boardString)

if command == "random":
    game.random()
elif command == "minimax":
    game.minimax()

'''
if command == "print":
    board.printBoard()
elif command == "done":
    print board.isDone()
elif command == "next":
    nextBoards = board.next()
    misc.printCLOSED(nextBoards)
elif command == "random":
    board.random(10)
elif command == "bfs":
    board.bfs()
elif command == "astar":
    board.astar()
elif command == "test":
    #print misc.findAll(board.boardArr, 'q')
    board.next_for_car('o')
    #board.moveCar('q', 'up', 2)
    #print misc.find(board.boardArr, 'p')
    #print misc.findAll(board.boardArr, 'p')
    #board.moveCar('p','right',2)
'''
