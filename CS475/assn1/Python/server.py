#!/usr/bin/env python3

import sys
import socket

from H import H
from misc import fileWriterList, fileWriterNum, fileReader

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

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    c.send('Thank you for connecting')

    c.close()

'''
address = ('localhost', 6000)
listener = Listener(address, authkey='predator')
conn = listener.accept()
print('connection accepted from', listener.last_accepted)
while True:
    msg = conn.recv()
    
    password = int(fileReader(filename))
    password_received = int(msg)
    if password == H(password_received):
        print(True)
        fileWriterNum(password_received, filename)
    # else:
    #     print(False)

    if msg == 'close':
        conn.close()
        break
listener.close()
'''
