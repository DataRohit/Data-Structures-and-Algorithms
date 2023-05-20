# Import typing for type hinting
from typing import *


# Function to generate the permutation and update the answer array
def solve(nums: List[int], ans: List[List[int]], index: int) -> None:
    # Base case - Check if nums still has elements
    if index >= len(nums):
        # Update the answer array
        ans.append(nums[:])

        # Return
        return

    # Loop over the nums elements
    for i in range(index, len(nums)):
        # Swap elements to generate permutation
        nums[index], nums[i] = nums[i], nums[index]

        # Recursive call for generating all other permutations
        solve(nums, ans, index + 1)

        # Back Track - swap the elements
        nums[index], nums[i] = nums[i], nums[index]


# Main function to return all the possible permutations
def permute(nums: List[int]) -> List[List[int]]:
    # Create a list to store all the possible permutations
    ans = []

    # Initialize an index to keep track of elements
    index = 0

    # Apply the solve function
    solve(nums, ans, index)

    # Return the answer array
    return ans


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


# Apply function to get the permute
ans = permute(arr)


# Print the set of all permutations
print(ans)
