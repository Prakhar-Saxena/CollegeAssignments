#!/usr/bin/env python3
#
# CS 472 - Homework # 2
# Prakhar Saxena
# ftpclient.py

import sys
import socket
import os
import re
from Logger import Logger

class FtpServer:
    def __init__(self, port):
        logger.log('ftpServer initialised.')
        self.port = port
        self.c = None
        self.is_logged_in = False
        self.user_name = None
        self.user_pass = None
        self.is_port = False
        self.is_passive = False
        self.is_eprt = False
        self.is_epsv = False
        self.data_receiving_socket = None
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

    @staticmethod
    def create_new_socket():
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def logged_in_check(self):
        if not self.is_logged_in:
            self.c.send('530 Login with USER and PASS.\n')
            return False
        else:
            return True

    def pwd_command(self):
        try:
            self.logged_in_check()
            if self.is_logged_in:
                logger.log('Request: PWD')
                working_directory = os.getcwd()
                response = '257 \"' + working_directory + '\"\n'
                self.c.send(FtpServer.str_to_bytes(response))
                logger.log('Response: ' + response)
        except Exception as e:
            logger.log_err(str(e))

    def quit_command(self):
        try:
            logger.log_attempt('QUIT')
            self.c.send(FtpServer.str_to_bytes('221 Goodbye.\n'))
            logger.log('Response: 221 Goodbye.')
        except Exception as e:
            logger.log_err(str(e))

    def port_command(self, client_input):
        try:
            logger.log_attempt('PORT')
            if self.logged_in_check():
                logger.log('Received: ' + client_input)
                input_mod = client_input[5:].replace(',', '.')

                match = re.search('(\d+\.\d+\.\d+\.\d+)(\.\d+)(\.\d+)', client_input)
                if match:
                    ip_address = match.group(1)
                    port_1 = match.group(2)
                    port_2 = match.group(3)
                port_1 = int(port_1.replace('.', ''))
                port_2 = int(port_2.replace('.', ''))
                port = int((port_1 * 256) + port_2)
                self.data_receiveing_socket = FtpServer.create_new_socket()
                self.data_receiveing_socket.connect((ip_address, port))
                self.c.send('200 PORT command successful.')
                logger.log('Response: 200 PORT command successful.')
                self.is_port = True
                self.is_passive = False
                self.is_eprt = False
                self.is_epsv = False
                # not checking for lust retr or stor here because menu repl takes care of that
        except Exception as e:
            logger.log_err(str(e))

    def eprt_command(self, client_input):
        try:
            logger.log_attempt('EPRT')
            if self.logged_in_check():
                logger.log('Received: ' + client_input)
                client_input_mod = client_input[10:]  # getting the ip and ports
                logger.log(client_input_mod)
                ip_address = ''
                port = ''
                match = re.search('(\d+\.\d+\.\d+\.\d+)(\|\d+)', client_input_mod)
                if match:
                    ip_address = match.group(1)
                    port = match.group(2)
                port = port[1:]
                self.data_receiveing_socket = FtpServer.create_new_socket()
                self.data_receiveing_socket.connect((ip_address, int(port)))

                self.c.send('200 EPRT command successful.')
                logger.log('Response: 200 EPRT command successful.')
                self.is_eprt = True
                self.is_port = False
                self.is_passive = False
                self.is_epsv = False
                # not checking for lust retr or stor here because menu repl takes care of that
        except Exception as e:
            logger.log_err(str(e))

    def pasv_command(self, client_input):
        try:
            logger.log_attempt('PASV')
            if self.logged_in_check():
                self.data_receiveing_socket = FtpServer.create_new_socket()
                self.data_receiveing_socket.bind((socket.gethostbyname(socket.gethostname()), 0))
                self.data_receiveing_socket.listen(1)
                logger.log('Data Receiving Socket created.')
                port_1 = int((self.data_receiveing_socket.getsockname()[1]) / 256)
                port_2 = int((self.data_receiveing_socket.getsockname()[1]) - (port_1 * 256))
                self.c.send('227 Entering Passive Mode.')
                logger.log('Response: 227 Entering Passive Mode.' + str(port_1) + '; ' + str(port_2))
                self.is_passive = True
                self.is_eprt = False
                self.is_port = False
                self.is_epsv = False
                # not checking for lust retr or stor here because menu repl takes care of that
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
            self.port_command(client_input)
        elif 'EPRT' in client_input:
            self.eprt_command(client_input)
        elif 'PASV' in client_input:
            self.pasv_command(client_input)

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
