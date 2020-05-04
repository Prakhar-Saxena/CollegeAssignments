#!/usr/bin/env python3

from Wheel import Wheel


class Enigma:
    def __init__(self):
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

    def getChout(self, chin):
        print('Processing character', chin)
        self.characterCounter += 1
        rightOut_midIn = self.rightWheel.getContactOut(self.wheel.index(chin))
        self.rightWheel.turn()
        print('The right wheel turns.')
        midOut_leftIn = self.middleWheel.getContactOut(rightOut_midIn)
        if self.characterCounter % 7 == 0:
            self.middleWheel.turn()
            print('The middle wheel turns.')
        leftOut = self.leftWheel.getContactOut(midOut_leftIn)
        if self.characterCounter % 5 == 0:
            self.leftWheel.turn()
            print('The left wheel turns.')
        print('Encrypted letter:', self.wheel[leftOut])
        print('The wheel orientations from left to right are:',
              self.leftWheel.getOrientation(), self.middleWheel.getOrientation(), self.rightWheel.getOrientation())
        return self.wheel[leftOut]

    # def getChout_ver2(self, chin):
    #     self.characterCounter += 1
    #     self.rightWheel.turn()
    #     rightOut_midIn = self.rightWheel.getContactOut(self.wheel.index(chin))
    #     if self.characterCounter % 7 == 0:
    #         self.middleWheel.turn()
    #     midOut_leftIn = self.middleWheel.getContactOut(rightOut_midIn)
    #     if self.characterCounter % 5 == 0:
    #         self.leftWheel.turn()
    #     leftOut = self.leftWheel.getContactOut(midOut_leftIn)
    #     return self.wheel[leftOut]

    def encrypt(self, message):
        chars = list(message)
        output = ''
        for char in chars:
            output += self.getChout(char)
        return output

    def getDChout(self, chin):
        print('Processing character', chin)
        if self.characterCounter % 5 == 0:
            self.leftWheel.turnOtherWay()
            print('The left wheel turns the other way.')
        leftOut_midIn = self.leftWheel.getDContactOut(self.wheel.index(chin))
        # if self.characterCounter % 5 == 0:
        #     self.leftWheel.turnOtherWay()
        if self.characterCounter % 7 == 0:
            self.middleWheel.turnOtherWay()
            print('The middle wheel turns the other way.')
        midOut_rightIn = self.middleWheel.getDContactOut(leftOut_midIn)
        # if self.characterCounter % 7 == 0:
        #     self.middleWheel.turnOtherWay()
        self.rightWheel.turnOtherWay()
        print('The right wheel turns the other way.')
        rightOut = self.rightWheel.getDContactOut(midOut_rightIn)
        print('Decrypted Letter:', self.wheel[rightOut])
        print('The wheel orientations from left to right are:',
              self.leftWheel.getOrientation(), self.middleWheel.getOrientation(), self.rightWheel.getOrientation())
        # self.rightWheel.turnOtherWay()
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
        return output
            # leftOut_midIn = self.rightWheel.getReverseContactOut()


def main():
    enigmaE = Enigma()
    print(enigmaE.encrypt('THEBEATLES'))
    enigmaD = Enigma()
    print(enigmaD.decrypt('KWN7M2873W'))
    # print(enigma.encrypt('CCI'))
    # print(enigmaD.decrypt('YL3'))

if __name__ == '__main__':
    main()
