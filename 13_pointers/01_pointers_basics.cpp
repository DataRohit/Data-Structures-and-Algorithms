// Import required header files
#include <bits/stdc++.h>


// Use namespace of std
using namespace std;


// Declare the main function
int main()
{
	// Declare and initialize a variable
	int num = 5;

	// Print the value of num
	cout << "num\t\t\t: " << num;

	// Print the address of num
	cout << "\n&num\t\t: " << &num;

	// Print the size of number
	cout <<  "\nsizeof(num)\t: " << sizeof(num);

	// Declare and initialize a pointer
	int *p = &num;

	// Print data in pointer
	cout << "\n\np\t\t\t: " << p;

	// Print data at the address store in pointer
	cout << "\n*p\t\t\t: " << *p;

	// Print the size of pointer
	// Size of pointer is double the size of the type
	cout <<  "\nsizeof(p)\t: " << sizeof(p);

	// Copy pointer p to pointer q
	int *q = p;

	// Print the value of p and 1
	cout << "\n\np\t: " << p;
	cout << "\nq\t: " << q;

	// Print the value of *p and *q
	cout << "\n\n*p\t: " << *p;
	cout << "\n*q\t: " << *q;

	// Increment n
	num++;

	// Print num, *p and *q
	cout << "\n\nnum\t:" << num;
	cout << "\n*p\t:" << *p;
	cout << "\n*q\t:" << *q;

	// Increment n using p
	(*p)++;

	// Print num, *p and *q
	cout << "\n\nnum\t:" << num;
	cout << "\n*p\t:" << *p;
	cout << "\n*q\t:" << *q;

	// Increment n using q
	(*q)++;

	// Print num, *p and *q
	cout << "\n\nnum\t:" << num;
	cout << "\n*p\t:" << *p;
	cout << "\n*q\t:" << *q;

	// Add line break
	cout << "\n";
}