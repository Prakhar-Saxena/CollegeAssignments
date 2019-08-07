#include <stdlib.h>
#include <iostream>
#include <stack>
#include <vector>
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
	vector<TREE> child;
};

TREE makeNode1(char x, TREE t);
TREE makeNode4(char x, TREE t1, TREE t2, TREE t3, TREE t4);
TREE B();
TREE S();
TREE parseTree; /* holds the result of the parse */
string nextTerminal; /* current position in input string */
TREE makeTree(stack<string> S);

void printStack(stack<string> S);
void printPostorder(struct NODE* node);
void printPreorder(struct NODE* node);
int maxDepth(struct NODE* node);


int main()
{
	nextTerminal = "{wcs;s;}E"; /* in practice, a string
				  of terminals would be read from input */
	// using 'E' for ENDM
	parseTree = S();


	cout << maxDepth(parseTree) << endl;

	return 0;	
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
	NODE root;
	root->label = "S";
	int i = 1;
	TREE currentNode = *root;
	TREE firstS, secondS, thirdS;
	NODE saveNode;
	
	while(LOOKAHEAD != "E"){
		TREE currentNode = *root;
		if (STACK.top().substr(0,1) == LOOKAHEAD){
			LOOKAHEAD = nextTerminal.substr(i,1);
			i++;
			STACK.push(STACK.top().substr(1));
		}
		else if (STACK.top().substr(0,1) == "S"){
			if (LOOKAHEAD == "{"){
				STACK.push("{T" + STACK.top().substr(1)); // production (2)
				NODE left;
				left.label = '{';
				NODE right;
				right.label = 'T';
				currentNode->child.insert(left);
				currentNode->child.insert(right);
				currrentNode = *right;
			}
			else if(LOOKAHEAD == "s"){
				STACK.push("s;" +  STACK.top().substr(1)); // production (3)
				NODE left;
				left.label = 's';
				NODE right;
				right.label = ';';
				if(saveNode != FAILED)
					currentNode = *saveNode;
			}
			else if(LOOKAHEAD == "w"){
				STACK.push("wcS" +  STACK.top().substr(1)); // production (3)
				NODE left;
				left.label = 'w';
				NODE middle;
				middle.label = 'c';
				NODE right;
				right.label = 'S';
				currentNode = *right;
			}
		}
		else if (STACK.top().substr(0,1) == "T"){
			if (LOOKAHEAD == "{" || LOOKAHEAD == "w" || LOOKAHEAD == "s"){
				STACK.push("ST" + STACK.top().substr(1)); // production (4)
				NODE left;
				left.label = 'S';
				NODE right;
				right.label = 'T';
				currentNode->child.insert(left);
				currentNode->child.insert(right);
				currentNode = *left;
				saveNode = *right;
			}
			else if (LOOKAHEAD == "}"){
				STACK.push("}" + STACK.top().substr(1)); // production (5)
				NODE c;
				c.label = '}';
				currentNode->child.insert(c);
			}
		}
	}

	stack<string> newSTACK;

	while(! STACK.empty()){
		newSTACK.push(STACK.top());
		STACK.pop();
	}
	printStack(newSTACK);
	return root;
}

void printStack(stack<string> S){
	stack<string> SN = S;
	while(! SN.empty()){
		cout << SN.top() << endl;
		SN.pop();
	}
}

TREE makeTree(stack<string> S){
	NODE init;
	init->label = S.top();
	S.pop();
	while(! s.empty()){
		S.top()
		init->child = makeTree(S);
	}
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
