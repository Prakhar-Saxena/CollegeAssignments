#!/usr/bin/env python2
#
# Prakhar Saxena
# 2018-05-17
#


import sys

class Stack:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []
	
	def peek(self):
		return self.items[len(self.items)-1]
	
	def push(self,item):
		self.items.append(item)
		return 0
	
	def pop(self):
		return self.items.pop()
	
	def size(self):
		return len(self.items)
	
	def printStack(self):
		for i in reversed(self.items):
			print i

def tokenise( fin ) :
        '''generator, serves up one token at a time
        input - a valid, openo file handle (object)
        output - next token (as a string)
        side-effects - input pointer is moved'''

        for line in fin :
                for tok in line.split() :
                        yield tok

precedence={}
precedence['/']=2
precedence['*']=2
precedence['%']=2
precedence['+']=1
precedence['-']=1
operatorList=['/','*','%','+','-']

def infix2postfix( inpExp ) :
	s=Stack()
	pfExp=[]
	tokenList=inpExp.split()
	tokenList.append(')')
	s.push('(')


	for token in tokenList:
		if token == '(':
			s.push(token)
		elif token == ')':
			stackTop=s.peek()
			while stackTop != '(':
				pfExp.append(stackTop)
				s.pop()
				if s.isEmpty:
					break
				else:
					stackTop=s.pop()
			s.pop()
		elif token.isdigit():
			pfExp.append(token)
		elif token in operatorList:
			while (not s.isEmpty()) and (s.peek() in operatorList) and (precedence[s.peek()] >= precedence[token]):
				pfExp.append(s.pop())
			s.push(token)
	return pfExp

def evalPostfix ( inpExp ) :
	s=Stack()
	for inp in inpExp:
		if inp.isdigit():
			s.push(inp)
		else:
			y = int(s.pop())
			x = int(s.pop())
			result=0.00
			if inp == '/':
				result = x / y
			elif inp == '*':
				result = x * y
                        elif inp == '%':
                                result = x % y
                        elif inp == '+':
                                result = x + y
                        elif inp == '-':
                                result = x - y
			s.push(result)
	return s


def main( args ) :
        if len( args ) < 2 :  # read stdin
                f = sys.stdin
        else :
                f = open( args[1] )

        tokens = tokenise( f )
	for line in f:
		pfExp = infix2postfix(line)
		s=evalPostfix(pfExp)
		print line, '=', s.peek()
		print '-'*20
        return 0

if __name__ == '__main__' :
        sys.exit( main( sys.argv ))

