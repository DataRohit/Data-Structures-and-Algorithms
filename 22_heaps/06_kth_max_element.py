# Import heapq and copy
from heapq import *
from copy import *


# Function to find the kth maximum element
def kthMaxElement(arr, k):
    # Initialize an empty heap
    heap = []

    # Push first k elements into the heap
    for i in range(k):
        heappush(heap, arr[i])

    # Iterate over the remaining elements
    for i in range(k, len(arr)):
        # If the current element is greater than the root of the heap
        if arr[i] > heap[0]:
            # Pop the root element and push the current element
            heapreplace(heap, arr[i])

    # Return the root of the heap
    return heap[0]


# Function to find the kth minimum element
def kthMinElement(arr, k):
    # Initialize an empty heap
    heap = []

    # Push first k elements into the heap
    for i in range(k):
        heappush(heap, -arr[i])

    # Iterate over the remaining elements
    for i in range(k, len(arr)):
        # If the current element is less than the root of the heap
        if arr[i] < -heap[0]:
            # Pop the root element and push the current element
            heapreplace(heap, -arr[i])

    # Return the root of the heap
    return -heap[0]


# Take user input for the array
arr = list(map(int, input().split()))


# Take user input for the value of k
k = int(input())


# Print the kth maximum element
print(kthMaxElement(arr, k))


# Print the kth minimum element
print(kthMinElement(arr, k))
