import connect3 as connect3

def minimax(board, label, depth, maximizingPlayer):
    otherLabel = 'O' if label == 'X' else 'X'
    if maximizingPlayer:
        if depth == 0 or board.winner() != None:
            if board.winner() == label:
                return 1*(depth)
            elif board.winner() == otherLabel:
                return (-1)*(depth)
            else:
                return 0
        nextBoards = board.next(label)
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
        nextBoards = board.next(otherLabel)
        minEval = float("inf")
        for nextBoard in nextBoards:
            e = minimax(nextBoard, label, depth - 1, True)
            minEval = min(minEval, e)
        return minEval

def minimax_pruning(board, label, depth, maximizingPlayer, alpha, beta):
    otherLabel = 'O' if label == 'X' else 'X'
    if maximizingPlayer:
        if depth == 0 or board.winner() != None:
            if board.winner() == label:
                return 1*(depth)
            elif board.winner() == otherLabel:
                return (-1)*(depth)
            else:
                return 0
        nextBoards = board.next(label)
        maxEval = -float("inf")
        for nextBoard in nextBoards:
            e = minimax_pruning(nextBoard, label, depth - 1, False, alpha, beta)
            maxEval = max(maxEval, e)
            aplha = max(alpha, e)
            if beta <= alpha:
                break
        return maxEval
    else:
        if depth == 0 or board.winner() != None:
            if board.winner() == label:
                return 1*(depth)
            elif board.winner() == otherLabel:
                return (-1)*(depth)
            else:
                return 0
        nextBoards = board.next(otherLabel)
        minEval = float("inf")
        for nextBoard in nextBoards:
            e = minimax_pruning(nextBoard, label, depth - 1, True, alpha, beta)
            minEval = min(minEval, e)
            beta = min(alpha,e)
            if beta <= alpha:
                break
        return minEval