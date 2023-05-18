# Import type hinting
from typing import *


# Function to reverse the array inplace
def reverse_string(s: List[str]) -> None:
    # User array indexing to reverse the array
    s[:] = s[::-1]


# Take user input for number of elements
n = int(input())


# Initialize array of size n with 0
arr = [0] * n


# Array input
arr_input = input()


# Loop over index
for index, i in enumerate(arr_input.split()):
    # Break if index >= n
    if index >= n:
        # Break out of loop
        break

    # Get user input
    arr[index] = i


# Reverse the array
reverse_string(arr)

# Print the reversed string
print(arr)
