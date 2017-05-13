#include "tic.h"
#include <iostream>
#include <string>

using namespace std;

int main()
{
	//Use the default constructor to create a new empty game.
	tBoard myGame;
	cout << "Hello! Welcome to Tic-Tac-Toe" << endl;
	
	//Create an array to hold my 2 values
	string player[2];
	
	//Get the Payer Names
	cout << "What is the name of the player going first (X)?" << endl;
	getline(cin,player[0]);
	cout << player[0] << " is X " << endl;
	
	cout << "What is the name of the player going second (O)?" << endl;
	getline(cin,player[1]);
	cout << player[1] << " is O " << endl;
	
	//Player 1 goes first
	//They are playing X
	int current_player=0;
	symbol piece = X;
	//Keep Going Until the Game is over
	while(!myGame.game_over())
	{
		//Draw the Board
		cout << myGame;
		//Ask the user for their move
		cout << player[current_player] << " enter space to place ";
		cout << piece;
		cout << " as ROW COL then press enter" << endl;
		//Read in the move
		int row;
		int col;
		cin >> row;
		cin >> col;
		//Check if the move is valid
		//Only go to the next player on valid moves
		if( myGame.move(piece,row,col) )
		{
			cout << "Move Successful." << endl;
			current_player=(current_player + 1 )%2;
			piece++;
		}else
		{
			cout << "Move Failed, try again." << endl;
		}
	}
	//The Game is over. Find out who won.
	cout << "Game Over" << endl;
	cout << myGame;
	switch(myGame.winner())
	{
		case(X):
			cout << "Congratulations " << player[0] << endl;
			break;
		case(O):
			cout << "Congratulations " << player[1] << endl;
			break;
		case(BLANK):
			cout << "TIE: Everyone Wins" << endl;
			break;
	}
	//Return to Exit
	return 0;
}