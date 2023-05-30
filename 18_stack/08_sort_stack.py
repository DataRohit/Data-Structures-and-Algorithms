# Import collections to use deque
from collections import deque


# Function to insert the element in sorted fashion
def sorted_insert(s, num):
    # Base case  -> If stack is empty
    # Base case -> Stack is not empty and Top smaller than num
    if len(s) == 0 or (len(s) > 0 and s[-1] < num):
        # Push to stack
        s.append(num)

        # Return
        return

    # Store the top element
    n = s[-1]

    # Pop the stack
    s.pop()

    # Recursive call
    sorted_insert(s, num)

    # Push the remaining element to stack
    s.append(n)


# Function to sort the stack
def sort_stack(s):
    # Base case -> Stack is empty
    if len(s) == 0:
        # Return
        return

    # Store the current top element
    num = s[-1]

    # Pop the top element
    s.pop()

    # Recursive call
    sort_stack(s)

    # Sorted insert
    sorted_insert(s, num)


# Declare and initialize a unsorted stack
stack = deque([1, 3, 2, 5, 4])


# Print the stack
print(stack)


# Call the function to sort the stack
sort_stack(stack)


# Print the stack
print(stack)
