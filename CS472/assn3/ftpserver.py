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
