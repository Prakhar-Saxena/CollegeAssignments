#include "tic.h"

using namespace std;

//CONSTRUCTTOR
tBoard::tBoard() {
	for (int i = 0; i < 3; i++) {//rows
		for (int j = 0; j < 3; j++) {//columns
			board[i][j] = BLANK;
		}
	}
}

//Makes a move on the board
//X is the row and y is the column
//m is the symbol to place (either X or O)
//It returns true if the move was made
//If the move is illegal, return false and do not change the table
bool tBoard::move(symbol m, int x, int y) {
	if (x > 2 || y > 2 || x < 0 || y < 0) {//out of bounds of array
		return false;
	}
	else if (board[x][y] == BLANK) {//to check if there is no other symbol there
		board[x][y] = m;
		return true;
	}
	else {
		return false;
	}
}

//Returns true if the game is over
//This could be because of a winner or because of a tie
bool tBoard::game_over() {
	if (winner() !=BLANK) {
		return true;
	}
	else if (winner() == BLANK) {
		int filled = 0;//variable to check the number of filled boxes
		for (int i = 0; i < 3; i++) {//rows
			for (int j = 0; j < 3; j++) {//columns
				if (board[i][j] != BLANK) {
					filled++;//increasing the nubmer of filled places
				}
			}
		}
		if (filled == 9) {//since there are just 9 boxes in tic-tac-toe
			return true;
		}
		else {
			return false;
		}
	}
	else {
		return false;
	}
}

//Returns who won X or O.
//If the game was a tie, return  BLANK
symbol tBoard::winner() {
	if ( ( (board[0][0] == board[0][1]) && (board[0][0] == board[0][2]) && (board[0][0] == X) ) || ( (board[1][0] == board[1][1]) && (board[1][0] == board[1][2]) && (board[1][0] == X) ) || ( (board[2][0] == board[2][1]) && (board[2][0] == board[2][2]) && (board[2][0] == X) ) ) {//Horizontal conditions for X
		return X;
	}
	else if ( ( (board[0][0] == board[0][1]) && (board[0][0] == board[0][2]) && (board[0][0] == O) ) || ( (board[1][0] == board[1][1]) && (board[1][0] == board[1][2]) && (board[1][0] == O) ) || ( (board[2][0] == board[2][1]) && (board[2][0] == board[2][2]) && (board[2][0] == O) ) ) {//Horizontal Conditions for O
		return O;
	}
	else if ( ( (board[0][0] == board[1][0]) && (board[0][0] == board[2][0]) && (board[0][0] == X) ) || ( (board[0][1] == board[1][1]) && (board[0][1] == board[2][1]) && (board[0][1] == X) ) || ( (board[0][2] == board[1][2]) && (board[0][2] == board[2][2]) && (board[0][2] == X) ) ) {//Vertical Conditions for X
		return X;
	}
	else if ( ( (board[0][0] == board[1][0]) && (board[0][0] == board[2][0]) && (board[0][0] == O) ) || ( (board[0][1] == board[1][1]) && (board[0][1] == board[2][1]) && (board[0][1] == O) ) || ( (board[0][2] == board[1][2]) && (board[0][2] == board[2][2]) && (board[0][2] == O) ) ) {//Vertical Conditions for O
		return O;
	}
	else if ( ( (board[0][0] == board[1][1]) && (board[0][0] == board[2][2]) && (board[0][0] == X) ) || ( (board[0][2] == board[1][1]) && (board[0][2] == board[2][0]) && (board[0][2] == X) ) ) {//Diagonal Conditions for X
		return X;
	}
	else if (((board[0][0] == board[1][1]) && (board[0][0] == board[2][2]) && (board[0][0] == O)) || ((board[0][2] == board[1][1]) && (board[0][2] == board[2][0]) && (board[0][2] == O))) {//Diagonal Conditions for O
		return O;
	}
	else {
		return BLANK;
	}
}

//method to be used for output
//returning symbols would work too, since << has already been overloaded in symbol.cpp
string tBoard::getSymbol(int x, int y) const{
	switch (board[x][y]) {
	case X:
		return "X";
		break;
	case O:
		return "O";
		break;
	default:
		return " ";
		break;
	}
}

//operator overloading for outputing the tic-tac-toe board in the console
ostream & operator<<(ostream& os, const tBoard& myTable) {
	
	os << "   |  0  |  1  |  2  |" << endl;
	os << "   +-----------------+" << endl;
	os << "  0|  " << myTable.getSymbol(0, 0) << "  |  " << myTable.getSymbol(0, 1) << "  |  " << myTable.getSymbol(0, 2) << "  |" << endl;
	os << "   +-----------------+" << endl;
	os << "  1|  " << myTable.getSymbol(1, 0) << "  |  " << myTable.getSymbol(1, 1) << "  |  " << myTable.getSymbol(1, 2) << "  |" << endl;
	os << "   +-----------------+" << endl;
	os << "  2|  " << myTable.getSymbol(2, 0) << "  |  " << myTable.getSymbol(2, 1) << "  |  " << myTable.getSymbol(2, 2) << "  |" << endl;
	os << "   +-----------------+" << endl;
	return os;
}