# Import typing for type hinting
from typing import *


# Function to search for key in array
def binary_search(array: List[int], start: int, end: int, key: int) -> bool:
    # Base case element not found
    if start > end:
        return False

    # Calculate mid
    mid = start + (end - start) // 2

    # Base case element found at mid
    if array[mid] == key:
        return True

    # Search in left half
    if key < array[mid]:
        return binary_search(array, start, mid - 1, key)

    # Search in right half
    else:
        return binary_search(array, mid + 1, end, key)


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


# Take user input for key
key = int(input())


# Call the function
print(binary_search(arr, 0, len(arr) - 1, key))
