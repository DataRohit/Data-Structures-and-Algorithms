# Stack implemented using class and list
class Stack:
    """
    This class represents a stack data structure implemented using a Python list.
    """

    def __init__(self):
        """
        Initializes an empty stack with the specified capacity.
        """
        self.stack = []

    def push(self, item):
        """
        Pushes an item onto the top of the stack.

        Args:
            item: The item to be pushed onto the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Removes and returns the item at the top of the stack.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty and there are no items to pop.
        """
        if self.empty():
            raise IndexError("Stack underflow. Cannot pop item from an empty stack.")
        return self.stack.pop()

    def top(self):
        """
        Returns the index of item at the top of the stack.

        Returns:
            Index of item at the top of the stack.

        Raises:
            IndexError: If the stack is empty and there are no items to retrieve.
        """
        if self.empty():
            raise IndexError(
                "Stack underflow. Cannot retrieve item from an empty stack."
            )
        return self.size() - 1

    def peek(self):
        """
        Returns the item at top of the stack without removing it.

        Returns:
            The item at top of the stack without removing it.
        """
        if self.empty():
            raise IndexError(
                "Stack underflow. Cannot retrieve item from an empty stack."
            )
        return self.stack[-1]

    def empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def clear(self):
        """
        Clears all the items from the stack, making it empty.
        """
        self.stack = []

    def copy(self):
        """
        Creates a shallow copy of the stack.

        Returns:
            A new stack object with the same items as the original stack.
        """
        return Stack(self.capacity).stack.extend(self.stack)

    def size(self):
        """
        Returns the total number of elements in the stack.

        Returns:
            The number of elements in the stack.
        """
        return len(self.stack)


# Declare and initialize a new stack
stack = Stack()


# Push items onto the stack
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)


# Print the stack contents
print(stack.stack)


# Pop items from the stack
print(stack.pop())


# Print the stack contents
print(stack.stack)


# Print the index of top of the stack
print(stack.top())


# Peek the item at the top of the stack
print(stack.peek())


# Check if the stack is empty
print(stack.empty())


# Clear the stack
stack.clear()


# Check if the stack is empty
print(stack.empty())
