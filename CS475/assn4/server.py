#!/usr/bin/env python3

from keygen import __all__

p, q = 2, 7
N = p * q  # 14



'''
https://www.geeksforgeeks.org/socket-programming-python/
'''

import sys
import socket

from H import H
from misc import fileWriterList, fileWriterNum, fileReader

try:
    filename = 'server_password'

    s = socket.socket()
    print('socket created')

    port = 3141

    s.bind(('',port))
    print('socket binded to ', port)

    print('Hostname: ', socket.gethostname())
    print('IP: ', socket.gethostbyname(socket.gethostname()))

    s.listen(5)
    print('socket is listening')
except:
    print('Didn\'t work')
try:
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)

        c.send(str.encode('Thank you for connecting'))

        password: int = int(fileReader(filename))
        password_received = c.recv(1024)
        print('password received:', password_received)

        if password == H(int(password_received)):
            print('Password Match!')
            fileWriterNum(int(password_received), filename)
            c.send(str.encode('Password Match!'))
        else:
            print('Invalid Pasword')
            c.send(str.encode('Ivalid Password'))

        c.close()
except:
    print('Didn\'t work')

