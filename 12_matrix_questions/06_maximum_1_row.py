# Import typing for type hinting
from typing import *


# Function to get row index with maximum 1s
def row_with_max_1s(matrix: List[List[int]]) -> int:
    # Set max 1 row index
    max_row_index = 0

    # Intialize var for storing the sum of row
    max_row_sum = sum(matrix[0])

    # Loop over remaining rows
    for i in range(1, len(matrix)):
        # Check if current row sum > max row sum
        if sum(matrix[i]) > max_row_sum:
            # Set max row index to current row
            max_row_index = i

            # Update the max row sum
            max_row_sum = sum(matrix[i])

    # Return the max row index
    return max_row_index


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


# Call the function to get the row index with maximum 1
print(row_with_max_1s(matrix))
