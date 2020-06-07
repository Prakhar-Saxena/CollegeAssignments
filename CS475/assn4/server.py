#!/usr/bin/env python3

from keygen import __all__
from misc import __all__
import sys, socket, random


class Server(ServerClient):
    def __init__(self):
        self.p = prime_gen(0)
        self.q = prime_gen(1)
        self.public_key = get_public_key(self.p, self.q)
        self.private_key = get_private_key(self.p, self.q)
        # self.session_keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # self.sessions = {} #random.randint(1, 100)
        self.clients = {}
        fileWriterNum(self.public_key, 'server_public_key')

    def session_key_gen(self, client_name):
        session_key = random.choice(self.session_keys)
        self.sessions[session_key] = client_name

    def add_client(self, client_name, client_public_key):
        self.clients[client_name] = client_public_key

    def get_client_key(self, client_name):
        return self.clients[client_name]

    def check_client(self, client_name):
        if list(self.clients.keys()).contains(client_name):
            return True
        else:
            return False



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
    while True:
        c, addr = s.accept()
        print('Got connection from', addr)

        c.send(str.encode('Thank you for connecting'))

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
