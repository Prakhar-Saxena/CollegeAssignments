#ifndef _Socialite_H
#define _Socialite_H

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

class Socialite{
public:
	//CONSTRUCTORS
	Socialite();
	Socialite(string, string, string, string, string, string);
	Socialite(Socialite&);//copy constructor

	//MUTATORS
	void setLName(string);
	void setFName(string);
	void setUserID(string);
	void setPicture(string);
	void setWebURL(string);
	void setWebDes(string);
	void addCliques(string);

	//INSPECTORS
	string getLName() const;
	string getFName() const;
	string getUserID() const;
	string getPicture() const;
	string getWebURL() const;
	string getWebDes() const;
	int getNumOfCliques() const;
	string getClique(int) const;

	//OTHER METHODS
	void txtOut(ostream & out);
	void HTMLOut(ostream & out);
private:
	//ATTRIBUTES
	string LName_;
	string FName_;
	string UserID_;
	string Picture_;
	string WebURL_;
	string WebDes_;
	vector <string> cliques_;
};
#endif