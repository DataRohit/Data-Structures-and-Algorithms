// Import required header files
#include <bits/stdc++.h>


// Use namespace of std
using namespace std;


// Function to print the value of var and ref var
void print_value(int i, int j)
{
	// Print value of i
	cout << "\n\ni\t: " << i;

	// Print value of j
	cout << "\nj\t: " << j;
}


// Declare the main function
int main()
{
	// Declare and initialize i
	int i = 5;

	// Print value of i
	cout << "i\t: " << i;

	// Create a reference variable j for i
	int &j = i;

	// Print value of j
	cout << "\nj\t: " << j;

	// Update value using i
	cout << "\n\n++i\t: " << ++i;

	// Print values
	print_value(i, j);

	// Update value using j
	cout << "\n\n++j\t: " << ++j;

	// Print values
	print_value(i, j);

	// Add line break
	cout << "\n";
}