#!/usr/bin/env python3
#
# CS 472 - Homework # 3
# Prakhar Saxena
# ftpserver.py

import sys
import socket
import os
import re
import subprocess
from Logger import Logger

class FtpServer:
    '''
    initialise the server with port
    '''
    def __init__(self, port):
        logger.log('ftpServer initialised.')
        self.port = int(port)
        self.c = None
        self.is_valid_user_name = False
        self.is_valid_user_pass = False
        self.is_logged_in = False
        self.user_name = None
        self.user_pass = None
        self.is_port = False
        self.is_passive = False
        self.is_eprt = False
        self.is_epsv = False
        self.data_receiving_socket = None
        self.client_input = None
        self.valid_users = {'cs472': 'hw2ftp'}
        self.valid_user = ('cs472', 'hw2ftp')
        self.socket = None

    '''
    initialise the server with a proper connection, login and the menu-REPL
    '''
    def initialise(self):   #, user_name, password):
        try:
            logger.log('Initialising the server.')
            print("IP Address: " + socket.gethostbyname(socket.gethostname()))
            print("Port Number: " + str(self.port))

            self.s = socket.socket()
            logger.log('Socket created.')
            print('Socket created.')
            self.s.bind(('', self.port))
            logger.log('Socket successfully binded.')
            print('Socket successfully binded.')
            self.s.listen(20)
            logger.log('Socket is listening.')
            print('Socket is listening.')
            while True:
                self.c, addr = self.s.accept()
                logger.log('Connection from: ' + str(addr))
                print('Connection from: ' + str(addr))
                self.c.send(FtpServer.str_to_bytes('220 You are now connected to ps668 FTP server.\n'))
                logger.log_response('220 You are now connected to ps668 FTP server.')
                print('220 You are now connected to ps668 FTP server.')
                self.login_command()
                self.menu_repl()
        except Exception as e:
            logger.log_err(str(e))

    '''
    converts string to bytes
    needed this method because sockets require bytes and not strings.
    '''
    @staticmethod
    def str_to_bytes(string):
        return bytes(string, 'utf-8')

    '''
    creates new socket
    '''
    @staticmethod
    def create_new_socket():
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    '''
    checks whether a client is logged in or not
    returns True and False accordingly
    '''
    def logged_in_check(self):
        if not self.is_logged_in:
            self.c.send(FtpServer.str_to_bytes('530 Login with USER and PASS.\n'))
            return False
        else:
            return True

    '''
    checks whether the client has any mode active or not
    returns True and False accordingly
    '''
    def mode_check(self):
        if (not self.is_port) and (not self.is_passive) and (not self.is_eprt) and (not self.is_epsv):
            self.c.send(FtpServer.str_to_bytes('425 Use PORT or PASV first.\n'))
            return False
        else:
            return True

    '''
    runs after passive, epsv, port and eprt commands
    '''
    def after_mode_command(self):
        self.client_input = str(self.c.recv(1024).strip())[2:-1]
        if 'LIST' in self.client_input:
            self.list_command()
        elif 'RETR' in self.client_input:
            self.retr_command()
        elif 'STOR' in self.client_input:
            self.stor_command()

    '''
    takes care of the initial login with user and password
    due to time constraint has the username hardcoded, trying to mimic the Professor's FTP server..
    '''
    def login_command(self):
        try:
            logger.log_attempt('Logging in')
            self.user_name = str(self.c.recv(1024).strip())[7:-1]
            logger.log('Received: username: ' + self.user_name)

            self.c.send(FtpServer.str_to_bytes('331 Specify password.\n'))
            logger.log_response('331 Specify password.')
            self.user_pass = str(self.c.recv(1024).strip())[7:-1]

            if self.user_name == self.valid_user[0] and self.user_pass == self.valid_user[1]:
                self.is_logged_in = True
            else:
                logger.log('Invalid username/password received.')
                self.is_logged_in = False

            if self.is_logged_in:
                self.c.send(FtpServer.str_to_bytes('230 Login successful.\n'))
                logger.log_response('230 Login successful.')
                # SYST
                syst = str(self.c.recv(1024).strip())
                logger.log('Received: ' + syst)
                self.c.send(FtpServer.str_to_bytes('215 UNIX Type: L8\n'))
                logger.log_response('215 UNIX Type: L8')
            else:
                self.c.send(FtpServer.str_to_bytes('530 Login failed.\n'))
                logger.log_response('530 Login failed.')
                syst = str(self.c.recv(1024).strip())
                logger.log('Received: ' + syst)
                self.c.send(FtpServer.str_to_bytes('530 Login with USER and PASS.\n'))
                logger.log_response('530 Login with USER and PASS.')
        except Exception as e:
            logger.log_err(str(e))

    '''
    USER command
    handles the username and password from the client
    '''
    def user_command(self):
        try:
            logger.log_attempt('USER')
            if self.is_logged_in and self.client_input == self.valid_user[0]:
                self.c.send(FtpServer.str_to_bytes('331 Any password will do.\n'))
                logger.log_response('331 Any password will do.')
                password = str(self.c.recv(1024).strip())
                logger.log(password)
                self.c.send(FtpServer.str_to_bytes('230 Already logged in.\n'))
                logger.log_response('230 Already logged in.')
                syst = str(self.c.recv(1024).strip())
                logger.log('Received: ' + syst)
                self.c.send(FtpServer.str_to_bytes('215 UNIX Type: L8\n'))
                logger.log_response('215 UNIX Type: L8')
            elif self.is_logged_in and self.client_input != self.valid_user[0]:
                self.c.send(FtpServer.str_to_bytes('331 Cannot change to another user.\n'))
                logger.log_response('331 Cannot change to another user.')
                password = str(self.c.recv(1024).strip()).strip()
                logger.log(password)
                self.c.send(FtpServer.str_to_bytes('230 Already logged in.\n'))
                logger.log_response('230 Already logged in.')
                syst = str(self.c.recv(1024).strip())
                logger.log('Received: ' + syst)
                self.c.send(FtpServer.str_to_bytes('215 UNIX Type: L8\n'))
                logger.log_response('215 UNIX Type: L8')
            elif not self.is_logged_in and self.client_input == self.valid_user[0]:
                self.c.send(FtpServer.str_to_bytes('331 Specify password.\n'))
                logger.log_response('331 Specify password.')
                password = str(self.c.recv(1024).strip())
                if password != self.valid_user[1]:
                    self.c.send(FtpServer.str_to_bytes('530 login failed.\n'))
                    logger.log_response('530 login failed.')
                else:
                    self.c.send(FtpServer.str_to_bytes('230 Login successful.\n'))
                    logger.log_response('230 Login successful.')
                    syst = str(self.c.recv(1024).strip())
                    logger.log('Received: ' + syst)
                    self.c.send(FtpServer.str_to_bytes('215 UNIX Type: L8\n'))
                    logger.log_response('215 UNIX Type: L8')
                    self.is_logged_in = True
            elif not self.is_logged_in and self.client_input != self.valid_user[0]:
                self.c.send(FtpServer.str_to_bytes('331 Specify password.\n'))
                logger.log_response('331 Specify password.')
                password = str(self.c.recv(1024).strip())
                logger.log('Received: ' + password)
                self.c.send(FtpServer.str_to_bytes('530 Login failed.\n'))
                logger.log_response('530 Login failed.')
        except Exception as e:
            logger.log_err(str(e))

    '''
    PWD command
    returns the working directory to the client
    same as the pwd command on the unix terminal
    '''
    def pwd_command(self):
        try:
            logger.log_attempt('PWD')
            if self.logged_in_check():
                logger.log('Request: PWD')
                working_directory = os.getcwd()
                response = '257 \"' + working_directory + '\"\n'
                self.c.send(FtpServer.str_to_bytes(response))
                logger.log_response(response)
        except Exception as e:
            logger.log_err(str(e))

    '''
    CWD command
    lets the client change the working directory
    note: in the unix ftp client, the user has to use cd and not CWD
    '''
    def cwd_command(self):
        try:
            logger.log_attempt('CWD')
            if self.logged_in_check():
                dir_input = self.client_input[4:]
                if os.path.isdir(dir_input):
                    os.chdir(dir_input)
                    self.c.send(FtpServer.str_to_bytes('250 Directory changed.\n'))
                    logger.log_response('250 Directory changed.')
                else:
                    self.c.send(FtpServer.str_to_bytes('550 CWD failed.\n'))
                    logger.log_response('550 CWD failed')
        except Exception as e:
            logger.log_err(str(e))

    '''
    QUIT command
    lets the user quit the server and thus the client.
    '''
    def quit_command(self):
        try:
            logger.log_attempt('QUIT')
            self.c.send(FtpServer.str_to_bytes('221 Goodbye.\n'))
            logger.log_response('221 Goodbye.')
            print('221 Goodbye.')
            sys.exit(0)
        except Exception as e:
            logger.log_err(str(e))

    '''
    PORT command
    lets the client turn on the port mode and turn off all the other modes
    '''
    def port_command(self):
        try:
            logger.log_attempt('PORT')
            if self.logged_in_check():
                logger.log('Received: ' + self.client_input)
                input_mod = self.client_input[5:].replace(',', '.')
                match = re.search('(\d+\.\d+\.\d+\.\d+)(\.\d+)(\.\d+)', input_mod)
                if match:
                    ip_address = match.group(1)
                    port_1 = int(match.group(2).replace('.', ''))
                    port_2 = int(match.group(3).replace('.', ''))
                    port = int((port_1 * 256) + port_2)
                    self.data_receiving_socket = FtpServer.create_new_socket()
                    self.data_receiving_socket.connect((ip_address, port))
                    self.c.send(FtpServer.str_to_bytes("200 PORT command successful." + "\n"))
                    self.is_port = True
                    self.is_passive = False
                    self.is_eprt = False
                    self.is_epsv = False
                    logger.log_response('200 PORT command successful.')
                    self.after_mode_command()
                else:
                    return
                # not checking for lust retr or stor here because menu repl takes care of that
        except Exception as e:
            logger.log_err(str(e))

    '''
    EPRT command
    basically the same as PORT but with different format
    '''
    def eprt_command(self):
        try:
            logger.log_attempt('EPRT')
            if self.logged_in_check():
                logger.log('Received: ' + self.client_input)
                client_input_mod = self.client_input[10:]  # getting the ip and ports
                logger.log(client_input_mod)
                ip_address = ''
                port = ''
                match = re.search('(\d+\.\d+\.\d+\.\d+)(\|\d+)', client_input_mod)
                if match:
                    ip_address = match.group(1)
                    port = match.group(2)
                port = port[1:]
                self.data_receiving_socket = FtpServer.create_new_socket()
                self.data_receiving_socket.connect((ip_address, int(port)))

                self.c.send(FtpServer.str_to_bytes('200 EPRT command successful.\n'))
                logger.log_response('200 EPRT command successful.')
                self.is_eprt = True
                self.is_port = False
                self.is_passive = False
                self.is_epsv = False
                self.after_mode_command()
                # not checking for lust retr or stor here because menu repl takes care of that
        except Exception as e:
            logger.log_err(str(e))

    '''
    PASV command
    lets the client turn on the passive mode and turn off all the other modes
    '''
    def pasv_command(self):
        try:
            logger.log_attempt('PASV')
            if self.logged_in_check():
                self.data_receiving_socket = FtpServer.create_new_socket()
                self.data_receiving_socket.bind((socket.gethostbyname(socket.gethostname()), 0))
                self.data_receiving_socket.listen(1)
                logger.log('Data Receiving Socket created.')
                port_1 = int((self.data_receiving_socket.getsockname()[1]) / 256)
                port_2 = int((self.data_receiving_socket.getsockname()[1]) - (port_1 * 256))
                passive_response = '227 Entering Passive Mode (' + socket.gethostbyname(socket.gethostname()).replace('.', ',') + ',' + str(port_1) + ',' + str(port_2) + ').\n '
                self.c.send(FtpServer.str_to_bytes(passive_response))
                logger.log_response(passive_response)
                self.is_passive = True
                self.is_eprt = False
                self.is_port = False
                self.is_epsv = False
                self.after_mode_command()
                # not checking for lust retr or stor here because menu repl takes care of that
        except Exception as e:
            logger.log_err(str(e))

    '''
    EPSV command
    basically the same as PASV but with original IP and full port
    '''
    def epsv_command(self):
        try:
            logger.log_attempt('EPSV')
            if self.logged_in_check():
                self.data_receiving_socket = FtpServer.create_new_socket()
                self.data_receiving_socket.bind((socket.gethostbyname(socket.gethostname()), 0))
                self.data_receiving_socket.listen(1)
                logger.log('Data Receiving Socket created.')
                port = self.data_receiving_socket.getsockname()[1]
                epsv_response = '229 Entering Extended Passive Mode. (|||' + str(port) + '|)'
                self.c.send(FtpServer.str_to_bytes(epsv_response + '\n'))
                logger.log_response(epsv_response)
                self.is_epsv = True
                self.is_passive = False
                self.is_eprt = False
                self.is_port = False
                self.after_mode_command()
                # not checking for lust retr or stor here because menu repl takes care of that
        except Exception as e:
            logger.log_err(str(e))

    '''
    LIST command
    returns the list of all the files in the working directory of the server
    '''
    def list_command(self):
        try:
            logger.log_attempt('LIST')
            if self.logged_in_check() and self.mode_check():
                if os.name == 'nt':
                    ls_output = subprocess.check_output(['dir'], shell=True)# + FtpServer.str_to_bytes('\n')
                else:
                    ls_output = subprocess.check_output(['ls', '-l'], shell=True)# + FtpServer.str_to_bytes('\n')
                self.c.send(FtpServer.str_to_bytes('150 Directory Listing.\n'))
                logger.log_response('150 Directory Listing')
                if self.is_port:
                    self.data_receiving_socket.send(ls_output)
                elif self.is_passive:
                    conn, host = self.data_receiving_socket.accept()
                    conn.send(ls_output)
                elif self.is_eprt:
                    self.data_receiving_socket.send(ls_output)
                elif self.is_epsv:
                    conn, host = self.data_receiving_socket.accept()
                    conn.send(ls_output)
                logger.log(str(ls_output))
                self.c.send(FtpServer.str_to_bytes('226 List Response OK.\n'))
                self.is_port = False
                self.is_passive = False
                self.is_eprt = False
                self.is_epsv = False
        except Exception as e:
            logger.log_err(str(e))

    '''
    RETR command
    lets the client retrieve a file from the working directory
    '''
    def retr_command(self):
        try:
            logger.log_attempt('RETR')
            if self.logged_in_check() and self.mode_check():
                user_file_name = self.client_input[5:]
                if not os.path.exists(user_file_name):
                    self.c.send(FtpServer.str_to_bytes('550 Failed to open file.\n'))
                    logger.log_response('550 Failed to open file.')
                else:
                    file = open(user_file_name, 'r')
                    file_data = file.read()
                    self.c.send(FtpServer.str_to_bytes('150 Sending file ' + user_file_name + '\n'))
                    logger.log('150 Sending file ' + user_file_name)
                    if self.is_port or self.is_eprt:
                        self.data_receiving_socket.send(FtpServer.str_to_bytes(file_data))
                    elif self.is_passive or self.is_epsv:
                        conn, host = self.data_receiving_socket.accept()
                        conn.send(FtpServer.str_to_bytes(file_data + '\n'))
                    self.c.send(FtpServer.str_to_bytes('226 Transfer complete.\n'))
                    logger.log_response('226 Transfer complete.')
                    self.is_port = False
                    self.is_passive = False
                    self.is_eprt = False
                    self.is_epsv = False
        except Exception as e:
            logger.log_err(str(e))

    '''
    STOR command
    lets the client store a file in the current working directory of the server
    '''
    def stor_command(self):
        try:
            logger.log_attempt('STOR')
            if self.logged_in_check() and self.mode_check():
                user_file_name = self.client_input[5:]
                file = open(user_file_name, 'w')
                self.c.send(FtpServer.str_to_bytes('150 OK to store.\n'))
                logger.log_response('150 OK to store.')
                if self.is_port or self.is_eprt:
                    while True:
                        file_data = self.data_receiving_socket.recv(1024).strip()
                        if not file_data:
                            break
                        file.write(file_data)
                elif self.is_passive or self.is_epsv:
                    conn, host = self.data_receiving_socket.accept()
                    while True:
                        file_data = conn.recv(1024).strip()
                        if not file_data:
                            break
                        file.write(file_data)
                self.c.send(FtpServer.str_to_bytes('226 Transfer complete.\n'))
                logger.log_response('226 Transfer complete.')
        except Exception as e:
            logger.log_err(str(e))

    '''
    CDUP command
    changes working directory to immediate parent directory
    '''
    def cdup_command(self):
        try:
            logger.log_attempt('CDUP')
            if self.logged_in_check():
                os.chdir('../')
                self.c.send(FtpServer.str_to_bytes('250 Directory changed.\n'))
                logger.log_response('250 Directory changed.')
        except Exception as e:
            logger.log_err(str(e))

    def type_I_command(self):
        try:
            if not (self.logged_in_check() and self.mode_check()):
                self.c.send(FtpServer.str_to_bytes('200 Switching to Binary Mode.\n'))
                logger.log_response('200 switching to Binary Mode.')
        except Exception as e:
            logger.log_err(str(e))

    def menu_repl(self):
        try:
            while True:
                self.client_input = str(self.c.recv(1024).strip())[2:-1]
                if 'PWD' == self.client_input:
                    self.pwd_command()
                elif 'CWD' in self.client_input:
                    self.cwd_command()
                elif 'QUIT' == self.client_input:
                    self.quit_command()
                elif 'USER' in self.client_input:
                    self.user_command()
                elif 'PORT' in self.client_input:
                    self.port_command()
                elif 'EPRT' in self.client_input:
                    self.eprt_command()
                elif 'PASV' in self.client_input:
                    self.pasv_command()
                elif 'EPSV' in self.client_input:
                    self.epsv_command()
                elif 'LIST' == self.client_input:
                    self.list_command()
                elif 'RETR' in self.client_input:
                    self.retr_command()
                elif 'STOR' in self.client_input:
                    self.stor_command()
                elif 'CDUP' == self.client_input:
                    self.cdup_command()
                elif 'TYPE' in self.client_input:
                    self.type_I_command()
                else:
                    continue
        except Exception as e:
            logger.log_err(str(e))
            print(str(e))

def main():
    if len(sys.argv) != 3:
        print('Invalid number of arguments.')
        sys.exit(0)

    log_file_name = sys.argv[1]
    port = int(sys.argv[2])
    global logger
    logger = Logger(log_file_name)
    ftpServer = FtpServer(port)
    ftpServer.initialise()

if __name__ == '__main__':
    main()
