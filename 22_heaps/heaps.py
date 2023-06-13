# Class for MaxHeap
class MaxHeap(object):
    # Constructor
    def __init__(self, heap=None):
        """
        Initializes a MaxHeap object.

        Parameters:
        - heap (list): Optional initial heap. Defaults to an empty list.

        Returns:
        None
        """
        # If no heap is provided, initialize an empty list
        if heap is None:
            self.heap = []

        # Otherwise, initialize the heap with the provided list
        else:
            self.heap = heap

            # Build minheap from the list
            self.buildHeap()

    # Function to return the index of the parent of a node
    def parent(self, i):
        """
        Returns the index of the parent node of the node at index i.

        Parameters:
        - i (int): Index of the node.

        Returns:
        int: Index of the parent node.
        """
        # If the node is the root
        if i == 0:
            return None

        # Otherwise, return the index of the parent node
        return (i - 1) // 2

    # Function to return the index of the left child of a node
    def leftChild(self, i):
        """
        Returns the index of the left child node of the node at index i.

        Parameters:
        - i (int): Index of the node.

        Returns:
        int: Index of the left child node.
        """
        # If the left child exists
        if 2 * i + 1 < len(self.heap):
            return 2 * i + 1

        # Otherwise, return None
        else:
            return None

    # Function to return the index of the right child of a node
    def rightChild(self, i):
        """
        Returns the index of the right child node of the node at index i.

        Parameters:
        - i (int): Index of the node.

        Returns:
        int: Index of the right child node.
        """
        # If the right child exists
        if 2 * i + 2 < len(self.heap):
            return 2 * i + 2

        # Otherwise, return None
        else:
            return None

    # Function to check if a node is a leaf
    def isLeaf(self, i):
        """
        Checks if the node at index i is a leaf node (has no children).

        Parameters:
        - i (int): Index of the node.

        Returns:
        bool: True if the node is a leaf, False otherwise.
        """
        # If the node has no children
        if 2 * i + 1 >= len(self.heap):
            return True

        # Otherwise, return False
        else:
            return False

    # Swap the elements
    def swap(self, i, j):
        """
        Swaps the elements at indices i and j in the heap.

        Parameters:
        - i (int): Index of the first element.
        - j (int): Index of the second element.

        Returns:
        None
        """
        # Swap the elements
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Function to heapify the heap
    def heapify(self, i, n=None):
        """
        Maintains the heap property by heapifying the node at index i.

        Parameters:
        - i (int): Index of the node to be heapified.
        - n (int): Optional size of the heap to be heapified. Defaults to the size of the heap.

        Returns:
        None
        """
        # Get index of left and right child of node at index i
        left = self.leftChild(i)
        right = self.rightChild(i)

        # Assume the node at index i is the largest
        largest = i

        # Initialize the size of the heap
        heap_size = n if n is not None else len(self.heap)

        # If the left child exists and is larger than the node at index i
        if (
            left is not None
            and left < heap_size
            and self.heap[left] > self.heap[largest]
        ):
            # Update the index of the largest node
            largest = left

        # If the right child exists and is larger than the node at index i
        if (
            right is not None
            and right < heap_size
            and self.heap[right] > self.heap[largest]
        ):
            # Update the index of the largest node
            largest = right

        # If the node at index i is not the largest
        if largest != i:
            # Swap the node at index i with the largest node
            self.swap(i, largest)

            # Heapify the new node at index largest
            self.heapify(largest, heap_size)

    # Function to build the heap
    def buildHeap(self):
        """
        Builds the heap by heapifying every node in the heap.

        Parameters:
        None

        Returns:
        None
        """
        # Loop from the first non-leaf node to the root node
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            # Heapify the node at index i
            self.heapify(i)

    # Function to insert a node into the heap
    def insert(self, value):
        """
        Inserts a node with the given value into the heap while maintaining the heap property.

        Parameters:
        - value: Value of the node to be inserted.

        Returns:
        None
        """
        # Insert the new node at the end of the heap
        self.heap.append(value)

        # Get the index of the new node
        i = len(self.heap) - 1

        # While the new node is not the root and is larger than its parent
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            # Swap the new node with its parent
            self.swap(i, self.parent(i))

            # Update the index of the new node
            i = self.parent(i)

    # Function to remove the maximum node (root node) from the heap
    def removeMax(self):
        """
        Removes and returns the maximum element (root) from the heap while maintaining the heap property.

        Parameters:
        None

        Returns:
        The maximum element (root) of the heap.
        """
        # If the heap is empty
        if len(self.heap) == 0:
            # Raise an IndexError
            raise IndexError("Heap is empty.")

        # Get the maximum element (root) of the heap
        root = self.heap[0]

        # Move the last element of the heap to the root
        self.heap[0] = self.heap[-1]

        # Remove the last element of the heap
        self.heap.pop()

        # Heapify the root node
        self.heapify(0)

        # Return the maximum element (root) of the heap
        return root

    # Function to remove a node at a given index from the heap
    def removeAt(self, i):
        """
        Removes the element at the given index from the heap while maintaining the heap property.

        Parameters:
        - i (int): Index of the element to be removed.

        Returns:
        None
        """
        # If the heap is empty
        if i < 0 or i >= len(self.heap):
            # Raise an IndexError
            raise IndexError("Index out of range.")

        # Replace the node to be removed with positive infinity
        self.heap[i] = float("inf")

        # While the node to be removed is not the root and is larger than its parent
        while i != 0 and self.heap[i] > self.heap[self.parent(i)]:
            # Swap the node to be removed with its parent
            self.swap(i, self.parent(i))

            # Update the index of the node to be removed
            i = self.parent(i)

        # Remove the positive infinity element
        self.removeMax()

    # Function to remove a node with a given value from the heap
    def removeValue(self, value):
        """
        Removes the first occurrence of the given value from the heap while maintaining the heap property.

        Parameters:
        - value: Value to be removed.

        Returns:
        None
        """
        # If value not found in the heap
        if value not in self.heap:
            # Raise a ValueError
            raise ValueError("Value not found in the heap.")

        # Get the index of the value to be removed
        index = self.heap.index(value)

        # Remove the value at the given index
        self.removeAt(index)


