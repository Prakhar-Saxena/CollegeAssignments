#!/usr/bin/env python3

import sys

from H import H
from misc import fileWriterList, fileWriterNum, fileReader

pass_arg = int(sys.argv[1])

password = int(fileReader('server_password'))

if password == H(pass_arg):
    print(True)
else:
    print(False)
