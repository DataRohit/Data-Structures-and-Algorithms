# Import heapq
from heapq import *


# Function to find the size of smallest range including at least one element from each of the k lists
def findSmallestRange(lists, k, n):
    # Initialize max and min value
    minVal, maxVal = float("inf"), float("-inf")

    # Initialize heap
    heap = []

    # Traverse the lists
    for i in range(k):
        # Add the first element of each list to the heap
        heappush(heap, (lists[i][0], i))

        # Update the max value and min value
        maxVal = max(maxVal, lists[i][0])
        minVal = min(minVal, lists[i][0])

        # Remove the first element from the list
        lists[i].pop(0)

    # Initialize the start and end points of the range
    start, end = minVal, maxVal

    # Loop until the heap is not empty
    while heap:
        # Get the minimum element from the heap
        val, idx = heappop(heap)

        # Update minVal if new min is found
        minVal = val

        # Check if new range is smaller than the current range
        if maxVal - minVal < end - start:
            # Update the start and end points of the range
            start, end = minVal, maxVal

        # Check if the list is not empty
        if lists[idx]:
            # Update max value
            maxVal = max(maxVal, lists[idx][0])

            # Push the next element in the heap
            heappush(heap, (lists[idx][0], idx))

            # Remove the first element from the list
            lists[idx].pop(0)

        # If any list is exhausted, break the loop
        else:
            break

    # Return the size of smallest range
    return end - start + 1


# Taker user input for number of lists and number of elements in each list
k, n = map(int, input().split())


# Take user input for k lists of n elements each
lists = []  # Main list to store all lists
for i in range(k):  # Loop for k lists
    lists.append(list(map(int, input().split())))  # Take user input for each list
    lists[i].sort()  # Sort each list


# Print the size of smallest range
print(findSmallestRange(lists, k, n))
