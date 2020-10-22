#!/usr/bin/env python3
#
# CS 472 - Homework #3
# Prakhar Saxena
# Logger.py
#
# This file contains implementation of a logging tool, that is used by the FTP server in the same directory.
# This is the same logger used for FTP client.
#

import sys
import datetime

'''
Logger class
- used for logging.
'''
class Logger:
    '''
    initialise with a log file created
    '''
    def __init__(self, log_file_name):
        try:
            self.log_file_name = log_file_name
            self.f = open(log_file_name, 'a')
        except Exception as e:
            print(str(e))
            sys.exit(0)

    '''
    close the log file
    '''
    def close_file(self):
        try:
            self.f.close()
        except Exception as e:
            print(str(e))
            sys.exit(0)

    '''
    log messages
    '''
    def log(self, msg):
        self.f.write(str(datetime.datetime.now()) + '\t' + msg + '\n')

    '''
    log error messages
    '''
    def log_err(self, err_msg):
        self.f.write(str(datetime.datetime.now()) + '\t' + 'X'*25 + ' ERROR ' + 'X'*25 + '\n\t\t\t\t\t' + err_msg + '\n')
        # print('Something didn\'t work and now the whole thing is blown.')

    '''
    log socket error messages
    '''
    def log_socket_error(self, error_msg):  # created this because Socket error is the most expected/caught error.
        self.log_err('Socket Error: ' + error_msg)

    '''
    log response messages
    '''
    def log_response(self, response):
        self.log('Response Received: ' + response)

    '''
    log attempt messages
    '''
    def log_attempt(self, msg):
        self.log('Attempting ' + msg)
