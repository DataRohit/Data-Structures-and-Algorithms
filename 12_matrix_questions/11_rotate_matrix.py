# Import typing for type hinting
from typing import *


# Function to rotate the matrix
def rotate_matrix(matrix: List[List[int]]):
    # Find the size of the matrix
    n = len(matrix)

    # Traverse each layer of the matrix, starting from the outermost layer
    for layer in range(n // 2):
        # Index of the first element in the current layer
        first = layer

        # Index of the last element in the current layer
        last = n - 1 - layer

        # Traverse the elements in the current layer, except for the last element
        for i in range(first, last):
            # Calculate the offsets to access the four elements to be rotated
            offset = i - first

            top = matrix[first][i]
            right = matrix[i][last]
            bottom = matrix[last][last - offset]
            left = matrix[last - offset][first]

            # Rotate the four elements in-place
            matrix[first][i] = left
            matrix[i][last] = top
            matrix[last][last - offset] = right
            matrix[last - offset][first] = bottom


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


# Call the function to get the list of common elements
rotate_matrix(matrix)


# Print the matrix
for i in matrix:
    print(i)
