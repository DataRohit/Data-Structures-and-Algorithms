# Import typing for type hinting
from typing import *


# Function to sort the array using pigeonhole sort
def pigeonhole_sort(arr: List[int]) -> None:
    # Find the minimum and maximum values
    min_val = min(arr)
    max_val = max(arr)

    # Calculate the range of values in the array
    range_val = max_val - min_val + 1

    # Create an array of pigeonholes, with one pigeonhole for each possible value
    holes = [0] * range_val

    # Put each element in its corresponding pigeonhole
    for i in arr:
        holes[i - min_val] += 1

    # Put the elements back into the array in order
    index = 0
    for i in range(range_val):
        while holes[i] > 0:
            arr[index] = i + min_val
            index += 1
            holes[i] -= 1


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


# Apply pigeonhole sort algorithm
pigeonhole_sort(arr)


# Print the sorted array
print(*arr)
