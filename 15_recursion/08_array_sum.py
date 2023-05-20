# Import typing for type hinting
from typing import *


# Recursive function to get the sum of elements
def get_array_sum(arr: List[int], idx: int) -> int:
    # If length of array is 0
    if len(arr) == 0:
        return 0

    # If length of array is 1
    if len(arr) == 1:
        return arr[0]

    # Base case -> index of last element
    if idx == len(arr) - 1:
        return arr[idx]

    # Calculate the answer
    ans = arr[idx] + get_array_sum(arr, idx + 1)

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
print(get_array_sum(arr, 0))
