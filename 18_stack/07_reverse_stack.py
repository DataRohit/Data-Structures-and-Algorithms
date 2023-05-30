# Import collections to use deque
from collections import deque


# Function to reverse stack
def reverse_stack(s):
    # Base case -> stack is empty
    if len(s) == 0:
        # Return
        return

    # Save the top element
    num = s[-1]

    # Pop the top
    s.pop()

    # Recursive call for reversing the stack
    reverse_stack(s)

    # Insert num at bottom
    s.insert(0, num)


# Declare and initialize a stack
stack = deque([1, 2, 3, 4, 5])


# Print the stack
print(stack)


# Call the function to reverse stack
reverse_stack(stack)


# Print the stack
print(stack)
