# Import heapq
from heapq import *


# Function to return kth largest sum
def getKthLargest(nums, k):
    # Initialize an empty heap
    heap = []

    # Traverse for length of array
    for i in range(len(nums)):
        # Initialize current sum
        curr_sum = 0

        # Traverse for subarray
        for j in range(i, len(nums)):
            # Increment the sum of subarray
            curr_sum += nums[j]

            # If kth sum not reached
            if len(heap) < k:
                # Add the sum to heap
                heappush(heap, curr_sum)

            # If kth sum reached
            else:
                # If curr sum is potential kth largest sum
                if curr_sum > heap[0]:
                    # Push the current element to the heap and pop the heap
                    heappushpop(heap, curr_sum)

    # Return the top of the heap
    return heap[0]


# Initialize array
arr = [5, 4, -8, 6]


# Function call
print(getKthLargest(arr, 10))
