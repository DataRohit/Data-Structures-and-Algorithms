// Import required header files
#include <bits/stdc++.h>


// Use namespace of std
using namespace std;


// Declare the main function
int main()
{
	// Declare vars for rows and cols
	int m, n;

	// Take user input for m and n
	cin >> m >> n;

	// Create a dynamic array of m to store array of size n
	int **arr = new int *[m];

	// Create array of size n for each rows
	for (int i = 0; i < m; i++)
	{
		// Initialize array
		arr[i] = new int[n];
	}

	// Take user input for number of rows and cols
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> arr[i][j];
		}
	}

	// Add a line break
	cout << "\n";

	// Print the stored elements
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << arr[i][j] << " ";
		}

		// Add line break for row
		cout << "\n";
	}

	// Release individual arrays
	for (int i = 0; i < m; i++)
	{
		free(arr[i]);
	}

	// Release the main array
	free(arr);
}