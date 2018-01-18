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
	char peptide[] = "ABCCBA";
	char *ptr_peptide = peptide;

	// this produces a weight of 0
	double weight = 0;
	
	while ( *ptr_peptide != '\0' )
	{
		weight += testMap[peptide[*ptr_peptide]];
		ptr_peptide++;
	}

	cout << weight << endl;


	


return 0;
}
	
