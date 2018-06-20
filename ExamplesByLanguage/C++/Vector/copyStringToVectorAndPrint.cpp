#include <iostream>
#include <vector> // use of vectors requires a header
#include <string>

int main()
{
	std::string peptide1 = "PEPTIDEONE";
	std::string peptide2 = "PEPTIDETWO";

	// declare an empty vector with tye
	std::vector<char> empty_vector;

	// declare standard vector with type and copy of string
	std::vector<char> residue_list(peptide1.begin(), peptide1.end());

	// print in the way one would expect 
	for ( int i = 0; i < peptide1.length(); i++ ) {
		std::cout << residue_list[i] << std::endl;
	}

return 0;
}
