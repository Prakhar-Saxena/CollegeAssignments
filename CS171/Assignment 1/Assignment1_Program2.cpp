#include <iostream>
#include<iomanip>
using namespace std;
int main(void) {
	long long fo; // fluid ounces
	cout << "How many fluid ounces do you have?" << endl;
	cin >> fo; // input from user of the amount of fluid ounces
	long long ba = fo / 5376; // barel(s)
	long long ga = (fo % 5376) / 128; //gallon(s)
	long long qu = ((fo % 5376) % 128) / 32; //quart(s)
	long long pi = (((fo % 5376) % 128) % 32) / 16; //pint(s)
	long long cu = ((((fo % 5376) % 128) % 32) % 16) / 8; //cup(s)
	long long gi = (((((fo % 5376) % 128) % 32) % 16) % 8) / 4; //gill(s)
	long long ts = ((((((fo % 5376) % 128) % 32) % 16) % 8) % 4) * 2; //tablespoons
	cout << endl << fo << " fluid ounces can be divied long longo:" << endl;
	cout << setw(7) << ba << setw(15) << "barrel(s)" << endl;
	cout << setw(7) << ga << setw(15) << "gallon(s)" << endl;
	cout << setw(7) << qu << setw(15) << "quart(s)" << endl;
	cout << setw(7) << pi << setw(15) << "pint(s)" << endl;
	cout << setw(7) << cu << setw(15) << "cup(s)" << endl;
	cout << setw(7) << gi << setw(15) << "gill(s)" << endl;
	cout << setw(7) << ts << setw(15) << "tablespoons" << endl;
	return 0;
}
