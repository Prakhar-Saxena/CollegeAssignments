all: run clean

run: build
	export DIMENSION=$(DIMENSION)
	export GAMES=$(GAMES)
	./G3
	
test: build
	export DIMENSION=8
	export GAMES=3
	./G3

build:
	gcc G3.c -o G3

clean:
	rm G3
