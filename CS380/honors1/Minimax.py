import Board as Board

def minimax(board, label, depth, maximizingPlayer):
    otherLabel = 'y' if label == 'x' else 'x'
    if maximizingPlayer:
        if depth == 0 or board.winner() != None:
            if board.winner() == label:
                return 1*(depth)
            elif board.winner() == otherLabel:
                return (-1)*(depth)
            else:
                return 0
        nextBoards = board.nextExcludingCar(otherLabel)
        maxEval = -float("inf")
        for nextBoard in nextBoards:
            e = minimax(nextBoard, label, depth - 1, False)
            maxEval = max(maxEval, e)
        return maxEval
    else:
        if depth == 0 or board.winner() != None:
            if board.winner() == label:
                return 1*(depth)
            elif board.winner() == otherLabel:
                return (-1)*(depth)
            else:
                return 0
        nextBoards = board.nextExcludingCar(label)
        minEval = float("inf")
        for nextBoard in nextBoards:
            e = minimax(nextBoard, label, depth - 1, True)
            minEval = min(minEval, e)
        return minEval
