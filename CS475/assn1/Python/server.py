#!/usr/bin/env python3

import sys

from H import H
from misc import fileWriterList, fileWriterNum, fileReader

filename = 'server_password'

pass_arg = int(sys.argv[1])

password = int(fileReader(filename))

if password == H(pass_arg):
    print(True)
    fileWriterNum(pass_arg, filename)
else:
    print(False)
