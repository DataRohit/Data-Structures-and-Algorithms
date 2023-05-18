# Import typing for type hinting
from typing import *


# Function to get the common elements
def get_common_elements(matrix: List[List[int]]) -> List[int]:
    # Intialize dictionary to store element and count
    count_dict = {}

    # Loop over elements
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Check if element already in dict and repeated
            if matrix[i][j] in count_dict.keys() and count_dict[matrix[i][j]] == i:
                # Update the count
                count_dict[matrix[i][j]] += 1

            # If element is not in dict
            else:
                # Add element to dictionary
                count_dict[matrix[i][j]] = 1

    # Sort the count dict by value
    count_dict = dict(
        sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
    )

    # Initialize the answer list
    ans_list = []

    # List to store the elements
    for key, value in zip(count_dict.keys(), count_dict.values()):
        # Check if element in every row
        if value == len(matrix):
            # Add element to answer list
            ans_list.append(key)

        # Else the answer list
        else:
            return ans_list


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
print(*get_common_elements(matrix))
