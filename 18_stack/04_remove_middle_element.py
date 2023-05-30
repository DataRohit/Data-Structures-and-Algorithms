# Import collections to use deque
from collections import deque


# Recursive function to delete middle element of a stack
def solve(inputStack, count, N):
    # Base case -> mid reached
    if count == N // 2:
        # Pop the middle element
        inputStack.pop()

        # Return
        return

    # Store the top element of stack
    num = inputStack[-1]

    # Pop the top element
    inputStack.pop()

    # Recursive call
    solve(inputStack, count + 1, N)

    # Push the top element back to stack
    inputStack.append(num)


# Function to delete middle element of a stack
def delete_middle(inputStack, N):
    # Variable to track count of elements traversed
    count = 0

    # Call the recursive function
    solve(inputStack, count, N)


# Declare and initialize a stack1
stack1 = deque([1, 2, 3, 4, 5])


# Print the stack1
print(stack1)


# Call the function to delete middle element
delete_middle(stack1, len(stack1))


# Print the stack1
print(stack1)


# Declare and initialize a stack2
stack2 = deque([1, 2, 3, 4, 5, 6])


# Print the stack2
print(stack2)


# Call the function to delete middle element
delete_middle(stack2, len(stack2))


# Print the stack2
print(stack2)
