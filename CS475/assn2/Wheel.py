#!/usr/bin/env python3

class Wheel:
    def __init__(self, cin, cout, orientation):  # pun unintended: cin and cout refer to character in and out
        if len(cin) != len(cout):
            return
        self.wiring = dict(zip(cin, cout))
        self.orientation = orientation
        self.inWheel = cin
        self.outWheel = cout

    def getCout(self, cin):
        return self.wiring[cin]

    def turn(self):
        self.inWheel = self.inWheel[1:] + [self.inWheel[0]]
        self.outWheel = self.outWheel[1:] + [self.outWheel[0]]
