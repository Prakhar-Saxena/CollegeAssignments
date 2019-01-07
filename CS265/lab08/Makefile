cc = gcc

EXE = foo

JAVAC = javac

JRE = java

PAGER = less

TEST_OUT = test.out

EXP_OUT = expected.out

.PHONY : clean run-py run-c read run-java save-java test-java

foo.o : foo.c foo.h
	$(cc) -c foo.c

main.o : main.c foo.h
	$(cc) -c main.c

$(EXE) : main.o foo.o
	$(cc) -o$(EXE) main.o foo.o

run-c : $(EXE)
	./$(EXE)

run-py : foo.py
	./foo.py

read : README
	if [ -f README ]; then \
		$(PAGER) README; \
	fi

foo.class : foo.java
	$(JAVAC) foo.java

run-java : foo.class
	$(JRE) foo

save-java :
	$(JRE) foo > $(TEST_OUT)

test-java : $(TEST_OUT) $(EXP_OUT)
	-@if diff $(TEST_OUT) $(EXP_OUT) &> /dev/null ; then \
		echo "Passed!" ;\
	else \
		echo "Not the same!" ;\
	fi

clean :
	rm foo.o main.o $(EXE) foo.class test.out;\
	find . -name "*.o" -type f -delete
