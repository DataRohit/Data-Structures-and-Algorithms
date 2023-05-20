# Import typing for type hinting
from typing import *


# Function to apply selection sort
def selection_sort(arr: List[int], n: int) -> List[int]:
    # Base case -> array with less than 2 elements
    if n <= 1:
        return arr

    # Find the minimum element in unsorted part
    min_idx = 0
    for i in range(1, n):
        # If current element smaller than min_idx element
        if arr[i] < arr[min_idx]:
            # Update min_idx
            min_idx = i

    # Swap the minimum element with first element
    arr[0], arr[min_idx] = arr[min_idx], arr[0]

    # Recursively sort for the remaining elements
    return [arr[0]] + selection_sort(arr[1:], n - 1)


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


# Apply the selection sort algorithm
sorted_arr = selection_sort(arr, n)

# Print the sorted array
print(*sorted_arr)
