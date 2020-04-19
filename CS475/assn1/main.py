#!/usr/bin/env python3

import sys

from Misc import fileClear

if sys.argv[1] == "clean":
    fileClear('pswd')
    fileClear('pswd_dvc')

