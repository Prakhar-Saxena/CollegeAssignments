#include <iostream>
#include "Socialite.h"
#include <fstream>

using namespace std;

//CONSTRUCTORS

//DEFAULT CONSTRUCTOR
Socialite::Socialite(){
	LName_ = "";
	FName_ = "";
	UserID_ = "";
	Picture_ = "";
	WebURL_ = "";
	WebDes_ = "";
	cliques_.clear();
}

//ALTERNATE CONSTRUCTOR
Socialite::Socialite(string FName, string LName, string UserID, string Picture, string WebURL, string WebDes){
	LName_ = LName;
	FName_ = FName;
	UserID_ = UserID;
	Picture_ = Picture;
	WebURL_ = WebURL;
	WebDes_ = WebDes;
}

//COPY CONSTRUCTOR
Socialite::Socialite(Socialite& s) {
	LName_ = s.getLName();
	FName_ = s.getFName();
	UserID_ = s.getUserID();
	Picture_ = s.getPicture();
	WebURL_ = s.getWebURL();
	WebDes_ = s.getWebDes();
	for (int i = 0; i < s.getNumOfCliques(); i++) {
		cliques_.push_back(s.getClique(i));
	}
}

//MUTATORS/SETTERS //MODIFYING/UPDATING ATTRIBUTES
void Socialite::setLName(string LName){
	LName_ = LName;
}

void Socialite::setFName(string FName){
	FName_ = FName;
}

void Socialite::setUserID(string UserID){
	UserID_ = UserID;
}

void Socialite::setPicture(string Picture){
	Picture_ = Picture;
}

void Socialite::setWebURL(string URL){
	WebURL_ = URL;
}

void Socialite::setWebDes(string webDes){
	WebDes_ = webDes;
}

void Socialite::addCliques(string a) {
	cliques_.push_back(a);
}

//INSPECTORS/GETTERS //ACCESSING THE ATTRIBUTES
string Socialite::getLName() const{
	return LName_;
}

string Socialite::getFName() const{
	return FName_;
}

string Socialite::getUserID() const{
	return UserID_;
}

string Socialite::getPicture() const{
	return Picture_;
}

string Socialite::getWebURL() const{
	return WebURL_;
}

string Socialite::getWebDes() const{
	return WebDes_;
}

int Socialite::getNumOfCliques() const {
	return cliques_.size();
}

string Socialite::getClique(int i) const {//getting the clique at index i
	return cliques_[i];
}

//OTHER METHODS
void Socialite::txtOut(ostream & out){ //method for printing out the text on console and creating a .txt file
	ofstream outFile;
	outFile.open(UserID_ + ".txt");
	string output = "";//string  that handles all the information/text
	output += "Socialite: " + FName_ + " " + LName_ + "\n";
	output += "User ID: " + UserID_ + "\n";
	output += "Picture: " + Picture_ + "\n";
	output += "Shared Link: " + WebURL_ + "\n";
	output += "Description: " + WebDes_ + "\n";
	output += "Cliques:\n";
	for (unsigned int i = 0; i < cliques_.size(); i++) {//to print out all the cliques
		output += cliques_[i] + "\n";
	}
	out << output << endl << endl;
	outFile << output;
	outFile.close();
}

void Socialite::HTMLOut(ostream & out){ //method for printing out the text on console and creating a .html file
	ofstream outFile;
	outFile.open(UserID_ + ".html");
	string output = "";//string  that handles all the information/text
	output += "<html>\n";
	output += "<head>\n";
	output += "<title>" + FName_ + " " + LName_ + "\'s Socialite Page</title>\n";
	output += "</head>\n";
	output += "<body>\n";
	output += "<img SRC = \"" + Picture_ + "\" ALT = \"" + FName_ + " " + LName_ + "\'s picture\" " + "ALIGN = \"RIGHT\" height = \"500px\" />\n";
	output += "<h1>"+ UserID_ + "</h1>\n";
	output += "<h2>" + FName_ + " " + LName_ + "</h2>\n";
	output += "<hr/>\n";
	output += "<p>" + FName_ + " wants to share <a HREF = \"" + WebURL_ + "\" TARGET = _blank>" + WebDes_ + "</a> with you : <br/>" + WebURL_ + "</p>\n";
	output += "<hr/>";
	output += "<p><i>Cliques:</i><p>\n";
	output += "<ul>\n";
	for (unsigned int i = 0; i < cliques_.size(); i++) {//to print out all the cliques
		output += "<li>" + cliques_[i] + "</li>\n";
	}
	output += "</ul>\n";
	output += "</body>\n";
	output += "</html>";
	outFile << output;
	out << output << endl << endl;
	outFile.close();
}