class CircularQueue(object):
    """
    Class to implement a circular queue data structure.
    """

    def __init__(self, n):
        """
        Initialize a circular queue with a given size.

        Args:
            n (int): The size of the circular queue.
        """
        self.q = [None] * n
        self.n = n
        self.front_idx = -1
        self.rear_idx = -1

    def enqueue(self, value):
        """
        Add an element to the circular queue.

        Args:
            value (object): The element to be added to the circular queue.

        Returns:
            bool: True if the element is successfully added, False if the circular queue is full and the element cannot be added.
        """
        if (self.rear_idx + 1) % self.n == self.front_idx:
            # Queue is full, element cannot be inserted
            return False

        if self.front_idx == -1:
            # Inserting first element
            self.front_idx = 0
            self.rear_idx = 0
        else:
            # Inserting other elements
            self.rear_idx = (self.rear_idx + 1) % self.n

        # Insert element
        self.q[self.rear_idx] = value

        return True

    def dequeue(self):
        """
        Remove and return an element from the circular queue.

        Returns:
            object: The element removed from the circular queue.
            -1: If the circular queue is empty.
        """
        if self.front_idx == -1:
            # Queue is empty, no element to remove
            return -1

        dequeue_ele = self.q[self.front_idx]

        self.q[self.front_idx] = None

        if self.front_idx == self.rear_idx:
            # Removing the only element from the queue
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.n

        return dequeue_ele


# Declare a queue
queue = CircularQueue(5)


# Add items to the queue
queue.enqueue(10)
queue.enqueue(12)
queue.enqueue(14)
queue.enqueue(16)
queue.enqueue(18)


# Print the queue
print(queue.q)


# Remove items from the queue
print(queue.dequeue())


# Print the queue
print(queue.q)


# Remove items from the queue
print(queue.dequeue())


# Print the queue
print(queue.q)


# Add items to the queue
print(queue.enqueue(20))


# Print the queue
print(queue.q)


# Add items to the queue
print(queue.enqueue(22))


# Print the queue
print(queue.q)


# Add items to the queue
print(queue.enqueue(24))


# Print the queue
print(queue.q)
