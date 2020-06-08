#!/usr/bin/env python3

"""
https://www.geeksforgeeks.org/socket-programming-python/
"""

import sys
import socket
import rsa


class Client(ServerClient):
    def __init__(self, name):
        self.name = name
        self.public_key, self.private_key = rsa.newkeys(512)
        pub = fileReader('server_public_key')
        print(pub)
        pub = pub.split(',')
        print(pub)
        self.server_public_key = rsa.PublicKey()
        fileWriterString(str(self.public_key.n) + ',' + str(self.public_key.e), name + '_public_key')

    def encrypt(self, message):
        return rsa.encrypt(message, self.server_public_key)

    def decrypt(self, message):
        return rsa.decrypt(message, self.private_key)

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
    isAuthenticated = False
    isConnected = False
    client = Client("client_ps")
    while True:
        if not isConnected:
            ip = socket.gethostbyname(hostname)
            print('\tIP:', ip)

            s.connect((ip, int(port)))

            print(s.recv(1024))  # checking if connected here or not
            isConnected = True

        # Authentication

        if not isAuthenticated:
            e_client_name = client.encrypt(client.name)  ## assuming the server is up.
            s.send(e_client_name)
            nk = c.recv(1024)
            d_nk = client.decrypt(nk)
            if str(d_nk).split(',')[0] == client.name:
                c.send(b'1')
                isAuthenticated = True
            else:
                c.send(b'0')
                isConnected = False


        inp = raw_imput('Enter a message to send.')

    s.close()
except:
    print('Didn\'t work')