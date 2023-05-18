# Import typing for type hinting
from typing import *


# Finds the largest rectangle in a histogram of heights.
def largest_rectangle_histogram(heights):
    # Create an empty stack
    stack = []

    # Initialize the maximum area to 0
    max_area = 0

    # Iterate over each height in the histogram, including a final "dummy" height of 0
    for i, h in enumerate(heights + [0]):
        # If the current height is less than the height at the top of the stack,
        # pop elements from the stack and compute the area of the rectangle
        while stack and h < heights[stack[-1]]:
            # Pop the index of the height at the top of the stack
            prev_height = heights[stack.pop()]

            # Calculate the width of the rectangle as the distance between the current index and the previous index in the stack
            # or the full width of the histogram if the stack is empty
            width = i if not stack else i - stack[-1] - 1

            # Calculate the area of the rectangle and update the maximum area if necessary
            max_area = max(max_area, prev_height * width)

        # Push the index of the current height onto the stack
        stack.append(i)

    # Return the maximum area
    return max_area


# Finds the largest rectangle in a 2D array of 1s and 0s.
def largest_rectangle(matrix):
    # If the matrix is empty, return 0
    if not matrix:
        return 0

    # Get the number of rows and columns in the matrix
    m, n = len(matrix), len(matrix[0])

    # Create a list of heights initialized to zero
    heights = [0] * n

    # Initialize the maximum area to 0
    max_area = 0

    # Iterate over each row in the matrix
    for i in range(m):
        # Iterate over each column in the row
        for j in range(n):
            # If the cell contains a 1, increment the height of the corresponding bar in the histogram
            if matrix[i][j] == 1:
                heights[j] += 1
            # Otherwise, reset the height of the corresponding bar to zero
            else:
                heights[j] = 0

        # Find the area of the largest rectangle in the histogram of heights and update the maximum area
        max_area = max(max_area, largest_rectangle_histogram(heights))

    # Return the maximum area
    return max_area


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
print(largest_rectangle(matrix))
