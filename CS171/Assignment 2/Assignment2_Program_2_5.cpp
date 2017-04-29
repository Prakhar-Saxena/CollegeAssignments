#include <iostream>
#include <string>
#include <cmath> // used for the pow function to raise the powers of 10 using the loop variable

using namespace std;

int makeCheckDigit(int zipcode){ //this function returns the check digit
	int n, sum=0, rem, chkdgt; // rem is remainder
	n = zipcode;
	while (n != 0){ // this loop ads the digits
		rem = n % 10;
		sum += rem;
		n /= 10;
	}
	chkdgt = 10 - (sum % 10);
	return chkdgt;
}

const string HALFBAR = ":";
const string FULLBAR = "|";
const string ONEBAR = "00011";
const string TWOBAR = "00101";
const string THREEBAR = "00110";
const string FOURBAR = "01001";
const string FIVEBAR = "01010";
const string SIXBAR = "01100";
const string SEVENBAR = "10001";
const string EIGHTBAR = "10010";
const string NINEBAR = "10100";
const string ZEROBAR = "11000";
const int NUMBER_OF_DIGITS_IN_A_ZIP_CODE = 5;
const string ZERO_DIGIT = "0";
const string ONE_DIGIT = "1";

string convertDigit(int value){ // this function returns the respective constant depending on the argument
	switch (value){
	case 1:
		return ONEBAR;
	case 2:
		return TWOBAR;
	case 3:
		return THREEBAR;
	case 4:
		return FOURBAR;
	case 5:
		return FIVEBAR;
	case 6:
		return SIXBAR;
	case 7:
		return SEVENBAR;
	case 8:
		return EIGHTBAR;
	case 9:
		return NINEBAR;
	case 0:
		return ZEROBAR;
	default:
		return " ";
	}
}

string barcode(int zipcode){ //this funciton prints out and returns the barcode in the form of :(colons) and |(full bars
	int n, r;
	n = (zipcode * 10) + makeCheckDigit(zipcode);
	string substrng, bcode;
	for (int i = 5; i >= 0; i--){ // this loop isolates digits in the zipcode
		int j = pow(10, i);
		r = n / j;
		substrng = convertDigit(r);
		for (int x = 0; x <= 5; x++){ // checks each index of the barcode
			if (substrng[x] == '1'){
				bcode += FULLBAR;
			}
			else if (substrng[x] == '0'){
				bcode += HALFBAR;
			}
		}
		n %= j;
	}
	cout << bcode;
	cout << endl;
	return bcode;
}

int main()
{
	cout << "Enter the zipcode:";
	int zc;
	cin >> zc;
	cout << endl;
	if (zc >= pow(10,NUMBER_OF_DIGITS_IN_A_ZIP_CODE)){ // to check the lenght of digits
		cout << "The zipcode you entered has more than 5 digits \n";
	}
	if (zc >= 0){//check for negative
		barcode(zc);
	}
	else{
		cout << endl << "The zipcode you entered is a negative number \n";
	}
	cout << endl;
	return 0;
}