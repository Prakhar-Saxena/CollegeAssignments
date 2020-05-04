#!/usr/bin/env python3

class Wheel:
    def __init__(self, chout, orientation):  # chin and chout refer to character in and out
        if len(chout) != 36:
            return
        self.wheel = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.wiring = dict(zip(self.wheel[:], chout))
        self.orientation = orientation

        # self.baseWheel = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        #               'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def getChout(self, chin):
        return self.wiring[chin]

    def getContactOut(self, contactIn):
        chin = self.wheel[contactIn + self.orientation]  # because the wheel has turned self.orienteation turns, so the character in is the contactIn + orientation
        chout = self.getChout(chin)
        contactOut = self.wheel.index(chout) - self.orientation
        if contactOut < 0:
            contactOut += 36
        return contactOut

    def getDContactOut(self, dContactIn):
        i = dContactIn + self.orientation
        i %= 36
        chin = self.wheel[i]
        chout = ''
        for key, value in self.wiring.items():
            if value == chin:
                chout = key
                break
        if chout == '':
            print('Something\'s wrong, I can feel it.')
        reverseContactOut = self.wheel.index(chout) - self.orientation
        return reverseContactOut

    def turn(self):
        # self.wheel = self.wheel[1:] + [self.wheel[0]]
        self.orientation += 1
        self.orientation = self.orientation % 36

    def turnOtherWay(self):
        # self.wheel = [self.wheel[-1]] + self.wheel[:-1]
        self.orientation -= 1
        if self.orientation == -1:
            self.orientation = 35

    def setOrientation(self, o):
        self.orientation = o

    def getOrientation(self):
        return self.orientation
