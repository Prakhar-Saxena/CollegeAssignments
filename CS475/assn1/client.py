#!/usr/bin/env python3

'''
https://www.geeksforgeeks.org/socket-programming-python/
'''

import sys
from multiprocessing.connection import Client
import socket

from user import getPassword

if len(sys.argv) < 3:
    print('Invalid inpt')
    sys.exit()

hostname = sys.argv[1]
port = sys.argv[2]
pw = ''
if len(sys.argv) > 3:
    pw = sys.argv[3]

s = socket.socket()

print('Attempting to connect to')
print('\thost:', hostname)

try:
    ip = socket.gethostbyname(hostname)
    print('\tIP:', ip)

    s.connect((ip, int(port)))

    password = ''
    if pw == '':
        password = getPassword('user_passwords')
    else:
        password = pw

    print(s.recv(1024))

    s.send(str.encode(password))

    status = s.recv(1024)
    if status == 'Password Match!':
        getPassword('user_passwords')

    print(status)

    s.close()
except:
    print('Didn\'t work')
