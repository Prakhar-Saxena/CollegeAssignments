Prakhar Saxena | CS 472 Homework # 2 | October 12, 2020 | README

Introduction
THis assignment was implemented over a week using teh following softwares and tools:
    - PyCharm
    - ViM
    - git (GitHub)
    - Windows Terminal
    - Tux

The assignment includes two files, 'ftpClient.py' and 'logger.py'. It implements the client side of an FTP server.
I tried to get all the requirements for this assignment, but wasn't able to get them all.
Frankly, I didn't realise how long this assignment would take, I've already spent over 12 hours on this assignment;
I was led to believe this is a 3 credit course.

Either way, i was able to accomplish some major requirements of the assignment.

Accomplishments:
    - Command line processing
    - Handling arguments provided
    - most commands working
    - Handled all the errors to my knowledge; try-expected everywhere.
    - Logging
    - Questions; answered in a separate document

Difficulties and missed accomplishments:
Unfortunately due to time constraints, I wasn't able to test every single case of my client.
But I've documented and commented it well, so that I can take a shot at it after this term, when I have more time,
because it would keep bugging me.
This is one of the hardest assignments I have ever encountered.
The amount of hours I spent trying to comprehend the complex commands going through the RFCs and testing them out on the
very inconsistent FTP clients on windows and tux, I found terribly frustrating.

How to run teh program:
I have created a makefile for your ease. All you have to do is type:
    make
And it will ask you for teh username and password. Then you would find yourself in a menu REPL.
The case of commands you type wouldn't matter, I handled it converting them all to upper case, following the FTP
requirements.
You can find the logs in:
    log_file
In order to clean the log_file you can just run:
    make clean


Cheers

Prakhar Saxena