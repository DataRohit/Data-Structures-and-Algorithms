# Import typing for type hinting
from typing import *


# Function for spiral traversal of matrix
def spiral_order(matrix: List[List[int]], n: int, m: int) -> List[int]:
    # Create a answer list
    ans = []

    # Initialize total count of total elements
    total_elements = n * m

    # Initialize count of elements traversed
    count_elements = 0

    # Initialize start and end row
    # Initialize start and end col
    start_row, start_col = 0, 0
    end_row, end_col = n - 1, m - 1

    # Loop till elements are left to be traversed
    while count_elements < total_elements:
        # Check if element count < total elements
        if count_elements < total_elements:
            # Start row -> left to right
            for i in range(start_col, end_col + 1):
                # Push the elemnt to answer list
                ans.append(matrix[start_row][i])

                # Update the count of elements traversed
                count_elements += 1
            # Increment the start row counter
            start_row += 1

        # Check if element count < total elements
        if count_elements < total_elements:
            # End col -> top to bottom
            for i in range(start_row, end_row + 1):
                # Push the elemnt to answer list
                ans.append(matrix[i][end_col])

                # Update the count of elements traversed
                count_elements += 1
            # Decrement the end col counter
            end_col -= 1

        # Check if element count < total elements
        if count_elements < total_elements:
            # End row -> right to left
            for i in range(end_col, start_col - 1, -1):
                # Push the elemnt to answer list
                ans.append(matrix[end_row][i])

                # Update the count of elements traversed
                count_elements += 1
            # Decrement the end row counter
            end_row -= 1

        # Check if element count < total elements
        if count_elements < total_elements:
            # Start col -> bottom to top
            for i in range(end_row, start_row - 1, -1):
                # Push the elemnt to answer list
                ans.append(matrix[i][start_col])

                # Update the count of elements traversed
                count_elements += 1
            # Increment the start row counter
            start_col += 1

    # Return the answer array
    return ans


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
print(spiral_order(matrix, n, m))
