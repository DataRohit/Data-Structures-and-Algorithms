# Import typing for type hinting
from typing import *


# Function to get the kth smallest element
def kth_smallest_element(matrix: List[List[int]], k: int) -> int:
    # Get the sorted flattened matrix
    sorted_flattened = sorted([j for i in matrix for j in i])

    # Return the kth element
    return sorted_flattened[k - 1]


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


# User input for k
k = int(input())


# Call the function to get the kth min element
print(kth_smallest_element(matrix, k))
