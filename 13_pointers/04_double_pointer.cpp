// Import required header files
#include <bits/stdc++.h>


// Use namespace of std
using namespace std;


// Declare the main function
int main()
{
	// Declare and initialize variables and pointers
	int i = 5;
	int *p1 = &i;
	int **p2 = &p1;

	// Print values of i using i, p1 and p2
	cout << "i\t\t:" << i;
	cout << "\n*p1\t\t:" << *p1;
	cout << "\n**p2\t:" << **p2;

	// Print address of i using i, p1 and p2
	cout << "\n\n&i\t:" << &i;
	cout << "\np1\t:" << p1;
	cout << "\n*p2\t:" << *p2;

	// Print address of p1 using p1 and p2
	cout << "\n\n&p1\t:" << &p1;
	cout << "\np2\t:" << p2;

	// Print address of p2 using p2
	cout << "\n\n&p2\t:" << &p2;

	// Add line break
	cout << "\n";
}