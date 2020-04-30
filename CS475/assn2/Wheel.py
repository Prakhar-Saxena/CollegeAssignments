#!/usr/bin/env python3

class Wheel:
    def __init__(self, chin, chout, orientation):  # chin and chout refer to character in and out
        if len(chin) != len(chout):
            return
        self.wiring = dict(zip(chin, chout))
        self.orientation = orientation
        self.wheel = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.baseWheel = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def getChout(self, chin):
        return self.wiring[chin]

    def turn(self):
        self.wheel = self.wheel[1:] + [self.wheel[0]]
        self.orientation += 1
        self.orientation = self.orientation % 36

    def turnOtherWay(self):
        self.wheel = [self.wheel[-1]] + self.wheel[:-1]
        self.orientation -= 1
        if self.orientation == -1:
            self.orientation = 35
