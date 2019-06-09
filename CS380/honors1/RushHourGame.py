#!/usr/bin/env python3

import Board as Board
import Player as Player
import MiscFunctions as Misc

class RushHourGame:
    def __init__(self):
        self.board = Board.Board()
        self.board.createBoard("    aa|      |xx    |yy   q|     q|     q")
        # self.board.printBoard()
        self.player1 = Player.RandomPlayer(self.board.boardString, 'x')
        self.player2 = Player.MinimaxPlayer(self.board.boardString, 'y')
        self.activeTurn = 'x'
    
    def createGame(self, boardString):
        self.board = Board.Board()
        self.board.createBoard(boardString)
        self.player1 = Player.RandomPlayer(self.board.boardString, 'x')
        self.player2 = Player.MinimaxPlayer(self.board.boardString, 'y')
        self.activeTurn = 'x'

    def changeTurns(self):
        at = self.activeTurn
        self.activeTurn = 'y' if at == 'x' else 'x'

    def next(self):
        boards = self.board.next(self.activeTurn)
        return boards

    def winner(self):
        w == self.board.winner()
        # print w
        return w

    def random(self):
        self.player1 = Player.RandomPlayer(self.board.boardString, 'x')
        self.player2 = Player.RandomPlayer(self.board.boardString, 'y')
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
                self.board.createBoard(self.player1.random().stringifyBoard())
                self.changeTurns()
            elif self.activeTurn == 'y':
                self.board.createBoard(self.player2.random().stringifyBoard())
                self.changeTurns()
            CLOSED.append(self.board.boardArr)
            self.player1.modifyBoard(self.board.stringifyBoard())
            self.player2.modifyBoard(self.board.stringifyBoard())

    def minimax(self):
        self.player1 = Player.RandomPlayer(self.board.boardString, 'x')
        self.player2 = Player.MinimaxPlayer(self.board.boardString, 'y')
        CLOSED = []
        CLOSED.append(self.board.boardArr)
        cloneBoard = Board.Board()
        cloneBoard.clone(self.board)
        while True:
            w = self.board.winner()
            if w != None:
                Misc.printCLOSED(CLOSED)
                print w
                return w
            if self.activeTurn == 'x':
                self.board.createBoard(self.player1.random().stringifyBoard())
                self.changeTurns()
            elif self.activeTurn == 'y':
                self.board.createBoard(self.player2.minimaxDecision().stringifyBoard())
                self.changeTurns()
            CLOSED.append(self.board.boardArr)
            self.board.printBoard()
            self.player1.modifyBoard(self.board.stringifyBoard())
            self.player2.modifyBoard(self.board.stringifyBoard()) 

    def minimax_pruning(self):
        self.player1 = Player.RandomPlayer(self.board.boardString, 'x')
        self.player2 = Player.MinimaxAlphaBetaPlayer(self.board.boardString, 'y')
        CLOSED = []
        CLOSED.append(self.board.boardArr)
        cloneBoard = Board.Board()
        cloneBoard.clone(self.board)
        while True:
            w = self.board.winner()
            if w != None:
                Misc.printCLOSED(CLOSED)
                print w
                return w
            if self.activeTurn == 'x':
                self.board.createBoard(self.player1.random().stringifyBoard())
                self.changeTurns()
            elif self.activeTurn == 'y':
                self.board.createBoard(self.player2.minimaxDecisionABPruning().stringifyBoard())
                self.changeTurns()
            CLOSED.append(self.board.boardArr)
            # self.board.printBoard()
            self.player1.modifyBoard(self.board.stringifyBoard())
            self.player2.modifyBoard(self.board.stringifyBoard())