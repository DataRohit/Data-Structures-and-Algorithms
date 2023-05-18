# Import typing for type hinting
from typing import *


# Function to get the median of matrix
def find_median(matrix: List[List[int]]) -> int:
    # Get the sorted flattened matrix
    sorted_flattened = sorted([j for i in matrix for j in i])

    # Get length of array
    length = len(sorted_flattened)

    # If length is odd
    if length % 2 != 0:
        # Return median
        return sorted_flattened[(length // 2)]

    # If length is even
    else:
        # Return the avg of mids
        return (
            sorted_flattened[(length // 2) - 1] + sorted_flattened[(length // 2)]
        ) / 2


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


# Call the function and wave print the result
print(find_median(matrix))
