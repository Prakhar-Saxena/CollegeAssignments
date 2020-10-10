#!/usr/bin/env python3

import socket
import sys
from Logger import Logger


class FtpClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.commands = ['USER', 'PASS', 'PWD', 'CWD', 'HELP',
                         'PASV', 'EPSV', 'PORT', 'EPRT', 'RETR',
                         'STOR', 'SYST', 'LIST', 'QUIT']
        self.s = None

        self.is_passive = False
        self.is_port = False

    def initialise(self):
        self.connect_server()
        self.user_command()  # includes PASS command
        self.menu_repl()

    def response(self):
        response = str(self.s.recv(1024)).strip()
        print(response)
        Logger.log_response(response)
        return response

    @staticmethod
    def str_to_bytes(string):
        return bytes(string, 'utf-8')

    def connect_server(self):
        try:
            Logger.log_attempt('server connection with sockets.')
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            Logger.log('Socket created.')
            self.s.connect((self.ip, int(self.port)))
            response = self.response()
            Logger.log('Socket Successfully connected to ' + str(self.ip) + ' at port ' + str(self.ip))
        except socket.error as e:
            Logger.log_socket_error(str(e))

    def user_command(self):
        try:
            Logger.log_attempt('USER')
            user_name = input('Enter username: ')
            self.s.send(FtpClient.str_to_bytes('USER ' + user_name + '\n'))
            Logger.log('Sent: USER - ' + user_name)
            response = self.response()
            self.pass_command()
        except socket.error as e:
            Logger.log_socket_error(str(e))

    def pass_command(self):
        try:
            Logger.log_attempt('PASS')
            password = input('Enter password: ')
            self.s.send(FtpClient.str_to_bytes('PASS ' + password + '\n'))
            Logger.log('Sent: PASS ' + password)
            response = self.response()
        except socket.error as e:
            Logger.log_socket_error(str(e))

    def cwd_command(self):
        try:
            Logger.log_attempt('CWD')
            cd_input = input('Enter directory: ')
            self.s.send(FtpClient.str_to_bytes('CWD ' + cd_input + '\n'))
            Logger.log('Sent: CWD ' + cd_input)
            response = self.response()
            self.pwd_command()
        except Exception as e:
            Logger.log_err('Error: ' + str(e))
        return

    def quit_command(self):
        try:
            Logger.log_attempt('QUIT')
            self.s.send(FtpClient.str_to_bytes('QUIT \n'))
            Logger.log('Sent: QUIT')
            response = self.response()
            print('Quiting.')
            Logger.log('Quiting.')
            self.s.close()
            sys.exit(0)
        except socket.error as e:
            Logger.log_socket_error(str(e))

    def pasv_command(self):
        try:
            Logger.log_attempt('PASV')
            if self.is_passive:
                self.is_passive = False
                self.s.send(FtpClient.str_to_bytes('PASV n \n'))
            elif not self.is_passive:
                self.is_passive = True
                self.s.send(FtpClient.str_to_bytes('PASV \n'))
            else:
                print('This should be impossible.')
                Logger.log('This should be impossible.')
            response = self.response()
        except socket.error as e:
            Logger.log_socket_error(str(e))

    def epsv_command(self):
        return

    def port_command(self):
        try:
            Logger.log_attempt('PORT')
            if self.is_port:
                self.is_port = False
                self.s.send(FtpClient.str_to_bytes('PORT \n'))
            elif not self.is_port:
                self.is_port = True
                self.s.send(FtpClient.str_to_bytes('PORT \n'))
            else:
                print('This should be impossible.')
                Logger.log('This should be impossible.')
            response = self.response()
        except socket.error as e:
            Logger.log_socket_error(str(e))

    def eprt_command(self):
        return

    def retr_command(self):
        return

    def stor_command(self):
        return

    def pwd_command(self):
        try:
            Logger.log_attempt('PWD')
            self.s.send(FtpClient.str_to_bytes('PWD \n'))
            Logger.log('Sent: PWD')
            response = self.response()
        except socket.error as e:
            Logger.log_socket_error(str(e))

    def syst_command(self):
        return

    def list_command(self):
        return

    def help_command(self):
        try:
            Logger.log_attempt('HELP')
            self.s.send(FtpClient.str_to_bytes('HELP \n'))
            Logger.log('Sent: HELP')
            response = self.response()
        except socket.error as e:
            Logger.log_socket_error(str(e))

    '''
    REPL: Read-Evaluate-Print-Loop
    '''
    def menu_repl(self):
        Logger.log('Initialising menu REPL.')
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
                Logger.log('Invalid command entered: ' + user_choice)
                print('-' * 25)


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

    Logger.log_file_init(log_file_name)
    Logger.log('-' * 25 + 'STARTS HERE' + '-' * 25)
    Logger.log('New ftp client intialised.')
    Logger.log('IP: ' + ip)
    Logger.log('Port: ' + port)

    ftp_client = FtpClient(ip, port)
    ftp_client.initialise()

    Logger.log('-' * 25 + 'STOPS HERE' + '-' * 25)


if __name__ == '__main__':
    main()
