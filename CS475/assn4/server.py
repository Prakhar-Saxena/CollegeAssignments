#!/usr/bin/env python3

from keygen import __all__
import sys
import socket

p, q = 2, 7
N = p * q  # 14

def initialise_keys():
    p = prime_gen(0)
    q = prime_gen(1)
    public_key = get_public_key(p, q)
    private_key = get_private_key(p, q)

'''
https://www.geeksforgeeks.org/socket-programming-python/
'''

try:
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

