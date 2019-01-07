#!/usr/bin/env python
#
# Prakhar Saxena
# 2018-05-04
#

import sys

if len(sys.argv) != 2:
        sys.exit("Invalid nubmer of arguments")
print sys.argv[1]
fileArg=sys.argv[1]
fileInput = open(fileArg, 'r').read()
print type(fileInput)
scoreList=fileInput.split('\n')
print scoreList
for x in scoreList:
        y=x.split(',')
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

