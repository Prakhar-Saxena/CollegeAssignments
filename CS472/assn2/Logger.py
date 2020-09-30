#!/usr/bin/env python3

import sys
import datetime

class Logger:
    f = None

    @staticmethod
    def log_file_init(file_name):
        try:
            Logger.f = open(file_name, "a")
        except (IOError, Exception) as err:
            print("Logging onto file exception.")
            sys.exit(0)

    @staticmethod
    def log(msg):
        Logger.f.write(str(datetime.datetime.now()) + "\t" + msg + "\n")
