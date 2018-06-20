#include <iostream>
#include <vector>
#include <string>
#include <set>

int main()
{
	// initial string
	std::string name = "THADRYAN";

	// create a character set
	std::set <char> uniq(name.begin(), name.end());

	// create iterator obeject of appropriate type from set namespace
	std::set<char>::iterator iter;
	for ( iter = uniq.begin(); iter != uniq.end(); ++iter ) {		
		std::cout << *iter << std::endl; // defer as it is an object
	}

return 0;
}
