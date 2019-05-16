from random import randint

import connect3 as connect3

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
        return minimaxDecision(self.board)

    def minimaxDecision(self):
        nextBoards = self.board.next()
        minValues = []
        for nextBoard in nextBoards:
            s = minimax(nextBoard,12, True)
            minValues.append(s)
        index = minValues.index(max(minValues))
        return nextBoards[index]

    def minimax(self, depth, maximizingPlayer):
        if depth == 0 or self.board.winner() != None:
            if self.board.winner() == 'X':
                return -1
            elif self.board.winner() == 'O':
                return 1
            elif self.board.winner() == connect3.TIE:
                return 0
            return self.board
        nextBoards = self.board.next()
        if maximizingPlayer:
            maxEval = -float("inf")
            for nextBoard in nextBoards:
                eval = minimax(nextBoard, depth - 1, False)
                maxEval = max(maxEval, eval)
            return maxEval
        else:
            minEval = float("inf")
            for nextBoard in nextBoards:
                eval = minimax(nextBoard, depth - 1, True)
                minEval = min(minEval, eval)
            return

def maxVal(board, depth):
    if board.winner() != None:
        return
    v = -float("inf")
    nextBoards = board.next()
    for a in nextBoards:
        s = None
        if a.winner() != None:
            if a.winner() == 'X':
                s = score - 1
            elif a.winner() == 'O':
                s = score + 1
            elif a.winner() == connect3.TIE:
                s = 0
        else:
            v = max(v,minVal(a,s))
    return v

def minVal(board, depth):
    if board.winner() != None:
        return
    v = -float("inf")
    nextBoards = board.next()
    for a in nextBoards:
        v = min(v,maxVal(s))
    return v

def getWinScore(board):
    w = board.winner()
