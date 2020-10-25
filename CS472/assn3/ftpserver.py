#!/usr/bin/env python3
#
# CS 472 - Homework # 2
# Prakhar Saxena
# ftpclient.py

import sys
import socket
from Logger import Logger

class FtpServer:
    def __init__(self, port):
        logger.log('ftpServer initialised.')
        self.port = port
        self.c = None
        self.is_logged_in = False
        self.user_name = None
        self.user_pass = None
        try:
            self.s = socket.socket()
        except Exception as e:
            logger.log_err(str(e))

    def initialise(self, user_name, password):
        try:
            logger.log('Initialising the server.')

            self.s.bind(('', self.port))
            self.s.listen(20)
            self.menu_repl()
        except Exception as e:
            logger.log_err(str(e))

    @staticmethod
    def str_to_bytes(string):
        return bytes(string, 'utf-8')

    def is_logged_in(self):
        if not self.is_logged_in:
            self.c.send('530 Login with USER and PASS.\n')
        else:
            return

    def quit_command(self):
        try:
            logger.log_attempt('QUIT')
            self.c.send(FtpServer.str_to_bytes('221 Goodbye.\n'))
            logger.log('Response: 221 Goodbye.')
        except Exception as e:
            logger.log_err(str(e))

    def menu_repl(self):
        while True:
            self.c, addr = self.s.accept()
            logger.log('Connection from: ' + str(addr))
            self.c.send(FtpServer.str_to_bytes('220 You are now connected to ps668 FTP server.'))
            while True:
                self.command_switch()

    def command_switch(self):
        client_input = self.c.recv(1024)
        if client_input == 'PWD':
            self.pwd_command()
        elif client_input == 'QUIT':
            self.quit_command()
        elif 'CWD' in client_input:
            self.cwd_command(client_input)
        elif 'USER' in client_input:
            self.user_command()
        elif 'PORT' in client_input:
            self.port_command()
        elif

        else:
            return

        if user_choice == 'USER':
            self.user_command()
        elif user_choice == 'PASS':
            self.pass_command()
        elif user_choice == 'CWD':
            self.cwd_command()
        elif user_choice == 'QUIT':
            self.quit_command()
        elif user_choice == 'PASV':
            self.pasv_command()
        elif user_choice == 'EPSV':
            self.epsv_command()
        elif user_choice == 'PORT':
            self.port_command()
        elif user_choice == 'EPRT':
            self.eprt_command()
        elif user_choice == 'RETR':
            self.retr_command()
        elif user_choice == 'STOR':
            self.stor_command()
        elif user_choice == 'PWD':
            self.pwd_command()
        elif user_choice == 'SYST':
            self.syst_command()
        elif user_choice == 'LIST':
            self.list_command()
        elif user_choice == 'HELP':
            self.help_command()

    def pwd_command(self):
        self.is_logged_in()
        if self.is_logged_in:
            logger.log('Request: PWD')


def main():
    if len(sys.argv) != 3:
        print('Invalid number of arguments.')
        sys.exit(0)

    log_file_name = sys.argv[1]
    port = sys.argv[2]
    global logger
    logger = Logger(log_file_name)
    ftpServer = FtpServer(port)


if __name__ == '__main__':
    main()
