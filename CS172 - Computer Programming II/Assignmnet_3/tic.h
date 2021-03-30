#ifndef _TIC_TAC_TOE_
#define _TIC_TAC_TOE_

#include <vector>
#include <iostream>
#include <string>
#include "symbol.h"
#include <iomanip>
using namespace std;

class tBoard
{
	private:
		//array of symbols
		symbol board[3][3];
	public:
		//Default Constructor
		//Makes a board with all blank spaces
		tBoard();

		//Makes a move on the board
		//X is the row and y is the column
		//m is the symbol to place (either X or O)
		//It returns true if the move was made
		//If the move is illegal, return false and do not change the table
		bool move(symbol m, int x, int y);

		//Returns true if the game is over
		//This could be because of a winner or because of a tie
		bool game_over();

		//Returns who won X or O.
		//If the game was a tie, return  BLANK
		symbol winner();

		//method to be used for output
		//returning symbols would work too, since << has already been overloaded in symbol.cpp
		string getSymbol(int, int) const;
};

//Overload the output operator
ostream & operator<<(ostream& os, const tBoard& myTable);

#endif
