// Import required header files
#include <bits/stdc++.h>


// Use namespace of std
using namespace std;


// Declare the main function
int main()
{
	// Declare and initialize array
	int arr[10] = {0, 10, 20, 30, 40, 50, 60, 70, 80, 90};

	// Print the address of first memory block
	cout << "arr\t\t:" << arr;

	// Print the address of element in array using index
	cout << "\n&arr[0]\t:" << &arr[0];

	// Print the address of element in array using index
	cout << "\n&arr[5]\t:" << &arr[5];

	// Print the value of element in array using pointer
	cout << "\n\n*arr\t\t:" << *arr;

	// Print the value of element in array using pointer
	cout << "\n*(arr + 5)\t:" << *(arr + 5);

	// Initialize index
	int i = 8;

	// Print the i value
	cout << "\n\ni\t\t\t:" << 8;

	// Access value of element using index
	cout << "\ni[arr]\t\t:" << i[arr];

	// Access value of element using pointer
	cout << "\n*(i + arr)\t:" << *(i + arr);

	// Initialize a pointer storing address to first array element
	int *p = &arr[0];

	// Print pointer values
	cout << "\n\nsizeof(arr)\t:" << sizeof(arr);
	cout << "\nsizeof(p)\t:" << sizeof(p);
	cout << "\nsizeof(*p)\t:" << sizeof(*p);
	cout << "\nsizeof(&p)\t:" << sizeof(&p);

	// Add line break
	cout << "\n";
}