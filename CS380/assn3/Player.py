from random import randint

import connect3 as connect3

class Player:
    def __init__(self, string, label):
        self.board = connect3.Connect3Board(string)
        self.label = label
    
    def random(self):
        nextBoards = self.board.next(self.label)
        boardIndex = randint(0,len(nextBoards)-1)
        self.board = nextBoards[boardIndex]
        return self.board
    
    def modifyBoard(self, board):
        self.board = board.clone()
