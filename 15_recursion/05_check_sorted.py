# Import typing for type hinting
from typing import *


# Recusive function to check if array is sorted
def is_array_sorted(arr: List[int], idx: int) -> bool:
    # Base case
    if idx == len(arr) - 1:
        return True

    # User recurssion to get the answer
    ans = is_array_sorted(arr, idx + 1) & (arr[idx] <= arr[idx + 1])

    # Return the answer
    return ans


# User input for number of elements
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
    arr[index] = int(i)

# Call the function and check if array is sorted
print(is_array_sorted(arr, 0))
