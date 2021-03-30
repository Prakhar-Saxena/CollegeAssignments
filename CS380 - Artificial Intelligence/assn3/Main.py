import sys

import connect3 as connect3
import Connect3Game as Connect3Game

print("in main")

command = str(sys.argv[1])

game = Connect3Game.Connect3Game()#'   |XO |   |   ')

if len(sys.argv) > 2:
    boardString = str(sys.argv[2])
    game = Connect3Game.Connect3Game(boardString)



if command == "next":
    game.printNext()
elif command == "random":
    game.random()
elif command == "minimax":
    game.minimax()
elif command == "alphabeta":
    game.minimax_pruning()