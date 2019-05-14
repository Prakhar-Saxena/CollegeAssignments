import math
import random
import sys


CONNECT = 3
COLS = 4
ROWS = 3
EMPTY = ' '
TIE = 'TIE'


class Connect3Board:

    def __init__(self, string=None):
        if string is not None:
            self.b = [list(line) for line in string.split('|')]
        else:
            self.b = [list(EMPTY * ROWS) for i in range(COLS)]

    def compact_string(self):
        return '|'.join([''.join(row) for row in self.b])

    def clone(self):
        return Connect3Board(self.compact_string())

    def get(self, i, j):
        return self.b[i][j] if i >= 0 and i < COLS and j >= 0 and j < ROWS else None

    def row(self, j):
        return [self.get(i, j) for i in range(COLS)]

    def put(self, i, j, val):
        self.b[i][j] = val
        return self

    def empties(self):
        return self.compact_string().count(EMPTY)

    def first_empty(self, i):
        j = ROWS - 1
        if self.get(i, j) != EMPTY:
            return None
        while j >= 0 and self.get(i, j) == EMPTY:
            j -= 1
        return j+1
    
    def place(self, i, label):
        j = self.first_empty(i)
        if j is not None:
            self.put(i, j, label)
        return self

    def equals(self, board):
        return self.compact_string() == board.compact_string()
    
    def next(self, label):
        boards = []
        for i in range(COLS):
            j = self.first_empty(i)
            if j is not None:
                board = self.clone()
                board.put(i, j, label)
                boards.append(board)
        return boards
    
    def _winner_test(self, label, i, j, di, dj):
        for _ in range(CONNECT-1):
            i += di
            j += dj
            if self.get(i, j) != label:
                return False
        return True
    
    def winner(self):
        for i in range(COLS):
            for j in range(ROWS):
                label = self.get(i, j)
                if label != EMPTY:
                    if self._winner_test(label, i, j, +1, 0) \
                            or self._winner_test(label, i, j, 0, +1) \
                            or self._winner_test(label, i, j, +1, +1) \
                            or self._winner_test(label, i, j, -1, +1):
                        return label
        return TIE if self.empties() == 0 else None

    def __str__(self):
        return stringify_boards([self])


def stringify_boards(boards):
    if len(boards) > 6:
        return stringify_boards(boards[0:6]) + '\n' + stringify_boards(boards[6:])
    else:
        s = ' '.join([' ' + ('-' * COLS) +' '] * len(boards)) + '\n'
        for j in range(ROWS):
            rows = []
            for board in boards:
                rows.append('|' + ''.join(board.row(ROWS-1-j)) + '|')
            s += ' '.join(rows) + '\n'
        s += ' '.join([' ' + ('-' * COLS) +' '] * len(boards))
        return s


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        board = Connect3Board(sys.argv[2] if len(sys.argv) > 2 else None)
        if cmd == 'print':
            print(board)
