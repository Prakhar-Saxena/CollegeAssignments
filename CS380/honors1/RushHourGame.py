#!/usr/bin/env python3

import Board as Board
import Player as Player
import MiscFunctions as Misc

class RushHourGame:
    def __init__(self):
        self.board = Board.Board()
        self.board.createBoard("  o aa|  o   |xxo   |yy   q|     q|     q")
        self.player1 = Player.MinimaxPlayer(self.board, 'x')
        self.player2 = Player.RandomPlayer(self.board, 'y')
        self.activeTurn = 'x'

    def changeTurns(self):
        at = self.activeTurn
        self.activeTurn = 'y' if at == 'x' else 'x'

    def next(self):
        boards = self.board.next(self.activeTurn)
        return boards

    def winner(self):
        w == self.board.winner()
        print w
        return w

    def random(self):
        self.player1 = Player.RandomPlayer(self.board, 'x')
        self.player2 = Player.RandomPlayer(self.board, 'y')
        CLOSED = []
        CLOSED.append(self.board)
        cloneBoard = Board.Board()
        cloneBoard.clone(self.board)
        while True:
            w = self.board.winner()
            if w != None:
                Misc.printCLOSED(CLOSED)
                print w
                return w
            if self.activeTurn == 'x':
                self.board = self.player1.random()
                self.changeTurns()
            elif self.activeTurn == 'y':
                self.board = self.player2.random()
                self.changeTurns()
            CLOSED.append(self.board)
            self.player1.modifyBoard(self.board)
            self.player2.modifyBoard(self.board)
