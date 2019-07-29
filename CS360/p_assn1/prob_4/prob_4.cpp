#include <stdlib.h>
#include <iostream>
#include <stack>
using namespace std;
#define FAILED NULL
typedef struct NODE *TREE;

/*
(1) <S> -> w c<S>
(2) <S> -> { <T>
(3) <S> -> s ;
(4) <T> -> <S><T>
(5) <T> -> }
*/

struct NODE {
	char label;
	TREE leftmostChild, rightSibling;
};

TREE makeNode0(char x);
TREE makeNode1(char x, TREE t);
TREE makeNode4(char x, TREE t1, TREE t2, TREE t3, TREE t4);
TREE B();
TREE S();
TREE parseTree; /* holds the result of the parse */
string nextTerminal; /* current position in input string */

void printPostorder(struct NODE* node);
void printPreorder(struct NODE* node);
int maxDepth(struct NODE* node);

int main()
{
	nextTerminal = "{wcs;s;}E"; /* in practice, a string
				  of terminals would be read from input */
	// using 'E' for ENDM
	parseTree = S();

	printPostorder(parseTree);
	cout << endl;
	printPreorder(parseTree);
	cout << endl;
	cout << maxDepth(parseTree) << endl;

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

// (1) <B> ! ǫ
// (2) <B> ! ( <B> ) <B>


// (1) <S> -> w c<S>
// (2) <S> -> { <T>
// (3) <S> -> s ;
// (4) <T> -> <S><T>
// (5) <T> -> }

TREE S()
{
	// string STACK = "<S>";
	stack<string> STACK;
	STACK.push("S");
	string LOOKAHEAD = nextTerminal.substr(0,1);

	int i = 1;

	TREE firstS, secondS, thirdS;
	
	while(LOOKAHEAD != "E"){
		if (STACK.top().substr(0,1) == LOOKAHEAD){
			LOOKAHEAD = nextTerminal.substr(i,1);
			i++;
			STACK.push(STACK.top().substr(1));
		}
		else if (STACK.top().substr(0,1) == "S"){
			if (LOOKAHEAD == "{"){
				STACK.push("{T" + STACK.top().substr(1)); // production (2)
			}
			else if(LOOKAHEAD == "s"){
				STACK.push("s;" +  STACK.top().substr(1)); // production (3)
			}
			else if(LOOKAHEAD == "w"){
				STACK.push("wcS" +  STACK.top().substr(1)); // production (3)
			}
		}
		else if (STACK.top().substr(0,1) == "T"){
			if (LOOKAHEAD == "{" || LOOKAHEAD == "w" || LOOKAHEAD == "s"){
				STACK.push("ST" + STACK.top().substr(1)); // production (4)
			}
			else if (LOOKAHEAD == "}"){
				STACK.push("}" + STACK.top().substr(1)); // production (5)
			}
		}
	}
	while(! STACK.empty()){
		cout << STACK.top() << endl;
		STACK.pop();
	}
	return FAILED;
}

void printPreorder(struct NODE* node) 
{
	if (node == NULL)
		return;
	/* first print data of node */
	std::cout << node->label << " ";
	
	/* then recur on left sutree */
	printPreorder(node->leftmostChild);
	
	/* now recur on right subtree */
	printPreorder(node->rightSibling); 
}


void printPostorder(struct NODE* node) 
{
	if (node == NULL)
		return;
	
	/* first recur on left subtree */
	printPostorder(node->leftmostChild);
	
	/* then recur on right subtree */
	printPostorder(node->rightSibling);
	
	/* now deal with the node */
	std::cout << node->label << " "; 
} 

int maxDepth(struct NODE* node)  
{
		if (node == NULL)
			return 0;
		else
		{
			/* compute the depth of each subtree */
			int lDepth = maxDepth(node->leftmostChild);
			int rDepth = maxDepth(node->rightSibling);
	
			/* use the larger one */
			if (lDepth > rDepth)
				return(lDepth + 1);
			else return(rDepth + 1);

		}
}
