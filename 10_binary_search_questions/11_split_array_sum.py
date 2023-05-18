# Import requred modules
from typing import *


# Define the helper function to check if the given sum is valid or not
def is_valid_sum(target_sum: int) -> bool:
    """
    This helper function checks if the given target_sum is valid or not
    """

    # Initialize the subarray sum and subarray count
    subarray_sum, subarray_count = 0, 1

    # Loop over nums array
    for num in nums:
        # Add num to subarray sum
        subarray_sum += num

        # Check if subarray sum exceed the target sum
        if subarray_sum > target_sum:
            # Move to next sub array by setting current element to subarray sum
            subarray_sum = num

            # Increment the subarray count
            subarray_count += 1

        # If subarrays > k used
        if subarray_count > k:
            # Return false
            return False

    # Target sum is feasible
    return True


def split_array(nums: List[int], k: int) -> int:
    """
    This function takes an integer array 'nums' and an integer 'k' and returns the minimized largest sum of the split.
    """

    # Define the search range
    left, right = max(nums), sum(nums)

    # Binary search for the minimum possible largest sum
    while left < right:
        # Get the mid
        mid = left + (right - left) // 2

        # Check if mid is the valid sum
        if is_valid_sum(mid):
            # Search for smaller sum in left half
            right = mid
        else:
            # Search for larger sum in right half
            left = mid + 1

    # Retrun the final sum
    return left


# User input for number of elements
# User input for k
n, k = map(int, input().split())


# Initialize array of size n with 0
nums = [0] * n


# Array input
arr_input = input()


# Loop over index
for index, i in enumerate(arr_input.split()):
    # Break if index >= n
    if index >= n:
        # Break out of loop
        break

    # Get user input
    nums[index] = int(i)


# Print the minimum possible largest sum
print(split_array(nums, k))
