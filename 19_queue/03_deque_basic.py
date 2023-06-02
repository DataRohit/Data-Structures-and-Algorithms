class Deque(object):
    def __init__(self):
        """Initialize an empty deque."""
        self.deque = []

    def is_empty(self):
        """
        Check if the deque is empty.

        Returns:
            bool: True if the deque is empty, False otherwise.
        """
        return self.deque == []

    def size(self):
        """
        Get the size of the deque.

        Returns:
            int: The number of elements in the deque.
        """
        return len(self.deque)

    def front(self):
        """
        Get the front element of the deque.

        Returns:
            object: The front element of the deque.
            -1: If the deque is empty.
        """
        if self.is_empty():
            return -1
        return self.deque[0]

    def rear(self):
        """
        Get the rear element of the deque.

        Returns:
            object: The rear element of the deque.
            -1: If the deque is empty.
        """
        if self.is_empty():
            return -1
        return self.deque[-1]

    def push_front(self, value):
        """
        Add an element to the front of the deque.

        Args:
            value (object): The element to be added to the front of the deque.
        """
        self.deque.insert(0, value)

    def push_rear(self, value):
        """
        Add an element to the rear of the deque.

        Args:
            value (object): The element to be added to the rear of the deque.
        """
        self.deque.append(value)

    def pop_front(self):
        """
        Remove and return an element from the front of the deque.

        Returns:
            object: The element removed from the front of the deque.
            -1: If the deque is empty.
        """
        if self.is_empty():
            return -1
        return self.deque.pop(0)

    def pop_rear(self):
        """
        Remove and return an element from the rear of the deque.

        Returns:
            object: The element removed from the rear of the deque.
            -1: If the deque is empty.
        """
        if self.is_empty():
            return -1
        return self.deque.pop()


# Initialize a deque
deque = Deque()


# Check if the deque is empty
print(deque.is_empty())


# Test push_front
deque.push_front(1)
deque.push_front(2)


# Test push_rear
deque.push_rear(3)
deque.push_rear(4)


# Print deque
print(deque.deque)


# Test front
print(deque.front())


# Test rear
print(deque.rear())


# Check the size of the deque
print(deque.size())


# Test pop_front
print(deque.pop_front())


# Print deque
print(deque.deque)


# Test pop_rear
print(deque.pop_rear())


# Print deque
print(deque.deque)
