#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	long long tc1, tc2, tc3, tc4, tc5, total=0; // Declaring all the variables for tuition and total
	double rate;
	cout << "Enter the initial tuition amount : ";
	cin >> tc1; //input from user of the initioal tuition amount
	cout << "Enter the yearly tuition increase(as a percentage) : ";
	cin >> rate; //input from user of yearly tuition increase rate
	rate = 1 + (rate / 100); // converting rate in the form of 1.0r
	tc1 *= 100; //turning the amount into cents/pennies
	tc2 = tc1 * rate; //assigning the tuition for next yaers by multiplying the initial tuition amount with the newly calculated rate
	tc3 = tc2 * rate;
	tc4 = tc3 * rate;
	tc5 = tc4 * rate;
	cout << fixed << setprecision(2);
	cout << "Tuition of year 1 is: $" << setw(15) << static_cast<double>(tc1) / 100 << endl; //printing out the tuition amounts, using the static cast to convert the long long to double
	total += tc1; //adding the yearly tuition amounts to the total
	cout << "Tuition of year 2 is: $" << setw(15) << static_cast<double>(tc2) / 100 << endl;
	total += tc2;
	cout << "Tuition of year 3 is: $" << setw(15) << static_cast<double>(tc3) / 100 << endl;
	total += tc3;
	cout << "Tuition of year 4 is: $" << setw(15) << static_cast<double>(tc4) / 100 << endl;
	total += tc4;
	cout << "Tuition of year 5 is: $" << setw(15) << static_cast<double>(tc5) / 100 << endl;
	total += tc5;
	cout << "Total Tuition Cost is $" << setw(15) << static_cast<double>(total) / 100 << endl;
	return 0;
}