#!/usr/bin/env python3

from random import randint

import Board as Board

class Player:
    def __init__(self, board, carCh):
        self.board = board
        self.carCh = carCh
        self.otherCar = 'x' if carCh == 'y' else 'y'

    def modifyBoard(self,board):
        self.board = board

    def random(self):
        nextBoards = self.board.nextExcludingCar(self.otherCar)
        boardIndex = randint(0,len(nextBoards)-1)
        self.board = nextBoards[boardIndex]
        return self.board

class RandomPlayer(Player):
    def __init__(self, board, carCh):
        self.board = board
        self.carCh = carCh
        self.otherCar = 'x' if carCh == 'y' else 'y'

    def modifyBoard(self,board):
        self.board = board

    def random(self):
        nextBoards = self.board.nextExcludingCar(self.otherCar)
        boardIndex = randint(0,len(nextBoards)-1)
        self.board = nextBoards[boardIndex]
        return self.board

class MinimaxPlayer(Player):
    def __init__(self, board, carCh):
        self.board = board
        self.carCh = carCh
        self.otherCar = 'x' if carCh == 'y' else 'y'

    def modifyBoard(self,board):
        self.board = board

    def minimaxDecision(self):
        nextBoards = self.board.next()
        minValues = []

