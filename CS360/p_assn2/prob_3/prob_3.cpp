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
TREE B();
TREE parseTree; /* holds the result of the parse */
char *nextTerminal; /* current position in input string */

int main()
{
	nextTerminal = "101010";

	parseTree = S();

	return 0;
}

TREE B()
{
}
