// Import required header files
#include <bits/stdc++.h>


// Use namespace of std
using namespace std;


// Function that accepts reference variable
void update(int &num)
{
	// Update the value using reference variable
	num++;
}


// Declare the main function
int main()
{
	// Declare and initialize i
	int i = 5;

	// Print before value
	cout << "Before\t: " << i;

	// Call the update function on i
	update(i);

	// Print after value
	cout << "\nAfter\t: " << i;
	
	// Add line break
	cout << "\n";
}