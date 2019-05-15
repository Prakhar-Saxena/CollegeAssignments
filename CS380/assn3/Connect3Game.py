from random import randint

import connect3 as connect3
import Player as Player

class Connect3Game:
    def __init__(self, string= None):
        self.board = connect3.Connect3Board(string)
        self.activeTurn = 'X' # 'O' or 'X'
        self.player1 = Player.Player(string, 'X')
        self.player2 = Player.Player(string, 'O')

    def changeTurns(self):
        at = self.activeTurn
        self.activeTurn = 'O' if at == 'X' else 'X'
    
    def next(self):
        boards = self.board.next(self.activeTurn)
        # self.changeTurns()
        return boards
    
    def printNext(self):
        boards = self.next()
        s = connect3.stringify_boards(boards)
        print(s)
    
    def winner(self):
        w = self.board.winner()
        print(w)
        return w

    def random(self):
        CLOSED = []
        CLOSED.append(self.board)
        cloneBoard = self.board.clone()
        while True:
            w = self.board.winner()
            if w != None:
                s = connect3.stringify_boards(CLOSED)
                print(s)
                print(w)
                return
            if self.activeTurn == 'X':
                self.board = self.player1.random()
                self.changeTurns()
            elif self.activeTurn == 'O':
                self.board = self.player2.random()
                self.changeTurns()
            CLOSED.append(self.board)
            self.player1.modifyBoard(self.board)
            self.player2.modifyBoard(self.board)
