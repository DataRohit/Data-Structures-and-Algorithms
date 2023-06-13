# Import heap classes
from heaps import MaxHeap, MinHeap


# Heapsort algorithm -> MaxHeap
def heapsortAscending(arr):
    # Initialize a max heap.
    heap = MaxHeap(arr)

    # Traverse the heap in reverse order.
    for i in range(len(arr) - 1, 0, -1):
        # Swap the first and last elements.
        heap.swap(0, i)

        # Heapify the heap.
        heap.heapify(0, i)


# Heapsort algorithm -> MinHeap
def heapsortDescending(arr):
    # Initialize a min heap.
    heap = MinHeap(arr)

    # Traverse the heap in reverse order.
    for i in range(len(arr) - 1, 0, -1):
        # Swap the first and last elements.
        heap.swap(0, i)

        # Heapify the heap.
        heap.heapify(0, i)


# Function to test heapsortAscending.
def testHeapsortAscending():
    # Initialize an array.
    arr = [7, 5, 3, 1, 2, 4, 6]

    # Sort the array.
    heapsortAscending(arr)

    # Assert the array is sorted.
    assert arr == [1, 2, 3, 4, 5, 6, 7]

    # Print success message.
    print("HeapsortAscending works!")


# Function to test heapsortDescending.
def testHeapsortDescending():
    # Initialize an array.
    arr = [7, 5, 3, 1, 2, 4, 6]

    # Sort the array.
    heapsortDescending(arr)

    # Assert the array is sorted.
    assert arr == [7, 6, 5, 4, 3, 2, 1]

    # Print success message.
    print("HeapsortDescending works!")


# Test the heap sort algorithm.
testHeapsortAscending()
testHeapsortDescending()
