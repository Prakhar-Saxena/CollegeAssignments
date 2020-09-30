#!/usr/bin/env python3

import socket
import sys
import datetime
from Logger import Logger

def main():
    Logger.log_file_init('log_file')
    Logger.log('Hello there')

if __name__ == '__main__':
    main()