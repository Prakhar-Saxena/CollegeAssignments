#include "symbol.h"
#include <cassert>

std::ostream & operator<<(std::ostream& os, const symbol& my_symbol)
{
	switch(my_symbol)
	{
		case(X):
			os << "X";
			break;
		case(O):
			os << "O";
			break;
		default:
			os << " ";
			break;
	}
	return os;
}
//Change the value and return the updated value
symbol& operator++(symbol& my_symbol)
{
	switch(my_symbol)
	{
		case(X):
			my_symbol=O;
			break;
		case(O):
			my_symbol=X;
			break;
		//You can't increment to a blank!
		default:
			assert(my_symbol==X || my_symbol==O);
			break;
	}
	return my_symbol;
}
//Post a++ increment
symbol operator++(symbol & my_symbol,int)
{
	//The postfix a++ operator returns
	//the old value (before increment happened)
	symbol old_symbol=my_symbol;
	++my_symbol;
	return old_symbol;
}