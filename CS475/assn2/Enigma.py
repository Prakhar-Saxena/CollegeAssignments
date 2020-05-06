#!/usr/bin/env python3

import sys
from Wheel import Wheel


class Enigma:
    def __init__(self, orientations, permutator):
        self.wheel = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                      'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.leftWheel = Wheel(
            ['2', 'Y', 'Z', '0', '1', 'A', 'W', 'I', 'P', 'K', 'S', 'N', '3', 'T', 'E', 'R', 'M', 'U',
             'C', '5', 'V', '6', 'X', '7', 'F', 'Q', 'O', 'L', '4', '8', 'G', 'D', '9', 'B', 'J', 'H'],
            0
        )
        self.middleWheel = Wheel(
            ['0', 'L', 'X', '1', '2', '8', 'H', 'B', '3', 'N', 'R', 'O', 'K', 'D', 'T', '7', 'C', '6',
             'P', 'I', 'V', 'J', '4', 'A', 'U', 'W', 'M', 'E', '9', '5', 'Q', 'S', 'Z', 'G', 'Y', 'F'],
            0
        )
        self.rightWheel = Wheel(
            ['3', '5', 'H', 'E', 'F', 'G', 'D', 'Q', '8', 'M', '2', 'K', 'L', 'J', 'N', 'S', 'U', 'W',
             'O', 'V', 'R', 'X', 'Z', 'C', 'I', '9', 'T', '7', 'B', 'P', 'A', '0', '1', 'Y', '6', '4'],
            0
        )
        self.characterCounter = 0  # can be used both for encryption and decryption
        for orientation in range(orientations[0]):
            self.leftWheel.turn()
        for orientation in range(orientations[1]):
            self.middleWheel.turn()
        for orientation in range(orientations[2]):
            self.rightWheel.turn()
        self.permutator = permutator

    def printState(self):
        print('The wheel orientations from left to right are:',
              self.leftWheel.getOrientation(), self.middleWheel.getOrientation(), self.rightWheel.getOrientation())

    def getChout(self, chin):
        print('Processing character', chin)
        self.characterCounter += 1
        self.rightWheel.turn()
        print('The right wheel turns.')
        if self.characterCounter % 7 == 0:
            self.middleWheel.turn()
            print('The middle wheel turns.')
        if self.characterCounter % 5 == 0:
            self.leftWheel.turn()
            print('The left wheel turns.')
        self.printState()
        print('Still processing', chin)
        rightOut_midIn = self.rightWheel.getContactOut(self.wheel.index(chin))
        midOut_leftIn = self.middleWheel.getContactOut(rightOut_midIn)
        leftOut = self.leftWheel.getContactOut(midOut_leftIn)
        print('Encrypted letter:', self.wheel[leftOut])
        self.printState()
        return self.wheel[leftOut]

    def encrypt(self, message):
        initChars = list(message)
        chars = []
        if len(initChars) == 10:
            for i in self.permutator:
                chars.append(initChars[i])
        else:
            chars = initChars[:]
        output = ''
        for char in chars:
            output += self.getChout(char)
        return output

    def getDChout(self, chin):
        print('Processing character', chin)
        self.printState()
        leftOut_midIn = self.leftWheel.getDContactOut(self.wheel.index(chin))
        # if self.characterCounter % 5 == 0:
        #     self.leftWheel.turnOtherWay()
        midOut_rightIn = self.middleWheel.getDContactOut(leftOut_midIn)
        # if self.characterCounter % 7 == 0:
        #     self.middleWheel.turnOtherWay()
        rightOut = self.rightWheel.getDContactOut(midOut_rightIn)
        print('Decrypted Letter:', self.wheel[rightOut])
        self.printState()
        # self.rightWheel.turnOtherWay()
        if self.characterCounter % 5 == 0:
            self.leftWheel.turnOtherWay()
            print('The left wheel turns the other way.')
        if self.characterCounter % 7 == 0:
            self.middleWheel.turnOtherWay()
            print('The middle wheel turns the other way.')
        self.rightWheel.turnOtherWay()
        print('The right wheel turns the other way.')
        self.characterCounter -= 1
        return self.wheel[rightOut]


    def decrypt(self, message):
        chars = list(message)
        self.characterCounter = len(chars)
        for i in range(1, self.characterCounter+1):
            self.rightWheel.turn()
            if i % 7 == 0:
                self.middleWheel.turn()
            if i % 5 == 0:
                self.leftWheel.turn()
        charsReversed = chars[::-1]
        output = ''
        for char in charsReversed:
            output = self.getDChout(char) + output
        properOutput = ['', '', '', '', '', '', '', '', '', '', '']
        if len(chars) == 10:
            for i, j in zip(self.permutator, range(0, 10)):
                properOutput[i] = output[j]
        else:
            properOutput = output[:]
        op = ''
        for i in properOutput:
            op += i
        return op

    def protoGetChout(self, chin):
        print('Processing character', chin)
        self.printState()
        self.characterCounter += 1
        rightOut_midIn = self.rightWheel.getContactOut(self.wheel.index(chin))
        midOut_leftIn = self.middleWheel.getContactOut(rightOut_midIn)
        leftOut = self.leftWheel.getContactOut(midOut_leftIn)
        print('Encrypted letter:', self.wheel[leftOut])
        self.rightWheel.turn()
        print('The right wheel turns.')
        if self.characterCounter % 7 == 0:
            self.middleWheel.turn()
            print('The middle wheel turns.')
        if self.characterCounter % 5 == 0:
            self.leftWheel.turn()
            print('The left wheel turns.')
        self.printState()
        return self.wheel[leftOut]

    def protoEncrypt(self, message):
        chars = list(message)
        output = ''
        for char in chars:
            output += self.protoGetChout(char)
        return output

    def protoGetDChout(self, chin):
        print('Processing character', chin)
        self.printState()
        if self.characterCounter % 5 == 0:
            self.leftWheel.turnOtherWay()
            print('The left wheel turns the other way.')
        if self.characterCounter % 7 == 0:
            self.middleWheel.turnOtherWay()
            print('The middle wheel turns the other way.')
        self.rightWheel.turnOtherWay()
        print('The right wheel turns the other way.')
        leftOut_midIn = self.leftWheel.getDContactOut(self.wheel.index(chin))
        # if self.characterCounter % 5 == 0:
        #     self.leftWheel.turnOtherWay()
        midOut_rightIn = self.middleWheel.getDContactOut(leftOut_midIn)
        # if self.characterCounter % 7 == 0:
        #     self.middleWheel.turnOtherWay()
        rightOut = self.rightWheel.getDContactOut(midOut_rightIn)
        print('Decrypted Letter:', self.wheel[rightOut])
        self.printState()
        # self.rightWheel.turnOtherWay()
        self.characterCounter -= 1
        return self.wheel[rightOut]

    def protoDecrypt(self, message):
        chars = list(message)
        self.characterCounter = len(chars)
        for i in range(1, self.characterCounter+1):
            self.rightWheel.turn()
            if i % 7 == 0:
                self.middleWheel.turn()
            if i % 5 == 0:
                self.leftWheel.turn()
        charsReversed = chars[::-1]
        output = ''
        for char in charsReversed:
            output = self.protoGetDChout(char) + output
        return output
            # leftOut_midIn = self.rightWheel.getReverseContactOut()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('You didn\'t pass enough arguments.')
        sys.exit()
    textIn = sys.argv[2]
    orientation = [5, 4, 2]
    # permutator = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    permutator = [3, 1, 4, 2, 8, 5, 0, 7, 6, 9]
    enigmaE = Enigma(orientation, permutator)
    enigmaD = Enigma(orientation, permutator)
    # encryption = enigmaE.encrypt('YUMMYRAMEN')
    # encryption = enigmaE.encrypt('THEBEATLES')
    # encryption = enigmaE.encrypt('CCICCI')
    print('String entered:', textIn)
    if sys.argv[1] == 'encrypt':
        encryption = enigmaE.encrypt(textIn.upper())
        print('-' * 100)
        print(encryption)
        print('-' * 100)
    elif sys.argv[1] == 'decrypt':
        decryption = enigmaD.decrypt(textIn.upper())
        print('-' * 100)
        print(decryption)
        print('-' * 100)
    else:
        print('Didn\'t work')
