#!/usr/bin/env python3

from random import randint

import Board as Board
import Minimax as Minimax

class Player:
    def __init__(self, boardString, carCh):
        self.board = Board.Board()
        self.board.createBoard(boardString)
        self.carCh = carCh
        self.otherCar = 'x' if carCh == 'y' else 'y'

    def modifyBoard(self,boardString):
        self.board.createBoard(boardString)

class RandomPlayer(Player):
    def __init__(self, boardString, carCh):
        self.board = Board.Board()
        self.board.createBoard(boardString)
        self.carCh = carCh
        self.otherCar = 'x' if carCh == 'y' else 'y'

    def modifyBoard(self,boardString):
        self.board.createBoard(boardString)

    def random(self):
        nextBoards = self.board.nextBoardsExcludingCar(self.otherCar)
        boardIndex = randint(0,len(nextBoards)-1)
        self.board.clone(nextBoards[boardIndex])
        return self.board

class MinimaxPlayer(Player):
    def __init__(self, boardString, carCh):
        self.board = Board.Board()
        self.board.createBoard(boardString)
        self.carCh = carCh
        self.otherCar = 'x' if carCh == 'y' else 'y'

    def modifyBoard(self,boardString):
        self.board.createBoard(boardString)

    def minimaxDecision(self):
        nextBoards = self.board.nextBoardsExcludingCar(self.otherCar)
        minValues = []
        for nextBoard in nextBoards:
            s = Minimax.minimax(nextBoard, self.carCh, 3, False)
            minValues.append(s)
        i = minValues.index(max(minValues))
        return nextBoards[i]

class MinimaxAlphaBetaPlayer(Player):
    def __init__(self, boardString, carCh):
        self.board = Board.Board()
        self.board.createBoard(boardString)
        self.carCh = carCh
        self.otherCar = 'x' if carCh == 'y' else 'y'

    def modifyBoard(self,boardString):
        self.board.createBoard(boardString)

    def minimaxDecisionABPruning(self):
        nextBoards = self.board.nextBoardsExcludingCar(self.otherCar)
        minValues = []
        alpha = -float("inf")
        beta = float("inf")
        for nextBoard in nextBoards:
            s = Minimax.minimax_pruning(nextBoard, self.carCh, 3, False, alpha, beta)
            minValues.append(s)
        i = minValues.index(max(minValues))
        return nextBoards[i]