#include <iostream>
#include <vector>
#include <string>

int main()
{	
	// initialize vector with chars (SINGLE QUOTES)
	std::vector <char> letters = {'T', 'H', 'A', 'D', 'R', 'Y', 'A', 'N'};

	// vectors have a size() not length()
	for ( int i = 0; i < letters.size(); i++ ) {
		std::cout << letters[i] << std::endl;
	}
	
	// other method of iteration auto thing at address
	for ( auto & letter : letters ) {
		std::cout << letter << std::endl;
	}
	
return 0;
}
