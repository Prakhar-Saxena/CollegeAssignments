#!/usr/bin/env python3

import sys
from multiprocessing.connection import Listener

from H import H
from misc import fileWriterList, fileWriterNum, fileReader

filename = 'server_password'


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
pass_arg = int(sys.argv[1])
password = int(fileReader(filename))
password_received = int(pass_arg)
if password == H(password_received):
    print(True)
    fileWriterNum(password_received, filename)
else:
    print(False)
'''
