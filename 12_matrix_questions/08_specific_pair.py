# Import typing for type hinting
from typing import *


# Function to get the maximum value
def max_value(mat: List[List[int]]) -> int:
    # Find the size of the matrix
    n = len(mat)

    # Initialize the maximum difference to 0
    max_val = 0

    # Consider all possible pairs
    # mat[a][b] and mat[d][e]
    for a in range(n - 1):
        for b in range(n - 1):
            for d in range(a + 1, n):
                for e in range(b + 1, n):
                    if max_val < int(mat[d][e] - mat[a][b]):
                        max_val = int(mat[d][e] - mat[a][b])

    # Return the maximum difference
    return max_val


# Take user input for rows and columsn
n, m = map(int, input().split())


# Initialize the matrix
matrix = [0] * n


# Loop for rows
for j in range(n):
    # Initialize array of size m with 0
    arr = [0] * m

    # Array input
    arr_input = input()

    # Loop over index
    for index, k in enumerate(arr_input.split()):
        # Break if index >= n
        if index >= m:
            # Break out of loop
            break

        # Get user input
        arr[index] = int(k)

    # Add row to matrix
    matrix[j] = arr


# Call the function to get the max sum
print(max_value(matrix))
