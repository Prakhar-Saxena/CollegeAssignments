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
        logger.log_response(response)
        return response

    @staticmethod
    def str_to_bytes(string):
        return bytes(string, 'utf-8')

    @staticmethod
    def create_receiving_socket():
        try:
            socket_rec = FtpClient.create_new_socket()
            socket_rec.bind((socket.gethostbyname(), 0))
            socket_rec.listen(1)
            logger.log('New Socket created, for data receiving.')
            return socket_rec
        except socket.error as e:
            logger.log_socket_error(str(e))
        except Exception as e:
            logger.log_err(str(e))

    @staticmethod
    def create_new_socket():
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
        except Exception as e:
            logger.log_err(str(e))

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
        except Exception as e:
            logger.log_err(str(e))

    def pass_command(self):
        try:
            logger.log_attempt('PASS')
            password = input('Enter password: ')
            self.s.send(FtpClient.str_to_bytes('PASS ' + password + '\n'))
            logger.log('Sent: PASS ' + password)
            response = self.response()
        except socket.error as e:
            logger.log_socket_error(str(e))
        except Exception as e:
            logger.log_err(str(e))

    def cwd_command(self):
        try:
            logger.log_attempt('CWD')
            cd_input = input('Enter directory: ')
            self.s.send(FtpClient.str_to_bytes('CWD ' + cd_input + '\n'))
            logger.log('Sent: CWD ' + cd_input)
            response = self.response()
            self.pwd_command()
        except Exception as e:
            logger.log_err('Error: ' + str(e))
        return

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
        except Exception as e:
            logger.log_err(str(e))

    def pasv_command(self):
        try:
            logger.log_attempt('PASV')
            if self.is_passive:
                self.is_passive = False
            elif not self.is_passive:
                self.is_passive = True
            else:
                print('This should be impossible.')
                logger.log('This should be impossible.')
        except Exception as e:
            logger.log_err(str(e))

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
        except Exception as e:
            logger.log_err(str(e))

    def port_command(self):
        try:
            logger.log_attempt('PORT')
            if self.is_port:
                self.is_port = False
            elif not self.is_port:
                self.is_port = True
            else:
                print('This should be impossible.')
                logger.log('This should be impossible.')
        except Exception as e:
            logger.log_err(str(e))

    def eprt_command(self):
        try:
            socket_rec = FtpClient.create_new_socket()
            socket_rec.bind(socket.gethostbyname(socket.gethostbyname(socket.gethostname()), 0))
            socket_rec.listen(1)
            logger.log('New data receiving socket created.')
            port = str(socket_rec.getsockname()[1])
            ip = str(socket.gethostbyname(socket.gethostname()))
            self.s.send('EPRT | 1 | ' + ip + ' | ' + port + '\n')
            logger.log('Sent: EPRT')
            response = self.response()
        except socket.error as e:
            logger.log_socket_error(str(e))
        except Exception as e:
            logger.log_err(str(e))

    def retr_command(self):
        return

    def stor_command(self):
        try:
            logger.log_attempt('STOR')
            socket_rec = FtpClient.create_new_socket()
            socket_rec.bind((socket.gethostbyname(socket.gethostname()), 0))
            socket_rec.listen(1)
            logger.log('New data receiving socket created.')

            if self.is_port and not self.is_passive:
                port_1 = int((socket_rec.getsockname()[1]) / 256)
                port_2 = int((socket_rec.getsockname()[1]) - (port_1 * 256))
                port_command = 'PORT ' + socket.gethostbyname(socket.gethostname()).replace('.', ',') + ',' + str(port_1) + ',' + str(port_2) +'\n'
                self.s.send(FtpClient.str_to_bytes(port_command))
                logger.log('Sent: ' + port_command)
                response = self.response()

            elif self.is_passive:
                socket_rec.close()
                print('The client is in passive mode.')
                self.s.send('PASV \n')
                logger.log('Sent: PASV')
                response = self.response()
                address = response[27:-4].split(',')
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
                logger.log()

            user_file_name = input('Enter file name to be stored:')
            self.s.send('SEND ' + user_file_name + '\n')
            logger.log('Sent: STOR' + user_file_name)
            user_file = open(user_file_name, 'r')
            file_data = FtpClient.str_to_bytes(user_file.read())
            response = self.response()
            conn, host = socket_rec.accept()
            conn.send(file_data)
            user_file.close()
        except socket.error as e:
            logger.log_socket_error(str(e))
        except Exception as e:
            logger.log_err(str(e))

    def pwd_command(self):
        try:
            logger.log_attempt('PWD')
            self.s.send(FtpClient.str_to_bytes('PWD \n'))
            logger.log('Sent: PWD')
            response = self.response()
        except socket.error as e:
            logger.log_socket_error(str(e))
        except Exception as e:
            logger.log_err(str(e))

    def syst_command(self):
        return

    def list_command(self):
        return

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

    logger.log('-' * 25 + 'STOPS HERE' + '-' * 25)


if __name__ == '__main__':
    main()
