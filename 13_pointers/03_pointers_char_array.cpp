// Import required header files
#include <bits/stdc++.h>


// Use namespace of std
using namespace std;


// Declare the main function
int main()
{
	// Declare and initialize character array
	char ch[6] = "abcde";

	// Print data stored in ch
	cout << "ch\t:" << ch;

	// Initialize pointer with first character address
	char *p = &ch[0];

	// Print the value stored in pointer
	cout << "\np\t:" << p;

	// Declare and initialize a character
	char temp = 'z';

	// Print data stored in temp
	cout << "\n\ntemp\t:" << temp;

	// Initialize a pointer
	char *c = &temp;

	// Print the data store in c
	cout << "\nc\t\t:" << c;

	// Add line break
	cout << "\n";
}