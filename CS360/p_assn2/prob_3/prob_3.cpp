#include <stdlib.h>
#include <iostream>
using namespace std;
#define FAILED NULL
typedef struct NODE *TREE;

struct NODE {
	char label;
	TREE leftmostChild, rightSibling;
};

TREE makeNode0(char x);
TREE makeNode1(char x, TREE t);
TREE makeNode4(char x, TREE t1, TREE t2, TREE t3, TREE t4);
TREE S();
TREE A();
TREE C();
TREE B();
TREE D();
TREE parseTree; /* holds the result of the parse */
char *nextTerminal; /* current position in input string */

int main()
{
	nextTerminal = "101010";

	parseTree = S();

	return 0;
}

TREE makeNode0(char x)
{
	TREE root;
	root = (TREE) malloc(sizeof(struct NODE));
	root->label = x;
	root->leftmostChild = NULL;
	root->rightSibling = NULL;
	return root;
}

TREE makeNode1(char x, TREE t)
{
	TREE root;
	root = makeNode0(x);
	root->leftmostChild = t;
	return root;
}

TREE makeNode4(char x, TREE t1, TREE t2, TREE t3, TREE t4)
{
	TREE root;
	root = makeNode1(x, t1);
	t1->rightSibling = t2;
	t2->rightSibling = t3;
	t3->rightSibling = t4;
	return root;
}

TREE S() // for the base production S
{
	TREE firstS, secondS;
	if(*nextTerminal == '0'){ // for production A, becasue that's the base for 0
		nextTerminal++;
		firstS = A();
	}
	else if(*nextTerminal == '1'){ // for production B, becasue that's the base production for 1
		nextTerminal++;
		firstS = B();
	}
	else{
		return makeNode1('S', makeNode0('e')); // empty, for nothing
	}
}

TREE A() // for the production A, this is the base for 0 C 1
{
	TREE firstA, secondA;
	if(*nextTerminal == '0'){ // production C is followed
		nextTerminal++;
		firstA = C();
		if(firstA != FAILED && *nextTerminal == '1'){
			nextTerminal++;
			// secondA =
	}
	else if(*nextTerminal == '1'){
		return makeNode1('A', makeNode0('e'));
}

TREE C() // for the production C, this is the second production that takes care of 0 C 1 C rule
{
	TREE firstC, secondC;
	if(*nextTerminal == '0'){
		nextTerminal++;
		firstC = C();
	}
	// I'm not exactly sure of the code commented below would implement what I had in mind..
	/*
	else if(*nextTerminal == '1'){
		nextTerminal++;
		firstC = C();
	}*/
	else{
		return makeNode1('C', makeNode0('e')); // empty
	}
}

TREE B() // production B, this is the base for 1 D 0 rule
{
	TREE firstB, secondB;
	if(*nextTerminal == '1'){
		nextTerminal++;
		firstB = D();
	}
	else if(*nextTerminal == '0'){
		return makeNode('B', makeNode0('e'));
	}
}

TREE D() // production D, this is the second but more general production that takes care of 1 D 0 D rules
{
	TREE firstD, secondD;
	if(*nextTerminal == '1'){
		nextTerminal++;
		firstD = D();
	}
	else if(*nextTerminal == '0'){
		nextTerminal++;
		firstD = D();
	}
	else{
		return makeNode1('D', makeNode0('e')); // empty
	}
}
