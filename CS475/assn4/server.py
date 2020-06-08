#!/usr/bin/env python3

import random
import rsa
import socket
import sys

from misc import *


class Server(ServerClient):
    def __init__(self):
        self.public_key, self.private_key = rsa.newkeys(512)
        self.available_sessions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.clients = {}
        self.client_sessions = {}
        fileWriterString(str(self.public_key.n) + ',' + str(self.public_key.e), 'server_public_key')

    def add_client(self, client_name, client_public_key):
        self.clients[client_name] = client_public_key
        session_key = random.choice(self.available_sessions)
        self.available_sessions.remove(session_key)
        self.client_sessions[client_name] = session_key

    def get_client_key(self, client_name):
        return self.clients[client_name]

    def get_client_session(self, client_name):
        return self.client_sessions[client_name]

    def check_client(self, client_name):
        if list(self.clients.keys()).contains(client_name) and list(self.client_sessions.keys()).contains(client_name):
            return True
        else:
            return False

    def encrypt(self, message, key):
        return rsa.encrypt(message, key)

    def decrypt(self, message):
        return rsa.decrypt(message, self.private_key)




'''
https://www.geeksforgeeks.org/socket-programming-python/
'''

try:
    server = Server()
    s = socket.socket()
    print('socket created')

    port = 3141

    s.bind(('', port))
    print('socket binded to ', port)

    print('Hostname: ', socket.gethostname())
    print('IP: ', socket.gethostbyname(socket.gethostname()))

    s.listen(5)
    print('socket is listening')
    # except:
    #     print('Didn\'t work')
    #
    # try:
    isAuthenticated = False
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)

        c.send(str.encode('Thank you for connecting'))

        if not isAuthenticated:
            ciphered_client_name = c.recv(1024)
            client_name = server.decrypt(ciphered_client_name)
            client_public_key = FileReader(client_name + '_public_key')
            server.add_client(client_name, client_public_key)
            session_key = server.get_client_session(client_name)
            to_send = str(client_name) + ',' + str(session_key)
            # c.send(server.encrypt(server.decrypt(str.encode(to_send)), client_public_key))  # because decrypting
            # un-encrypted message doesn't make much sense to me
            c.send(server.encrypt(str.encode(to_send), client_public_key))
            isA = c.recv(1024)
            if isA == b'1':
                isAuthenticated = True
            else:
                print('Authentication didn\'t work.')
                continue




        msg = c.recv(1024)
        print('Message received:', msg)

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
