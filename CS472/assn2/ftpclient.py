#!/usr/bin/env python3

import socket
import sys
import datetime
from Logger import Logger


class FtpClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.commands = ['USER', 'PASS', 'CWD', 'QUIT', 'PASV', 'EPSV', 'PORT', 'EPRT', 'RETR', 'STOR', 'PWD', 'SYST',
                         'LIST', 'HELP']
        self.s = None

    def connect_server(self):
        try:
            Logger.log('Attempting server connection with sockets.')
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            Logger.log('Socket created.')
            self.s.connect((self.ip, self.port))
            Logger.log('Socket Successfully connected to ' + str(self.ip) + ' at port ' + str(self.ip))
        except socket.error as e:
            Logger.log_err('Socket Error:' + str(e))

    def user_command(self):
        return

    def pass_command(self):
        return

    def cwd_command(self):
        return

    def quit_command(self):
        return

    def pasv_command(self):
        return

    def epsv_command(self):
        return

    def port_command(self):
        return

    def eprt_command(self):
        return

    def retr_command(self):
        return

    def stor_command(self):
        return

    def pwd_command(self):
        return

    def syst_command(self):
        return

    def list_command(self):
        return

    def help_command(self):
        return

    def menu_repl(self):
        Logger.log('Initialising menu REPL.')
        print('Hello there!\n You\'re in the menu REPL now.')
        print('-' * 25)
        while True:
            print('List of available commands ' + '(' + str(len(self.commands)) + ' commands):')
            for command in self.commands:
                print(command)
            print('-' * 25)
            user_choice = input('Enter your command: ').upper()
            if user_choice == self.commands[0]:  # USER
                self.user_command()
            elif user_choice == self.commands[1]:  # PASS
                self.pass_command()
            elif user_choice == self.commands[2]:  # CWD
                self.cwd_command()
            elif user_choice == self.commands[3]:  # QUIT
                self.quit_command()
            elif user_choice == self.commands[4]:  # PASV
                self.pasv_command()
            elif user_choice == self.commands[5]:  # EPSV
                self.epsv_command()
            elif user_choice == self.commands[6]:  # PORT
                self.port_command()
            elif user_choice == self.commands[7]:  # EPRT
                self.eprt_command()
            elif user_choice == self.commands[8]:  # RETR
                self.retr_command()
            elif user_choice == self.commands[9]:  # STOR
                self.stor_command()
            elif user_choice == self.commands[10]:  # PWD
                self.pwd_command()
            elif user_choice == self.commands[11]:  # SYST
                self.syst_command()
            elif user_choice == self.commands[12]:  # LIST
                self.list_command()
            elif user_choice == self.commands[13]:  # HELP
                self.help_command()
            else:
                print('Invalid command entered. Try again.\n')
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

    ftpClient = FtpClient(ip, port)

    Logger.log('-' * 25 + 'STOPS HERE' + '-' * 25)


if __name__ == '__main__':
    main()
