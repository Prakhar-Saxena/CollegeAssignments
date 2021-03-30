#include "Socialite.h"

using namespace std;

int main(){

	//ASSIGNMENT 1 CODE
	//creating Socialite objects
	/*Socialite PrakharSaxena("Prakhar", "Saxena", "ps668", "https://sd.keepcalm-o-matic.co.uk/i/keep-calm-and-hakuna-matata-3117.png", "http://www.pages.drexel.edu/~ps668/", "My CS 164 Page");
	PrakharSaxena.addCliques("Drexel");
	Socialite GeraltOfRivia("Geralt", "Of Rivia", "geralt", "https://upload.wikimedia.org/wikipedia/en/4/43/Geralt_of_Rivia.png", "http://witcher.wikia.com/wiki/Geralt_of_Rivia", "Witcher Wikia");
	Socialite Saitama("Saitama", "", "onepunch", "http://www.gambitmag.com/wp-content/uploads/2016/09/HmWDsHkfTFyShq7GqbE1_b01.png", "http://onepunchman.wikia.com/wiki/Saitama", "One Punch Man Wikia");
	Saitama.addCliques("DrawnAndQuartered");
	Socialite BenedictCumberbatch("Benedict", "Cumberbatch", "benedict", "http://cdn.skim.gs/images/k7yeadop9xvv0viuaslm/the-very-important-evolution-of-benedict-cumberbatch-s-hair-in-15-pics-a-hair-story-of-ben","https://en.wikipedia.org/wiki/Benedict_Cumberbatch","Benedict Cumberbatch Wikipedia page");
	BenedictCumberbatch.addCliques("Glitterati");
	Socialite NarendraModi("Narendra", "Modi", "namo", "https://upload.wikimedia.org/wikipedia/commons/9/90/PM_Modi_2015.jpg", "https://www.mygov.in/", "Indian Government");
	NarendraModi.addCliques("BeTheChange");

	PrakharSaxena.txtOut(cout);
	PrakharSaxena.HTMLOut(cout);
	GeraltOfRivia.txtOut(cout);
	GeraltOfRivia.HTMLOut(cout);
	Saitama.txtOut(cout);
	Saitama.HTMLOut(cout);
	BenedictCumberbatch.txtOut(cout);
	BenedictCumberbatch.HTMLOut(cout);
	NarendraModi.txtOut(cout);
	NarendraModi.HTMLOut(cout);
	*/
	
	//ASSIGNMENT 2 CODE
	ifstream inFile;
	string ifile = "";
	cout << "Enter the name of the file that you want to read from:" << endl;
	cin >> ifile;
	inFile.open(ifile);
	string input;
	vector <Socialite> v;
	for (int i = 0; !inFile.eof(); i++) {//this loop is for reading the file
		Socialite s;
		getline(inFile, input);//infile >> input; won't work
		s.setUserID(input);
		getline(inFile, input);
		s.setFName(input);
		getline(inFile, input);
		s.setLName(input);
		getline(inFile, input);
		s.setPicture(input);
		getline(inFile, input);
		s.setWebURL(input);
		getline(inFile, input);
		s.setWebDes(input);
		getline(inFile, input);
		while (input != "++++") {//to read in the cliques and look for the ending information fo 1 Socialite
			s.addCliques(input);
			getline(inFile, input);
		}
		v.push_back(Socialite(s));
	}
	
	for (unsigned int i = 0; i < v.size(); i++){//for outputing everything
		v[i].txtOut(cout);
		v[i].HTMLOut(cout);
	}

	return 0;
}