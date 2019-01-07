#!/usr/bin/env python
#
# Prakhar Saxena
# 2018-05-04
#

import sys

if len(sys.argv) != 2:
        sys.exit("Invalid nubmer of arguments")
fileArg=sys.argv[1]
fileInput = open(fileArg, 'r').read()
ids=fileInput.split('\n')
dictIds=dict()
for x in ids:
	y=x.split(' ',1)
	if len(y)<=1:
		break
	dictIds[int(y[0])]=y[1]
for k in sorted(dictIds.keys()):
	print k, dictIds[k]
