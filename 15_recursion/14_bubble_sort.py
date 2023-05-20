# Import typing for type hinting
from typing import *


# Function to apply bubble sort
def bubble_sort(arr: List[int], n: int) -> List[int]:
    # If array has less than 2 elements
    if n <= 1:
        return arr

    # Loop over the range of index
    for i in range(n - 1):
        # Compare current with next element
        if arr[i] > arr[i + 1]:
            # Swap elements
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call for reduced array
    return bubble_sort(arr[:-1], n - 1) + [arr[-1]]


# User input for number of elements
n = int(input())


# Initialize array of size n with 0
arr = arr = [0] * n


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


# Apply bubble sort algorithm
sorted_arr = bubble_sort(arr, n)


# Print the sorted array
print(*sorted_arr)
