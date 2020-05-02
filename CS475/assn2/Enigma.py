#!/usr/bin/env python3

from Wheel import Wheel


class Enigma:
    def __init__(self):
        self.wheel = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.leftWheel = Wheel(
            ['2', 'Y', 'Z', '0', '1', 'A', 'W', 'I', 'P', 'K', 'S', 'N', '3', 'T', 'E', 'R', 'M', 'U', 'C', '5', 'V',
             '6', 'X', '7', 'F', 'Q', 'O', 'L', '4', '8', 'G', 'D', '9', 'B', 'J', 'H'],
            0
        )
        self.middleWheel = Wheel(
            ['0', 'L', 'X', '1', '2', '8', 'H', 'B', '3', 'N', 'R', 'O', 'K', 'D', 'T', '7', 'C', '6', 'P', 'I', 'V',
             'J', '4', 'A', 'U', 'W', 'M', 'E', '9', '5', 'Q', 'S', 'Z', 'G', 'Y', 'F'],
            0
        )
        self.rightWheel = Wheel(
            ['3', '5', 'H', 'E', 'F', 'G', 'D', 'Q', '8', 'M', '2', 'K', 'L', 'J', 'N', 'S', 'U', 'W', 'O', 'V', 'R',
             'X', 'Z', 'C', 'I', '9', 'T', '7', 'B', 'P', 'A', '0', '1', 'Y', '6', 4],
            0
        )
        self.characterCounter = 0

    def getChout(self, chin):
        rightOut_midIn = self.rightWheel.getContactOut(self.wheel.index(chin))
        self.rightWheel.turn()
        midOut_leftIn = self.rightWheel.getContactOut(rightOut_midIn)
        if self.characterCounter % 7 == 0:
            self.middleWheel.turn()
        leftOut = self.leftWheel.getContactOut(midOut_leftIn)
        if self.characterCounter % 5 == 0:
            self.leftWheel.turn()
        return self.wheel[leftOut]


def main():
    # wheel = Wheel(
    #     ['2', 'Y', 'Z', '0', '1', 'A', 'W', 'I', 'P', 'K', 'S', 'N', '3', 'T', 'E', 'R', 'M', 'U', 'C', '5', 'V',
    #      '6', 'X', '7', 'F', 'Q', 'O', 'L', '4', '8', 'G', 'D', '9', 'B', 'J', 'H'],
    #     0
    # )
    # wheel.turn()
    # print(wheel.getContactOut(0))
    enigma = Enigma()
    print(enigma.getChout('C'))
    print(enigma.getChout('C'))
    print(enigma.getChout('I'))


if __name__ == '__main__':
    main()
