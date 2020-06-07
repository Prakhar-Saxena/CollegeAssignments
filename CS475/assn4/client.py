#!/usr/bin/env python3

"""
https://www.geeksforgeeks.org/socket-programming-python/
"""

import sys
# from multiprocessing.connection import Client
from keygen import __all__
import socket

class Client(ServerClient):
    def __init__(self, name):
        self.name = name
        self.p = prime_gen(7)
        self.q = prime_gen(8)
        self.public_key = get_public_key(self.p, self.q)
        self.private_key = get_private_key(self.p, self.q)
    def send_message(self, message):

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
    client = Client("client_ps")
    ip = socket.gethostbyname(hostname)
    print('\tIP:', ip)

    s.connect((ip, int(port)))

    print(s.recv(1024))  # checking if connected here or not

    s.send(str.encode(password))

    status = s.recv(1024)
    if status == 'Password Match!':
        getPassword('user_passwords')

    print(status)

    s.close()
except:
    print('Didn\'t work')