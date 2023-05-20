# Import typing for type hinting
from typing import *


# Function to partition the array
def partition(arr: List[int], s: int, e: int) -> int:
    # Get the pivot element
    pivot = arr[s]

    # Variable to store count of smaller elements
    count = 0

    # Loop over array index
    for i in range(s + 1, e + 1):
        # Check if element is smaller than pivot
        if arr[i] <= pivot:
            # Update the count
            count += 1

            # Swap the element at count index with the current element
            arr[i], arr[s + count] = arr[s + count], arr[i]

    # Get the correct index of the pivot element
    pivot_index = s + count

    # Swap the element at pivot index with start
    arr[pivot_index], arr[s] = arr[s], arr[pivot_index]

    # Return the pivot index
    return pivot_index


# Function to quick sort algorithm
def quick_sort(arr: List[int], s: int, e: int) -> None:
    # Base case
    if s >= e:
        return

    # Partition the array
    p = partition(arr, s, e)

    # Sort left part
    quick_sort(arr, s, p - 1)

    # Sort right part
    quick_sort(arr, p + 1, e)


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


# Apply quick sort function
quick_sort(arr, 0, n - 1)


# Print the sorted array
print(*arr)
