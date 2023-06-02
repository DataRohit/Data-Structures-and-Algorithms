class Queue(object):
    """Class to implement queue data structure."""

    def __init__(self):
        """Initialize an empty queue."""
        self.queue = []

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.queue == []

    def size(self):
        """
        Get the size of the queue.

        Returns:
            int: The number of elements in the queue.
        """
        return len(self.queue)

    def front(self):
        """
        Get the front element of the queue.

        Returns:
            object: The front element of the queue.
            -1: If the queue is empty.
        """
        if self.is_empty():
            return -1
        return self.queue[0]

    def rear(self):
        """
        Get the rear element of the queue.

        Returns:
            object: The rear element of the queue.
            -1: If the queue is empty.
        """
        if self.is_empty():
            return -1
        return self.queue[-1]

    def enqueue(self, value):
        """
        Add an element to the queue.

        Args:
            value (object): The element to be added to the queue.
        """
        self.queue.append(value)

    def dequeue(self):
        """
        Remove and return an element from the queue.

        Returns:
            object: The element removed from the queue.
            -1: If the queue is empty.
        """
        if self.is_empty():
            return -1
        return self.queue.pop(0)

    def print_queue(self):
        """Print the elements in the queue."""
        print(self.queue)


# Declare a queue
queue = Queue()


# Check queue is empty or not
print(queue.is_empty())


# Add items to the queue
queue.enqueue(10)
queue.enqueue(12)
queue.enqueue(14)
queue.enqueue(16)
queue.enqueue(18)


# Print the queue
queue.print_queue()


# Print front and rear element of the queue
print(queue.front())
print(queue.rear())


# Print size of the queue
print(queue.size())


# Remove items from the queue
print(queue.dequeue())


# Print the queue
queue.print_queue()


# Print front and rear element of the queue
print(queue.front())
print(queue.rear())


# Print size of the queue
print(queue.size())
