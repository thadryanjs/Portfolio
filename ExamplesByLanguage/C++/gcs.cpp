#include <iostream>
#include <string>

using namespace std;

int main()
{
	string x = "THADRYAN";
	string y = "XXXXRYAN";
	string current;
	string longest;
			
	for ( int i = 0; i < x.length(); i++ ) {
		if ( x[i] == y[i] ) {
			current += x[i];
		} else {
			continue;
		}
		if ( current.length() > longest.length() ) {
			longest = current;
		}
	}
	cout << longest << endl;
return 0;
}

