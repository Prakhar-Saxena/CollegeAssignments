#!/usr/bin/env python3

import sys
from multiprocessing.connection import Listener

from H import H
from misc import fileWriterList, fileWriterNum, fileReader

filename = 'server_password'

# pass_arg = int(sys.argv[1])

password = int(fileReader(filename))

address = ('localhost', 8181)
listener = Listener(address, authkey='3.14159265')
conn = listener.accept()
print('connection accepted from', listener.last_accepted)
while True:
    msg = conn.recv()
    
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