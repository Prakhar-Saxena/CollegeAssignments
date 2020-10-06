#!/usr/bin/env python3

import socket
import sys
import datetime
from Logger import Logger

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
    Logger.log('-' * 25 + 'STOPS HERE' + '-' * 25)



if __name__ == '__main__':
    main()