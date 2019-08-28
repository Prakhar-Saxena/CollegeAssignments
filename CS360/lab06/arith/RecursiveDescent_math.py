#CS 360 2013
#Drexel University
#Mark Boady
#This solution is from the book pg 228-230 but implemented in python

#The language is
# expression -> term (+ term}
# term -> factor (* factor}
# factor -> number | ( expr )
import sys

class RDParser:
    def __init__(self):
        self.position=-1
        self.input=[]
    def parse(self,expression):
        #Initialize the input as a list
        self.input=list(expression)
        self.position=-1
        #Get the first character to start up the parser
        self.getToken()
        return self.command()
    def getToken(self):
        #Skip Whitespace
        self.position+=1
        while self.input[self.position]==' ':
            self.position+=1
        self.token=self.input[self.position]
    def match(self,c,e):
        if self.token==c:
            self.getToken()
        else:
            print "Error: "+e
    def command(self):
        #command -> expr \n
        result = self.expr()
        if self.token=="\n":
            return result
        else:
            print "Error: tokens after end of input"
    def expr(self):
        #expr -> term { + term}
        result=self.term()
        while self.token == '+':
            self.match('+',"+ expected")
            result +=self.term()
        return result
    def term(self):
        #term -> factor { * factor}
        result = self.factor()
        while self.token == '*':
            self.match('*',"* Expected")
            result *= self.factor()
        return result
    def factor(self):
        #factor -> number | (expr)
        if self.token=="(":
            self.match("(","( Expected")
            result = self.expr()
            self.match(")",") Expected")
        else:
            result = self.number()
        return result
    def number(self):
        #number -> [0-9]*
        mystr=""
        while self.token.isdigit():
            mystr+=self.token
            self.getToken()
        return int(mystr)
        
#Main Input
#Read a line, parse it, and repeat
if __name__ == '__main__' :
    print "Hello. Type ctrl-D (End of File) to quit."
    print "Enter a math expression using 0-9,*,+,()"
    print "Example: (2+3)*(4+5)"
    expression = sys.stdin.readline()
    while expression != "":
        parser=RDParser()
        res = parser.parse(expression)
        print("The answer is "+str(res))
        expression = sys.stdin.readline()
