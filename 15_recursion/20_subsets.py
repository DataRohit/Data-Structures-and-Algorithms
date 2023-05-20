# Import typing for type hinting
from typing import *


# Function to generate subset
def generate_subsets(nums: List[int], current_subset: List[int], subsets: List[List[int]]) -> None:
    # Base case: if nums is empty, add the current_subset to the subsets list
    if not nums:
        subsets.append(current_subset)
        return

    # Recursive case: for each element in nums, generate subsets including and excluding the current element
    generate_subsets(nums[1:], current_subset + [nums[0]], subsets)  # Include the current element
    generate_subsets(nums[1:], current_subset, subsets)  # Exclude the current element


# Main function to return all the subsets
def subsets(nums: List[int]) -> List[List[int]]:
    # List to store the subsets
    subsets = []

    # Generate all subsets
    generate_subsets(nums, [], subsets)

    # Return power set
    return subsets


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


# Apply function to get the subsets
ans = subsets(arr)


# Print the powerset array
print(ans)
