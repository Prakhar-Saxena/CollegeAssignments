import sys
import time

import connect3 as connect3
import Connect3Game as Connect3Game

newGame = Connect3Game.Connect3Game('O  |   |X  |X  ')
newGame.changeTurn('O')
# board = connect3.Connect3Board('   |XO |   |   ')

# print(str(board))

w = newGame.minimax()

newGame = Connect3Game.Connect3Game('O  |   |X  |X  ')
newGame.changeTurn('O')
w = newGame.minimax_pruning()

# start = time.time()

# owin = 0
# xwin = 0
# draws = 0

# for i in range(100):
#     newGame = Connect3Game.Connect3Game()#'   |XO |   |   ')
#     w = newGame.minimax()
#     if w == 'O':
#         owin += 1
#     elif w == 'X':
#         xwin += 1
#     elif w == connect3.TIE:
#         draws += 1

# print (f"O: {owin}")
# print (f"X:  {xwin}")
# print (f"Draws: {draws}")

# end = time.time()

# print("time for minimax(): "+str(end-start))
# print("\nPRUNING\n")

# newStart = time.time()

# owin = 0
# xwin = 0
# draws = 0

# for i in range(100):
#     newGame = Connect3Game.Connect3Game()#'   |XO |   |   ')
#     w = newGame.minimax_pruning()
#     if w == 'O':
#         owin += 1
#     elif w == 'X':
#         xwin += 1
#     elif w == connect3.TIE:
#         draws += 1

# print (f"O: {owin}")
# print (f"X:  {xwin}")
# print (f"Draws: {draws}")

# newEnd = time.time()

# print("time for minimax_pruning(): "+str(newEnd-newStart))