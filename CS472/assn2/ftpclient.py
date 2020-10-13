#!/usr/bin/env python3
#
# CS 472 - Homework # 2
# Prakhar Saxena
# ftpclient.py
#
# This file contains implementation of an FTP client that can login, list directory info, and store and retrieve info
# from a server hosting the FTP service.
#

import socket
import sys
from Logger import Logger

class FtpClient:
    '''
    initialise the client with ip, port, commands and other useful attributes
    '''
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.commands = ['USER', 'PASS', 'PWD', 'CWD', 'HELP',
                         'PASV', 'EPSV', 'PORT', 'EPRT', 'RETR',
                         'STOR', 'SYST', 'LIST', 'QUIT']
        self.s = None  # main socket

        self.is_passive = False  # passive mode attribute
        self.is_port = False  # port mode attribute

    '''
    initialise the client with connection, user-password and the menu-REPL
    '''
    def initialise(self):
        self.connect_server()
        self.user_command()  # includes PASS command
        self.menu_repl()

    '''
    created this method because we need to record the response from the FTP server quite frequently
    '''
    def response(self):
        response = str(self.s.recv(1024)).strip()
        print(response)
        logger.log_response(response)
        return response

    '''
    converts string to bytes
    needed this method because sockets require bytes and not strings.
    '''
    @staticmethod
    def str_to_bytes(string):
        return bytes(string, 'utf-8')

    '''
    creates a socket specifically used for receiving data.
    needed this method because a lot of commands required a frequent creation of a socket like this
    '''
    @staticmethod
    def create_receiving_socket():
        try:
            socket_rec = FtpClient.create_new_socket()
            socket_rec.bind((socket.gethostbyname(socket.gethostname()), 0))
            socket_rec.listen(1)
            logger.log('New Socket created, for data receiving.')
            return socket_rec
        except socket.error as e:
            logger.log_socket_error(str(e))
            return
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    creates a new socket.
    '''
    @staticmethod
    def create_new_socket():
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    '''
    connects to the FTP server
    takes no arguments, because all the information like the ip and port is already available to the instance
    '''
    def connect_server(self):
        try:
            logger.log_attempt('server connection with sockets.')
            self.s = FtpClient.create_new_socket()
            logger.log('Socket created.')
            self.s.connect((self.ip, int(self.port)))
            response = self.response()
            logger.log('Socket Successfully connected to ' + str(self.ip) + ' at port ' + str(self.ip))
        except socket.error as e:
            logger.log_socket_error(str(e))
            return
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    USER command
    lets the user type in the username for the FTP server
    also calls the PASS Command
    '''
    def user_command(self):
        try:
            logger.log_attempt('USER')
            user_name = input('Enter username: ')
            self.s.send(FtpClient.str_to_bytes('USER ' + user_name + '\n'))
            logger.log('Sent: USER - ' + user_name)
            response = self.response()
            self.pass_command()
        except socket.error as e:
            logger.log_socket_error(str(e))
            return
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    PASS command
    lets teh user type in the password for the username previously entered onto the FTP server
    '''
    def pass_command(self):
        try:
            logger.log_attempt('PASS')
            password = input('Enter password: ')
            self.s.send(FtpClient.str_to_bytes('PASS ' + password + '\n'))
            logger.log('Sent: PASS ' + password)
            response = self.response()
        except socket.error as e:
            logger.log_socket_error(str(e))
            return
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    CWD command
    Change working directory
    lets user change the working directory the client is accessing
    equivalent to 'cd' in Windows or Unix console/terminal
    calls the PWD command
    '''
    def cwd_command(self):
        try:
            logger.log_attempt('CWD')
            cd_input = input('Enter directory: ')
            self.s.send(FtpClient.str_to_bytes('CWD ' + cd_input + '\n'))
            logger.log('Sent: CWD ' + cd_input)
            response = self.response()
            self.pwd_command()  # calling the pwd, just to check what the directory is after the change
        except Exception as e:
            logger.log_err('Error: ' + str(e))
            return

    '''
    QUIT command
    lets the user quit the menu-REPL and the client application.
    '''
    def quit_command(self):
        try:
            logger.log_attempt('QUIT')
            self.s.send(FtpClient.str_to_bytes('QUIT \n'))
            logger.log('Sent: QUIT')
            response = self.response()
            print('Quiting.')
            logger.log('Quiting.')
            self.s.close()
            logger.close_file()
            sys.exit(0)
        except socket.error as e:
            logger.log_socket_error(str(e))
            return
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    PASV command
    lets the user change turn the client into passive mode.
    '''
    def pasv_command(self):
        try:
            logger.log_attempt('PASV')
            if self.is_passive:
                self.is_passive = False
                print('The client is not in passive mode now.')
                logger.log('The client is not in passive mode now.')
            elif not self.is_passive:
                self.is_passive = True
                print('The client is in passive mode now.')
                logger.log('The client is in passive mode now.')
            else:
                print('This should be impossible.')
                logger.log('This should be impossible.')
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    EPSV command
    basically the same as PASV but with original IP and full port
    '''
    def epsv_command(self):
        try:
            logger.log_attempt('EPSV')
            self.s.send(FtpClient.str_to_bytes('EPSV \n'))
            response = self.response()
            port = response.split('|')[3]
            socket_rec = FtpClient.create_receiving_socket()
            socket_rec.connect((self.ip, port))
            socket_rec.close()
        except socket.error as e:
            logger.log_socket_error(str(e))
            return
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    PORT command
    lets the user change turn the client into port mode.
    '''
    def port_command(self):
        try:
            logger.log_attempt('PORT')
            if self.is_port:
                self.is_port = False
                print('The client is not in port mode now.')
                logger.log('The client is not in port mode now.')
            elif not self.is_port:
                self.is_port = True
                print('The client is in port mode now.')
                logger.log('The client is in port mode now.')
            else:
                print('This should be impossible.')
                logger.log('This should be impossible.')
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    EPRT command
    basically the same as PASV but with different format
    '''
    def eprt_command(self):
        try:
            logger.log_attempt('EPRT')
            socket_rec = FtpClient.create_receiving_socket()
            logger.log('New data receiving socket created.')
            port = str(socket_rec.getsockname()[1])
            ip = str(socket.gethostbyname(socket.gethostname()))
            eprt_command = 'EPRT |1|' + ip + '|' + port  # + '|'  # RFC is wrong.
            self.s.send(FtpClient.str_to_bytes(eprt_command + ' \n'))
            logger.log('Sent: ' + eprt_command)
            response = self.response()
        except socket.error as e:
            logger.log_socket_error(str(e))
            return
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    RETR command
    to retrieve a file from the FTP server
    '''
    def retr_command(self):
        try:
            logger.log_attempt('RETR')
            socket_rec = FtpClient.create_receiving_socket()
            logger.log('New data receiving socket created.')
            if self.is_port and not self.is_passive:  # passive mode takes priority over port mode
                port_1 = int((socket_rec.getsockname()[1]) / 256)
                port_2 = int((socket_rec.getsockname()[1]) - (port_1 * 256))
                port_command = 'PORT ' + socket.gethostbyname(socket.gethostname()).replace('.', ',') + ',' + str(port_1) + ',' + str(port_2)
                self.s.send(FtpClient.str_to_bytes(port_command + '\n'))
                logger.log('Sent: ' + port_command)
                response = self.response()
            elif self.is_passive:
                print('The client is in passive mode.')
                self.s.send(FtpClient.str_to_bytes('PASV \n'))
                logger.log('Sent: PASV')
                response = self.response()
                address = response[29:-7].split(',')
                ip = address[0] + '.' + address[1] + '.' + address[2] + '.' + address[3]
                port_1 = int(address[4])
                port_2 = int(address[5])
                port = int((port_1 * 256) + port_2)
                socket_rec = FtpClient.create_new_socket()
                logger.log('New data receiving socket created.')
                socket_rec.connect((ip, port))
            else:
                socket_rec.close()
                print('Not in Port ot Passive mode.')
                logger.log('User attempted STOR whilst not being in Port or Passive mode.')
                return
            user_file_name = input('Enter file name to be retrieved: ')
            self.s.send(FtpClient.str_to_bytes('RETR ' + user_file_name + '\n'))
            response = self.response()
            user_file = open(user_file_name, 'r')
            file_data = FtpClient.str_to_bytes(user_file.read())
            response = self.response()
            conn, host = socket_rec.accept()
            while True:
                list_response = conn.recv(1024)
                if not list_response:
                    break
                print(list_response)
                logger.log('Received: ' + str(list_response))
            response = self.response()
        except socket.error as e:
            logger.log_socket_error(str(e))
            return
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    STOR command
    to store file onto the FTP server
    '''
    def stor_command(self):
        try:
            logger.log_attempt('STOR')
            socket_rec = FtpClient.create_receiving_socket()
            logger.log('New data receiving socket created.')
            if self.is_port and not self.is_passive:  # passive mode takes priority over port mode
                port_1 = int((socket_rec.getsockname()[1]) / 256)
                port_2 = int((socket_rec.getsockname()[1]) - (port_1 * 256))
                port_command = 'PORT ' + socket.gethostbyname(socket.gethostname()).replace('.', ',') + ',' + str(port_1) + ',' + str(port_2)
                self.s.send(FtpClient.str_to_bytes(port_command + ' \n'))
                logger.log('Sent: ' + port_command)
                response = self.response()
                user_file_name = input('Enter file name to be stored:')
                self.s.send(FtpClient.str_to_bytes('STOR ' + user_file_name + '\n'))
                logger.log('Sent: STOR' + user_file_name)
                user_file = open(user_file_name, 'r')
                file_data = FtpClient.str_to_bytes(user_file.read())
                response = self.response()
                conn, host = socket_rec.accept()
                conn.send(file_data)
                user_file.close()
            elif self.is_passive:
                print('The client is in passive mode.')
                self.s.send(FtpClient.str_to_bytes('PASV \n'))
                logger.log('Sent: PASV')
                response = self.response()
                address = response[29:-7].split(',')
                ip = address[0] + '.' + address[1] + '.' + address[2] + '.' + address[3]
                port_1 = int(address[4])
                port_2 = int(address[5])
                port = int((port_1 * 256) + port_2)
                socket_rec = FtpClient.create_new_socket()
                logger.log('New data receiving socket created.')
                socket_rec.connect((ip, port))
                user_file_name = input('Enter file name to be stored:')
                self.s.send(FtpClient.str_to_bytes('STOR ' + user_file_name + '\n'))
                logger.log('Sent: STOR' + user_file_name)
                user_file = open(user_file_name, 'r')
                file_data = FtpClient.str_to_bytes(user_file.read())
                response = self.response()
                # conn, host = socket_rec.accept()
                socket_rec.send(file_data)
                user_file.close()
            else:
                socket_rec.close()
                print('Not in Port ot Passive mode.')
                logger.log('User attempted STOR whilst not being in Port or Passive mode.')
                return
            socket_rec.close()
        except socket.error as e:
            logger.log_socket_error(str(e))
            return
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    PWD command
    prints the working directory
    same as the pwd command on the Unix terminal
    '''
    def pwd_command(self):
        try:
            logger.log_attempt('PWD')
            self.s.send(FtpClient.str_to_bytes('PWD \n'))
            logger.log('Sent: PWD')
            response = self.response()
        except socket.error as e:
            logger.log_socket_error(str(e))
            return
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    SYST command
    '''
    def syst_command(self):
        try:
            logger.log_attempt('SYST')
            self.s.send(FtpClient.str_to_bytes('SYST \n'))
            logger.log('Sent: SYST')
            response = self.response()
        except socket.error as e:
            logger.log_socket_error(str(e))
            return
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    LIST command
    
    '''
    def list_command(self):
        try:
            logger.log_attempt('LIST')
            socket_rec = FtpClient.create_receiving_socket()
            if self.is_port and not self.is_passive:
                port_1 = int((socket_rec.getsockname()[1]) / 256)
                port_2 = int((socket_rec.getsockname()[1]) - (port_1 * 256))
                port_command = 'PORT ' + socket.gethostbyname(socket.gethostname()).replace('.', ',') + ',' + str(port_1) + ',' + str(port_2)
                self.s.send(FtpClient.str_to_bytes(port_command + ' \n'))
                logger.log('Sent: ' + port_command)
                response = self.response()
                self.s.send(FtpClient.str_to_bytes('LIST \n'))
                response = self.response()
                conn, host = socket_rec.accept()
                while True:
                    list_response = conn.recv(1024)
                    if not list_response:
                        break
                    print(list_response)
                    logger.log('Received: ' + str(list_response))
                response = self.response()
                self.response()
            elif self.is_passive:
                print('The client is in passive mode.')
                self.s.send(FtpClient.str_to_bytes('PASV \n'))
                response = self.response()
                address = response[29:-7].split(',')
                ip = address[0] + '.' + address[1] + '.' + address[2] + '.' + address[3]
                port_1 = int(address[4])
                port_2 = int(address[5])
                port = int((port_1 * 256) + port_2)
                socket_rec = FtpClient.create_new_socket()
                logger.log('New data receiving socket created.')
                socket_rec.connect((ip, port))
                self.s.send(FtpClient.str_to_bytes('LIST \n'))
                response = self.response()
                while True:
                    list_response = socket_rec.recv(1024)
                    if not list_response:
                        break
                    print(list_response)
                    logger.log('Received: ' + str(list_response))
                response = self.response()
            else:
                socket_rec.close()
                print('Not in Port ot Passive mode.')
                logger.log('User attempted STOR whilst not being in Port or Passive mode.')
                return


        except socket.error as e:
            logger.log_socket_error(str(e))
            return
        except Exception as e:
            logger.log_err(str(e))
            return

    '''
    HELP command
    I don't need to implement this because my menu itself is a REPL.
    '''
    def help_command(self):
        try:
            logger.log_attempt('HELP')
        except socket.error as e:
            logger.log_socket_error(str(e))

    '''
    REPL: Read-Evaluate-Print-Loop
    '''
    def menu_repl(self):
        logger.log('Initialising menu REPL.')
        print('Hello there!\n You\'re in the menu REPL now.')
        print('-' * 25)
        while True:
            print('List of available commands ' + '(' + str(len(self.commands)) + ' commands):')
            cnt = 1
            for command in self.commands:
                if (cnt % 5) == 0:
                    print(str(cnt) + ') ' + command)
                else:
                    print(str(cnt) + ') ' + command + '\t\t\t', end='')
                cnt = cnt + 1
            print()
            print('-' * 25)
            user_choice = input('Enter your command: ').upper()
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
            else:
                print('Invalid command entered. Try again.\n')
                logger.log('Invalid command entered: ' + user_choice)
                print('-' * 25)

'''
main function.
'''
def main():
    ip = ''
    log_file_name = ''
    port = ''
    num_args = len(sys.argv)

    if num_args not in (3, 4):
        print('Invalid number of arguments.')
        sys.exit(0)

    if num_args == 4:
        port = sys.argv[3]
    else:
        port = '21'

    ip = sys.argv[1]
    log_file_name = sys.argv[2]

    global logger
    logger = Logger(log_file_name)

    logger.log('-' * 25 + 'STARTS HERE' + '-' * 25)
    logger.log('New ftp client intialised.')
    logger.log('IP: ' + ip)
    logger.log('Port: ' + port)

    ftp_client = FtpClient(ip, port)
    ftp_client.initialise()

    logger.log('-' * 25 + 'STOPS HERE' + '-' * 25 + '\n')

'''
Python main function name ceremony
'''
if __name__ == '__main__':
    main()
