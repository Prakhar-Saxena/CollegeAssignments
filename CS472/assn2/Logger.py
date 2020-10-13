#!/usr/bin/env python3

import sys
import datetime

class Logger:
    def __init__(self, log_file_name):
        try:
            self.log_file_name = log_file_name
            self.f = open(log_file_name, 'a')
        except Exception as e:
            print(str(e))
            sys.exit(0)

    def close_file(self):
        try:
            self.f.close()
        except Exception as e:
            print(str(e))
            sys.exit(0)

    def log(self, msg):
        self.f.write(str(datetime.datetime.now()) + '\t' + msg + '\n')

    def log_err(self, err_msg):
        self.f.write(str(datetime.datetime.now()) + '\t' + 'X'*25 + ' ERROR ' + 'X'*25 + '\n\t\t\t\t\t' + err_msg + '\n')
        # print('Something didn\'t work and now the whole thing is blown.')

    def log_socket_error(self, error_msg):  # created this because Socket error is the most expected/caught error.
        self.log_err('Socket Error: ' + error_msg)

    def log_response(self, response):
        self.log('Response Received: ' + response)

    def log_attempt(self, msg):
        self.log('Attempting ' + msg)
