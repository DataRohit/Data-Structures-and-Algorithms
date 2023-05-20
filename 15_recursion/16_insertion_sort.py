# Import typing for type hinting
from typing import *


# Function to apply insertion sort
def insertion_sort(arr: List[int], n: int) -> None:
    # Base case if array has less than 2 elements
    if n <= 1:
        return

    # Sort the first n - 1 elements
    insertion_sort(arr, n - 1)

    # Insert the last element at its correst position in sorted part
    last = arr[n - 1]
    j = n - 2

    # Loop to find the correct position
    while j >= 0 and arr[j] > last:
        # Move elements one index forward
        arr[j + 1] = arr[j]

        # Go to previon position
        j = j - 1

    # Put the last element in the empty place created
    arr[j + 1] = last


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


# Apply insertion sort function
insertion_sort(arr, n)


# Print the sorted array
print(*arr)
