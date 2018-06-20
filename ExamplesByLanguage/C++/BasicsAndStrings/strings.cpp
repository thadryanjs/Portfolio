#include <iostream>
#include <string> // normal strings require a header

using namespace std;

int main()
{	
	// they can be declared and used as expected
	string name = "Thadryan";

	cout << name << endl;
	
	// indexing works as expected 
	cout << name[0] << endl;

	// iterating though a string.
	for ( int i = 0; i < name.length(); i++ )
	{
		cout << name[i] << endl;
	}

return 0;
}
