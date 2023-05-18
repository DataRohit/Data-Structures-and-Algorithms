# Import typing for type hinting
from typing import *


# Function to apply binary search to matrix
def search_matrix(matrix: List[List[int]], target: int) -> bool:
    # Get the rows and cols
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize the start and end pointer
    start = 0
    end = rows * cols - 1

    # Loop till start <= end
    while start <= end:
        # Calculate the mid index
        mid = start + (end - start) // 2

        # Get the mid index element
        # mid / cols -> row index
        # mid % cols -> col index
        element = matrix[mid // cols][mid % cols]

        # If mid element is target
        if element == target:
            # Element found
            return True

        # Target > mid element
        elif target > element:
            # Search in right half
            start = mid + 1

        # Target < mid element
        else:
            # Search in left half
            end = mid - 1

    # If element is not found
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
