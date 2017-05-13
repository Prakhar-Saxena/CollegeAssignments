#include <iostream>
#include <math.h>
#include <iomanip>
#include <string>

using namespace std;

//ALL THE CONSTANTS
const double safe = 0.00;
const double someImpairment = 0.04;
const double significantAffected = 0.08;
const double someCriminalPenalties = 0.10;
const double deathPossible = 0.30;
const string SAFE = "Safe To Drive";
const string SOMEIMPAIR = "Some Impairment";
const string SIGNIFICANT = "Driving Skills Significantly Affected";
const string MOST_STATES = "Criminal Penalties in Most US States";
const string ALL_STATES = "Legally Intoxicated - Criminal Penalties in All US States";
const string YOURE_DEAD = "Death is Possible!";

void computeBloodAlcoholConcentration(int numDrinks, int weight, int duration, double &maleBAC, double &femaleBAC){ //this function calculates BAC of both male and female; that depends on number of drinks, weight and duration since the last drink.
	maleBAC = ((static_cast <double>(numDrinks) / static_cast <double>(weight))* 3.8) - ((static_cast <double>(duration)/40)* 0.01); //based on given constants for male
	femaleBAC = ((static_cast <double>(numDrinks) / static_cast <double>(weight))* 4.5) - ((static_cast <double>(duration)/40)* 0.01);
	if (maleBAC <= 0){ //condition if the value goes negative
		maleBAC = 0;
	}
	if (femaleBAC <= 0){ //condition if the value goes negative
		femaleBAC = 0;
	}
}

string impairment(double bac){ //this function returns the impairment condition on different range of values
	if (bac == safe){
		return SAFE;
	}
	else if (bac > safe && bac < someImpairment){
		return SOMEIMPAIR;
	}
	else if (bac >= someImpairment && bac < significantAffected){
		return SIGNIFICANT;
	}
	else if (bac >= significantAffected && bac < someCriminalPenalties){
		return MOST_STATES;
	}
	else if (bac >= someCriminalPenalties && bac <= deathPossible){ //made this change(from < to <= AND >= to >) to match the sample output given in the pdf
		return ALL_STATES;
	}
	else if (bac > deathPossible){
		return YOURE_DEAD;
	}
	else{
		return NULL;
	}
}

int promptForInteger(const string &message, int lower, int upper){ //this function will be used in main to restrict the users from entering unrealistic data values
	int checkvar;
	do
	{
		cout << endl << message;
		cin >> checkvar;
	} while (!(checkvar >= lower && checkvar <= upper)); //limits specified
	return checkvar;
}

char promptForMorF(const string &message){ //this funciton is lucid, the purpose of this function is to print out the argument message, and then read the input if the input matches the requirements specified it returns F or M
	char g;
	cout << endl << message;
	cin >> g;
	if (g == 'F' || g == 'f'){ // it accepts both F and f
		return 'F';
	}
	else if (g == 'M' || g == 'm'){ // it accepts both M and m
		return 'M';
	}
	else { //alternative scenario
		promptForMorF(message); //recursion
		return NULL;
	}
}

void showImpairmentChart(int weight, int duration, bool isMale){ //the final function, prints out the final output in an orderly fashion
	string stat; //variable to store the status
	double bac = 0, fbac, mbac; //General BAC, Female BAC and Male BAC
	for (int numDrinks = 0; numDrinks <= 10; numDrinks++){ //numDrinks stands for number of Drinks
		computeBloodAlcoholConcentration(numDrinks, weight, duration, mbac, fbac);
		if (isMale){ //isMale is a boolean parameter that is true if gender is male and false if female
			bac = mbac;
		}
		else{
			bac = fbac;
		}
		stat = impairment(bac);
		cout << setw(8) << numDrinks << setw(7) << bac << " " + stat << endl;
	}
}

int main(){
	double bac = 0, mbac = 0, fbac = 0;
	string stat, sexop; //sexop is used for output
	bool isMale = true; //isMale is a boolean parameter that is true if gender is male and false if female
	cout << fixed << setprecision(3); //to print out the BAC values upto 3 decimal point digits
	int weight = promptForInteger("Enter your weight (in lbs): ", 0, 1230); //no real entity can have a weight below 0; 1230 is the weight of the heaviest human in the world
	int duration = promptForInteger("How many minutes has it been since your last drink? ", 0, 1000); // limiting the time input from 0 to 1000
	char sex = promptForMorF("Enter your sex as M or F: ");
	if (sex == 'F'){
		isMale = false;
		sexop = "female"; //used for printing out
	}
	else if (sex == 'M'){
		isMale = true;
		sexop = "male"; //used for printing out
	}
	cout << endl << weight << " pounds, " << sexop << ", " << duration << " minutes since last drink" << endl;
	cout << endl << "# drinks" << setw(7) << "BAC" << setw(7) << "Status" << endl;
	showImpairmentChart(weight, duration, isMale);
	return 0;
}