# Class for MinHeap
class MinHeap(object):
    # Constructor
    def __init__(self, heap=None):
        """
        Initializes a MinHeap object.

        Parameters:
        - heap (list): Optional initial heap. Defaults to an empty list.

        Returns:
        None
        """
        # If no heap is provided, initialize an empty list
        if heap is None:
            self.heap = []

        # Otherwise, initialize the heap with the provided list
        else:
            self.heap = heap

            # Build minheap from the list
            self.buildHeap()

    # Function to return the index of the parent of a node
    def parent(self, i):
        """
        Returns the index of the parent node of the node at index i.

        Parameters:
        - i (int): Index of the node.

        Returns:
        int: Index of the parent node.
        """
        # If the node is the root
        if i == 0:
            return None

        # Otherwise, return the index of the parent node
        return (i - 1) // 2

    # Function to return the index of the left child of a node
    def leftChild(self, i):
        """
        Returns the index of the left child node of the node at index i.

        Parameters:
        - i (int): Index of the node.

        Returns:
        int: Index of the left child node.
        """
        # If the left child exists
        if 2 * i + 1 < len(self.heap):
            return 2 * i + 1

        # Otherwise, return None
        else:
            return None

    # Function to return the index of the right child of a node
    def rightChild(self, i):
        """
        Returns the index of the right child node of the node at index i.

        Parameters:
        - i (int): Index of the node.

        Returns:
        int: Index of the right child node.
        """
        # If the right child exists
        if 2 * i + 2 < len(self.heap):
            return 2 * i + 2

        # Otherwise, return None
        else:
            return None

    # Function to check if a node is a leaf
    def isLeaf(self, i):
        """
        Checks if the node at index i is a leaf node (has no children).

        Parameters:
        - i (int): Index of the node.

        Returns:
        bool: True if the node is a leaf, False otherwise.
        """
        # If the node has no children
        if 2 * i + 1 >= len(self.heap):
            return True

        # Otherwise, return False
        else:
            return False

    # Function to swap two nodes of the heap
    def swap(self, i, j):
        """
        Swaps the elements at indices i and j in the heap.

        Parameters:
        - i (int): Index of the first element.
        - j (int): Index of the second element.

        Returns:
        None
        """
        # Swap the elements
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Function to heapify the heap
    def heapify(self, i, n=None):
        """
        Maintains the heap property by heapifying the node at index i.

        Parameters:
        - i (int): Index of the node to be heapified.
        - n (int): Optional size of the heap to be heapified. Defaults to the size of the heap.

        Returns:
        None
        """
        # Get index of left and right child of node at index i
        left = self.leftChild(i)
        right = self.rightChild(i)

        # Assume the node at index i is the smallest
        smallest = i

        # Initialize the size of the heap
        heap_size = n if n is not None else len(self.heap)

        # If the left child exists and is smaller than the node at index i
        if (
            left is not None
            and left < heap_size
            and self.heap[left] < self.heap[smallest]
        ):
            # Update the index of the smallest node
            smallest = left

        # If the right child exists and is smaller than the node at index i
        if (
            right is not None
            and right < heap_size
            and self.heap[right] < self.heap[smallest]
        ):
            # Update the index of the smallest node
            smallest = right

        # If the node at index i is not the smallest
        if smallest != i:
            # Swap the node at index i with the smallest node
            self.swap(i, smallest)

            # Heapify the new node at index smallest
            self.heapify(smallest, heap_size)

    # Function to build the heap
    def buildHeap(self):
        """
        Builds the heap by heapifying every node in the heap.

        Parameters:
        None

        Returns:
        None
        """
        # Loop from the first non-leaf node to the root node
        for i in range((len(self.heap) // 2) - 1, -1, -1):
            # Heapify the node at index i
            self.heapify(i)

    # Function to insert a node into the heap
    def insert(self, value):
        """
        Inserts a node with the given value into the heap while maintaining the heap property.

        Parameters:
        - value: Value of the node to be inserted.

        Returns:
        None
        """
        # Insert the new node at the end of the heap
        self.heap.append(value)

        # Get the index of the new node
        i = len(self.heap) - 1

        # While the new node is not the root and is smaller than its parent
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            # Swap the new node with its parent
            self.swap(i, self.parent(i))

            # Update the index of the new node
            i = self.parent(i)

    # Function to remove the minimum node (root node) from the heap
    def removeMin(self):
        """
        Removes and returns the minimum element (root) from the heap while maintaining the heap property.

        Parameters:
        None

        Returns:
        The minimum element (root) of the heap.
        """
        # If the heap is empty
        if len(self.heap) == 0:
            # Raise an IndexError
            raise IndexError("Heap is empty.")

        # Get the minimum element (root) of the heap
        root = self.heap[0]

        # Move the last element of the heap to the root
        self.heap[0] = self.heap[-1]

        # Remove the last element of the heap
        self.heap.pop()

        # Heapify the root node
        self.heapify(0)

        # Return the minimum element (root) of the heap
        return root

    # Function to remove a node at a given index from the heap
    def removeAt(self, i):
        """
        Removes the element at the given index from the heap while maintaining the heap property.

        Parameters:
        - i (int): Index of the element to be removed.

        Returns:
        None
        """
        # If the heap is empty
        if i < 0 or i >= len(self.heap):
            # Raise an IndexError
            raise IndexError("Index out of range.")

        # Replace the node to be removed with negative infinity
        self.heap[i] = float("-inf")

        # While the node to be removed is not the root and is smaller than its parent
        while i != 0 and self.heap[i] < self.heap[self.parent(i)]:
            # Swap the node to be removed with its parent
            self.swap(i, self.parent(i))

            # Update the index of the node to be removed
            i = self.parent(i)

        # Remove the negative infinity element
        self.removeMin()

    # Function to remove a node with a given value from the heap
    def removeValue(self, value):
        """
        Removes the first occurrence of the given value from the heap while maintaining the heap property.

        Parameters:
        - value: Value to be removed.

        Returns:
        None
        """
        # If value not found in the heap
        if value not in self.heap:
            # Raise a ValueError
            raise ValueError("Value not found in the heap.")

        # Get the index of the value to be removed
        index = self.heap.index(value)

        # Remove the value at the given index
        self.removeAt(index)
