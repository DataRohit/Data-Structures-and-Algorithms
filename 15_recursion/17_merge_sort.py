# Import typing for type hinting
from typing import *


def merge(arr: List[int], left: int, right: int) -> None:
    """
    Helper function to merge two sorted subarrays of the original list.

    Args:
        arr (list): Original list to be sorted.
        left (list): First sorted subarray.
        right (list): Second sorted subarray.
    """

    left_index = 0
    right_index = 0
    arr_index = 0

    # Compare elements from both subarrays and place the smaller element into the original list.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            arr[arr_index] = left[left_index]
            left_index += 1
        else:
            arr[arr_index] = right[right_index]
            right_index += 1
        arr_index += 1

    # Place the remaining elements from the non-empty subarray into the original list.
    while left_index < len(left):
        arr[arr_index] = left[left_index]
        left_index += 1
        arr_index += 1

    while right_index < len(right):
        arr[arr_index] = right[right_index]
        right_index += 1
        arr_index += 1


def merge_sort(arr: List[int]) -> None:
    """
    Optimized Merge Sort algorithm implementation (in-place).

    Args:
        arr (list): Input list to be sorted.
    """

    # Base case: If the input list has only one element, it is already sorted.
    if len(arr) <= 1:
        return

    # Splitting the input list into two halves.
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively calling merge_sort on both halves to sort them.
    merge_sort(left_half)
    merge_sort(right_half)

    # Merging the sorted halves back into the original list.
    merge(arr, left_half, right_half)


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


# Apply merge sort function
merge_sort(arr)


# Print the sorted array
print(*arr)
