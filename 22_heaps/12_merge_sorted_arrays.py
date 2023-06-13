# Import heapq
from heapq import *


# Function to return the merged sorted array
def mergeKSortedArrays(kArrays):
    # List to store merged elements
    merged = []

    # Initialize minheap
    minheap = []

    # Traverse over arrays
    for i, array in enumerate(kArrays):
        # Check for empty arrays
        if array:
            # Push the first element of every non-empty array in minheap
            heappush(minheap, (array[0], i))

            # Remove the pushed element from the respective list
            kArrays[i] = array[1:]

    # While heap has elements
    while minheap:
        # Get the minimum value from the heap
        element, arrayIdx = heappop(minheap)

        # Add the element to the merged list
        merged.append(element)

        # Check if there are more elements in the array
        if kArrays[arrayIdx]:
            # Push the next element to the minheap
            heappush(minheap, (kArrays[arrayIdx][0], arrayIdx))

            # Remove the pushed element from the respective list
            kArrays[arrayIdx] = kArrays[arrayIdx][1:]

    return merged


# Initialize array of arrays
kArrays = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]


# Print the merged sorted array
print(mergeKSortedArrays(kArrays))
