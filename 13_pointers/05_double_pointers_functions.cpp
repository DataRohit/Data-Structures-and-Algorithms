// Import required header files
#include <bits/stdc++.h>


// Use namespace of std
using namespace std;


// Function to update value using double pointer
void update(int **ptr)
{
	// Update value of ptr
	ptr = ptr + 1;

	// // Update value of *ptr
	// *ptr = *ptr + 1;

	// // Update value of **ptr
	// **ptr = **ptr + 1;
}


// Declare the main function
int main()
{
	// Declare and initialize variables and pointers
	int i = 5;
	int *p1 = &i;
	int **p2 = &p1;

	// Print value of p2, *p2 and **p2 before update
	cout << "Before Update";
	cout << "\np2\t\t:" << p2;
	cout << "\n*p2\t\t:" << *p2;
	cout << "\n**p2\t:" << **p2;

	// Use function to update values
	update(p2);

	// Print values of p2, *p2 and **p2 after update
	cout << "\n\nAfter Update";
	cout << "\np2\t\t:" << p2;
	cout << "\n*p2\t\t:" << *p2;
	cout << "\n**p2\t:" << **p2;

	// Add line break
	cout << "\n";
}