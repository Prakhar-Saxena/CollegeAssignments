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
scoreList=fileInput.split('\n')
for x in scoreList:
	y=x.split(' ')
	if len(y)<=1:
		break
	i=1
	sumN=0
	avg=0
	while i<len(y):
		sumN=sumN+int(y[i])
		i=i+1
	avg=sumN/(len(y)-1)
	print y[0], avg
