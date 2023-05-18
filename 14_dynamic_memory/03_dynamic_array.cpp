// Import required header files
#include <bits/stdc++.h>


// Use namespace of std
using namespace std;


// Function to get the sum of all elements
int get_sum(int *arr, int n)
{
	// Initialize sum
	int sum = 0;

	// Loop over all elements
	for (int i = 0; i < n; i++)
	{
		// Update the sum
		sum += arr[i];
	}

	// Return the sum
	return sum;
}


// Declare the main function
int main()
{
	// Declare var for size of array
	int n;

	// Take user input for size of array
	cin >> n;

	// Declare dynamic array of size n
	int *arr = new int[n];

	// Take user input for array values
	for (int i = 0; i < n; i++)
	{
		// Take array values
		cin >> arr[i];
	}

	// Apply the function to get the sum of all elements
	int ans = get_sum(arr, n);

	// Print the sum
	cout << ans;
}