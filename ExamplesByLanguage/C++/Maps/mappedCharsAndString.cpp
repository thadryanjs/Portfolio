#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
	// declare map types
	map <char, double> testMap;

	// create keys/values
	testMap['A'] = 1.05;
	testMap['C'] = 1.12;
	testMap['B'] = 1.45;

	// we can now add th values together
	cout << testMap['C'] + testMap['B'] << endl;

	// use case for peptide-like sequence	
	string peptide = "ABCCBA";

	// create a variable to store the result 	
	double weight = 0;
	
	// iterate though and add paired value
	for ( int i = 0; i < peptide.length(); i++ )
	{
		weight += testMap[peptide[i]];
	}

	cout << weight << endl;

return 0;
}
	
