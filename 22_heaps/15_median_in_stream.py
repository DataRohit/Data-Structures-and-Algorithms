# Import heapq
from heapq import *


# Signum function
def signum(a, b):
    # Both maxHeap and minHeap have equal elements
    if a == b:
        return 0

    # MaxHeap has more elements
    elif a > b:
        return 1

    # MinHeap has more elements
    else:
        return -1


# Function to update median for stream
def callMedian(element, maxHeap, minHeap, median):
    # Get the signum value
    sig = signum(len(maxHeap), len(minHeap))

    # If both heaps have equal elements
    if sig == 0:
        # If current element is greater than median
        if element > median[0]:
            # Push the element into minHeap
            heappush(minHeap, element)

            # Update median to the top of minHeap
            median[0] = minHeap[0]

        # Else -> current element is less than or equal to median
        else:
            # Push the negative of the element into maxHeap
            heappush(maxHeap, -element)

            # Update median to the top of maxHeap (inverted)
            median[0] = -maxHeap[0]

    # If minHeap has fewer elements
    if sig == 1:
        # If current element is greater than median
        if element > median[0]:
            # Push the element into minHeap
            heappush(minHeap, element)

            # Update the median
            median[0] = (minHeap[0] + -maxHeap[0]) // 2

        # Else -> current element is less than or equal to median
        else:
            # Pop the top element from maxHeap (inverted) and push it into minHeap
            heappush(minHeap, -heappop(maxHeap))

            # Push the negative of the element into maxHeap
            heappush(maxHeap, -element)

            # Update the median
            median[0] = (minHeap[0] + -maxHeap[0]) // 2

    # If maxHeap has fewer elements
    if sig == -1:
        # If current element is greater than median
        if element > median[0]:
            # Pop the top element from minHeap and push it into maxHeap (inverted)
            heappush(maxHeap, -heappop(minHeap))

            # Push the element into minHeap
            heappush(minHeap, element)

            # Update the median
            median[0] = (minHeap[0] + -maxHeap[0]) // 2

        # Else -> current element is less than or equal to median
        else:
            # Push the negative of the element into maxHeap
            heappush(maxHeap, -element)

            # Update the median
            median[0] = (minHeap[0] + -maxHeap[0]) // 2


# Function to return the median of the elements in arr
def findMedian(arr, n):
    # Initialize a list to store medians
    ans = []

    # Initialize maxHeap and minHeap
    maxHeap, minHeap = [], []

    # Initialize median
    median = [0]

    # Traverse the arr
    for i in range(n):
        # Update the median
        callMedian(arr[i], maxHeap, minHeap, median)

        # Append the updated median to ans
        ans.append(median[0])

    # Return the answer
    return ans


# Take user input for array items
arr = list(map(int, input().split()))


# Find the median of the elements in arr
print(*findMedian(arr, len(arr)))
