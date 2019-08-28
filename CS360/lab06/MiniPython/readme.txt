This folder contains the Mini language for CS 360

Important Files:
interpreterext.py - An interpreter for the Mini Language using the PLY parser generator.
programext.py - Objects used to evaluate the program after parsing
TestInput - A collect of short test files that can be used with the mini language.

Here is an example execution trace using some of the test files. 

ruxpin:Python mboady$ python interpreterext.py < TestInput/add.p
[42]
Generating LALR tables
Running Program
Dump of Symbol Table
Name Table
  x -> 5 
  s -> 15 
Function Table
  add
ruxpin:Python mboady$ python interpreterext.py < TestInput/addr.p
[42]
Running Program
Dump of Symbol Table
Name Table
  s -> 28 
  n -> 7 
Function Table
  addr
ruxpin:Python mboady$ python interpreterext.py < TestInput/fact.p
[42]
Running Program
Dump of Symbol Table
Name Table
  i -> 0 
  fact -> 120 
  n -> -5 
Function Table