#include <iostream>
#include<iomanip>
using namespace std;
int main(void) {
	int tphil, thono, tseat, tlond, tmosc, thonk, tauck, tindo; // Variables for times
	cout << "What is the current time in Philadelphia? ";
	cin >> tphil; //Philadelphia
	//So the formula below gets rid of the problems that could have arised by simply addding the hours. adding 2400 and then doing the modulo operation eliminates the error that could have been caused by the time limit of 2400.
	thono = (2400 + (tphil - 600)) % 2400; //Honolulu
	tseat = (2400 + (tphil - 300)) % 2400; //Seattle
	tlond = (2400 + (tphil + 500)) % 2400; //London
	tmosc = (2400 + (tphil + 800)) % 2400; //Moscow
	thonk = (2400 + (tphil + 1200)) % 2400; //Honk Kong
	tauck = (2400 + (tphil + 1700)) % 2400; //Auckland
	tindo = (2400 + (tphil + 1030)) % 2400; //Indore, My Hometown in India
	cout << "Current time in other cities \n \n";
	cout << "Honolulu:   " << setw(4) << setfill('0') << thono << endl;
	cout << "Seattle:    " << setw(4) << setfill('0') << tseat << endl;
	cout << "London:     " << setw(4) << setfill('0') << tlond << endl;
	cout << "Moscow:     " << setw(4) << setfill('0') << tmosc << endl;
	cout << "Honk Kong:  " << setw(4) << setfill('0') << thonk << endl;
	cout << "Auckland:   " << setw(4) << setfill('0') << tauck << endl;
	cout << "Indore:     " << setw(4) << setfill('0') << tindo << endl;
	return 0;
}
