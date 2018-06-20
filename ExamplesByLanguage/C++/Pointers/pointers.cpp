#include <iostream>

using namespace std;

int main()
{
	// declaration
	int x, y;
        int *ptr_x, *ptr_y;

	// these pointers are whatever is at x an y
	// which is currently nothing 
       	ptr_x = &x;
        ptr_y = &y;

	// THESES ARE THE SAME POINTERS
	// They are just derefferenced so we can do shit to them 
        *ptr_x = 25;
	*ptr_y = 30;

	
	cout << x << endl;
	cout << y << endl;
	cout << x + y << endl;

return 0;
}
