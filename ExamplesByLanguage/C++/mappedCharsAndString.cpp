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
	
	double weight = 0;
	
	for ( int i = 0; i < peptide.length(); i++ )
	{
		weight += testMap[peptide[i]];
	}

	cout << weight << endl;

	int x, y;
	int * ptr_x, * ptr_y;

	ptr_x = &x;
	ptr_y = &y;

	*ptr_x = 25;

	cout << x << endl;

return 0;
}
	
