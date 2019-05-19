from random import randint
import time

import connect3 as connect3
import Minimax as Minimax

class Player:
    def __init__(self, string, label):
        self.board = connect3.Connect3Board(string)
        self.label = label
    
    def next(self):
        nextBoards = self.board.next(self.label)
        boardIndex = randint(0,len(nextBoards)-1)
        self.board = nextBoards[boardIndex]
        return self.board
    
    def modifyBoard(self, board):
        self.board = board.clone()

class MinimaxPlayer(Player):
    def __init__(self, string, label):
        self.board = connect3.Connect3Board(string)
        self.label = label
    
    def next(self):
        return self.minimaxDecision()

    def minimaxDecision(self):
        start = time.time()
        nextBoards = self.board.next(self.label)
        minValues = []
        for nextBoard in nextBoards:
            s = Minimax.minimax(nextBoard, self.label, 4, False)
            minValues.append(s)
        i = minValues.index(max(minValues))
        end = time.time()
        print("Time it took to make this decision with minimax without alpha-beta pruning: "+str(end-start))
        return nextBoards[i]

class MinimaxAlphaBetaPlayer(Player):
    def __init__(self, string, label):
        self.board = connect3.Connect3Board(string)
        self.label = label
    
    def next(self):
        return self.minimaxDecisionABPruning()
    
    def minimaxDecisionABPruning(self):
        start = time.time()
        nextBoards = self.board.next(self.label)
        minValues = []
        alpha = -float("inf")
        beta = float("inf")
        for nextBoard in nextBoards:
            s = Minimax.minimax_pruning(nextBoard, self.label, 4, False, alpha, beta)
            minValues.append(s)
        i = minValues.index(max(minValues))
        end = time.time()
        print("Time it took to make this decision with minimax with alpha-beta pruning: "+str(end-start))
        return nextBoards[i]