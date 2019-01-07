cc = gcc
flags =

csv : main.o csv.o
	$(cc) $(flags) main.o csv.o -o $@

main.o : main.c csv.h
	$(cc) -c $(flags) main.c

csv.o : csv.c csv.h
	$(cc) -c $(flags) csv.c

.PHONY : clean cleanall

clean :
	-\rm *.o

cleanall : clean
	-\rm csv
