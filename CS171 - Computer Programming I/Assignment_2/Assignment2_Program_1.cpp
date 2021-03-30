#include <iostream>
using namespace std;

bool leap_year(int year){ //the leap year function
	if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0){ //checks the conditions
		cout << "LEAP YEAR \n";
		return true;
	}
	else{
		cout << "NOT LEAP YAER \n";
		return false;
	}
}

int main()
{
	int y;
	cout << "Enter the year \n";
	cin >> y;
	leap_year(y);
	return 0;
}