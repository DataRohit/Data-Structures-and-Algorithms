# Import collections to use deque
from collections import deque


def sum_of_max_and_min(nums, n, k):
    # Initialize dequeue for max element index and min element index
    max_ele_idx = deque()
    min_ele_idx = deque()

    # Process first window
    for i in range(k):
        # While last element is smaller than current element
        while max_ele_idx and nums[max_ele_idx[-1]] <= nums[i]:
            # Remove the last element from the deque
            max_ele_idx.pop()

        # Push current larger element to max element array
        max_ele_idx.append(i)

        # While last element is larger than current element
        while min_ele_idx and nums[min_ele_idx[-1]] >= nums[i]:
            # Remove the last element from the deque
            min_ele_idx.pop()

        # Push the current smaller element to deque
        min_ele_idx.append(i)

    # Initialize ans variable to store the final sum
    ans = 0

    # Traverse the remaining elements
    for i in range(k, n):
        # Calculate the ans
        ans += nums[max_ele_idx[0]] + nums[min_ele_idx[0]]

        # Move to next window

        # Loop till the element at front of max_ele_idx is not in window
        while max_ele_idx and max_ele_idx[0] <= i - k:
            # Pop the element
            max_ele_idx.popleft()

        # Loop till the element at front of min_ele_idx is not in window
        while min_ele_idx and min_ele_idx[0] <= i - k:
            # Pop the element
            min_ele_idx.popleft()

        # While last element is smaller than current element
        while max_ele_idx and nums[max_ele_idx[-1]] <= nums[i]:
            # Remove the last element from the deque
            max_ele_idx.pop()

        # Push current larger element to max element array
        max_ele_idx.append(i)

        # While last element is larger than current element
        while min_ele_idx and nums[min_ele_idx[-1]] >= nums[i]:
            # Remove the last element from the deque
            min_ele_idx.pop()

        # Push the current smaller element to deque
        min_ele_idx.append(i)

    # Calculate the ans
    ans += nums[max_ele_idx[0]] + nums[min_ele_idx[0]]

    # Return the answer
    return ans


# Take user input for number of number of elements and window size
N, K = map(int, input().split())


# Take user input for elements
elements = list(map(int, input().split()))[:N]


# Call the function and print the result
print(sum_of_max_and_min(elements, N, K))
