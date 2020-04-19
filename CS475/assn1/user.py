#!/usr/bin/env python3

from misc import fileReader, fileWriterList

def getPassword(filename):
    fileString = fileReader(filename)
    passwords = fileString.split()
    current_password = passwords.pop()
    fileWriterList(passwords, filename)
    print('Current Password', current_password)
    return current_password

getPassword('user_passwords')
