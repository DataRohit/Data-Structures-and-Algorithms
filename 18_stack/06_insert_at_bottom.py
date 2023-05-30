# Import collections to use deque
from collections import deque


# Recursive function to insert an element at the bottom of a stack
def solve(myStack, x):
    # Base case -> Stack is empty
    if len(myStack) == 0:
        # Push the new element at the bottom
        myStack.append(x)

        # Return
        return

    # Store the top element for every function call
    num = myStack[-1]

    # Pop the top to reach the bottom
    myStack.pop()

    # Recursive call to check if bottom is reached
    solve(myStack, x)

    # Add the remaining elements to the stack
    myStack.append(num)

    # Return the updated stack
    return myStack


# Function to insert an element at the bottom of a stack
def push_at_bottom(myStack: deque, x: int):
    # Call the recursive function
    return solve(myStack, x)


# Declare and initialize a stack
stack = deque([1, 2, 3, 4, 5])


# Print the stack
print(stack)


# Call the function to insert an element at the bottom of a stack
stack = push_at_bottom(stack, 6)


# Print the stack
print(stack)
