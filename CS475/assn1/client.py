#!/usr/bin/env python3

'''
https://www.geeksforgeeks.org/socket-programming-python/
'''

import sys
from multiprocessing.connection import Client
import socket

from user import getPassword

if len(sys.argv) != 3:
    print('Invalid inpt')
    sys.exit()

hostname = sys.argv[1]
port = sys.argv[2]

s = socket.socket()

print('Attempting to connect to')
print('\thost:', hostname)

try:
    ip = socket.gethostbyname(hostname)
    print('\tIP:', ip)

    s.connect((ip, int(port)))


    password = getPassword('user_passwords')

    print(s.recv(1024))

    s.send(str.encode(password))

    print(s.recv(1024))

    s.close()
except:
    print('Didn\'t work')
