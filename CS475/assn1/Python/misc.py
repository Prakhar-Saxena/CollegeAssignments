#!/usr/bin/env python3

def fileWriterList(lst, filename):
    f = open(filename, 'w')
    for i in lst:
        print(i)
        f.write(str(i) + '\n')

def fileWriterNum(num, filename):
    f = open(filename, 'w')
    print(num)
    f.write(str(num))

def fileReader(filename):
    f = open(filename, 'r')
    return f.read()

def fileClear(filename):
    f = open(filename,'w')
    f.seek(0)
    f.truncate()
