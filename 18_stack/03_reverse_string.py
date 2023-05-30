# Import collections to use deque
from collections import deque


# Function to reverse string
def reverse_string(string):
    # Create a stack
    stack = deque()

    # Initialize a empty string
    rev_string = ""

    # Push all characters of string to stack
    for char in string:
        stack.append(char)

    # Pop all characters of stack and put them back to string
    for i in range(len(string)):
        rev_string += stack.pop()

    # Return the reversed string
    return rev_string


# User input string
string = input()


# Call the function to reverse string
rev_string = reverse_string(string)


# Print the reversed string
print(rev_string)
