# Imports
from heapq import *


# Function to return the merged array
def mergeHeap(arr1, arr2):
    # Merge the two arrays
    arr3 = [-i for i in arr1] + [-i for i in arr2]

    # Heapify
    heapify(arr3)

    # Invert arr3 and return
    return [-i for i in arr3]


# Initialize arr1 and arr2
arr1 = [10, 5, 6, 2]
arr2 = [12, 7, 9]


# Print the merged max heap
print(mergeHeap(arr1, arr2))
