#!/usr/bin/env python3

class Wheel:
    def __init__(self, cin, cout):  # pun intended
        if len(cin) != len(cout):
            return
        self.wiring = dict(zip(cin,cout))

    def getCout(self, cin):
        return self.wiring[cin]
