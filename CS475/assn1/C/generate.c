#include<stdio.h>
#include<time.h>
#include<stdlib.h>

#include"generate.h"

int H(int n){
	return n + 273.15;
}

int * generate(int n) {
	int lst[n];
	int rndm = rand();
	lst[0] = rndm;
	for( int i = 1; i < n; i++) {
		lst[i] = H( lst[i-1] );
	}
}
