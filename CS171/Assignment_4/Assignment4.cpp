#include <iostream>
#include <math.h>
#include <iomanip>
#include <string>
#include <ctime>
#include <cstdlib>

using namespace std;

void setupDoors(char &door1, char &door2, char &door3){ //sets up the doors with random values
	int rnum = rand() % 3; //random number generator
	switch (rnum){ //just three cases are possible, therefore 3 unmbers and switch case
	case 0:
		door1 = 'C';
		door2 = 'G';
		door3 = 'G';
		break;
	case 1:
		door1 = 'G';
		door2 = 'C';
		door3 = 'G';
		break;
	case 2:
		door1 = 'G';
		door2 = 'G';
		door3 = 'C';
		break;
	}
}

void pickDoorChoices(char door1, char door2, char door3, int &doorPlayer, int &doorMonty){ //picks the door choices for player and monty depending on the doors
	doorPlayer = (rand() % 3) + 1; // randomizing the player's door
	switch (doorPlayer){ // just 3 cases there fore switch case
	case 1:
		if (door2 == 'C'){ // since monty can only choose a goat door
			doorMonty = 3;
		}
		else {
			doorMonty = 2;
		}
		break;
	case 2:
		if (door1 == 'C'){
			doorMonty = 3;
		}
		else {
			doorMonty = 1;
		}
		break;
	case 3:
		if (door1 == 'C'){
			doorMonty = 2;
		}
		else {
			doorMonty = 1;
		}
		break;
	}
}

void switchDoor(int &doorPlayer, int doorMonty){ // function to switch doors
	switch (doorPlayer){
	case 1:
		if (doorMonty == 2){ // so that the player doesn't change to the door mony has choses
			doorPlayer = 3;
		}
		else if (doorMonty == 3){
			doorPlayer = 2;
		}
		break;
	case 2:
		if (doorMonty == 1){
			doorPlayer = 3;
		}
		else if (doorMonty == 3){
			doorPlayer = 1;
		}
		break;
	case 3:
		if (doorMonty == 2){
			doorPlayer = 1;
		}
		else if (doorMonty == 1){
			doorPlayer = 2;
		}
		break;
	}
}

void door(char door1, char door2, char door3, int doorPlayer, char &doorChosen){ //to assign a character value to a variable defined as the door chosen by player since integer can't be compared with character
	switch (doorPlayer){ //self explanatory
	case 1:
		doorChosen = door1;
		break;
	case 2:
		doorChosen = door2;
		break;
	case 3:
		doorChosen = door3;
		break;
	}
}

int main(){
	srand(time(0));
	char door1, door2, door3, dChosen = ' '; //dChosen is for the door that player chooses
	int doorPlayer = 0, doorMonty = 0, count1 = 0, count2 = 0; // count1 for times when the player switches door and count2 for when the player sticks to his previous choice
	for (int i = 1; i <= 10000; i++){
		setupDoors(door1, door2, door3);
		pickDoorChoices(door1, door2, door3, doorPlayer, doorMonty);
		if (i <= 5000){
			switchDoor(doorPlayer, doorMonty);
			door(door1, door2, door3, doorPlayer, dChosen);
			if (dChosen == 'C'){
				count1++;
			}
		}
		else if (i > 5000){
			door(door1, door2, door3, doorPlayer, dChosen);
			if (dChosen == 'C'){
				count2++;
			}
		}
	}
	double percent1 = (static_cast<double>(count1) / 5000) * 100;
	double percent2 = (static_cast<double>(count2) / 5000) * 100;
	cout << "The strategy of switching doors every time wins " << percent1 << "% of the time.\n";
	cout << "The strategy of not switching doors every time wins " << percent2 << "% of the time.\n";
	if (percent1 > percent2){
		cout << endl << "The strategy of switching doors every time is better than not switching.  Therefore, switching doors is to the player's advantage" << endl;
	}
	else if (percent1 < percent2){
		cout << endl << "The The strategy of not switching doors every time is better than switching. Therefore, switching doors is NOT to the player's advantage" << endl;
	}
	else{
		cout << endl << "Both are same" << endl;
	}
	return 0;
}