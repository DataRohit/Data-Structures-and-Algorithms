# Import typing for type hinting
from typing import *


# Function to search target in matrix
def search_matrix(matrix: List[List[int]], target: [int]) -> bool:
    # Get the row and col count of matrix
    nRows, nCols = len(matrix), len(matrix[0])

    # Initialize start pointer -> start from top right corner
    rowIdx = 0
    colIdx = nCols - 1

    # Loop till rows and cols are traversed
    while rowIdx < nRows and colIdx >= 0:
        # Get the current element
        element = matrix[rowIdx][colIdx]

        # If target and current element are equal
        if target == element:
            # Element found
            return True

        # If target > current element
        elif target > element:
            # Increment the row index
            rowIdx += 1

        # If target < current lement
        else:
            # Decrement the col index
            colIdx -= 1

    # Element not found
    return False


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


# Take user input for target
target = int(input())


# Call the function and wave print the result
print(search_matrix(matrix, target))
