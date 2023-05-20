# Import typing for type hinting
from typing import *


# Function to search for key in array
def linear_search(array: List[int], key: int, idx: int) -> bool:
    # Base Case -> if array is empty
    if len(array) == 0:
        return False

    # Compare the element with key
    if idx == len(array) - 1:
        return array[idx] == key

    # Search key in smaller array using recurssion and return answer
    return (arr[idx] == key) or (linear_search(arr, key, idx + 1))


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
print(linear_search(arr, key, 0))
