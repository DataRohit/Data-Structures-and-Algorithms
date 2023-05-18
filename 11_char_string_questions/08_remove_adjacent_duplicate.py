# Function to get the final duplicate removed string
def remove_duplicates(s: str) -> str:
    # Initialize the stack
    stack = []

    # Add the first element to the stack
    stack.append(s[0])

    # Loop over elements
    for i in range(1, len(s)):
        print(s[i])
        # If stack has elements and
        # If the last element of stack and current element are equal
        if len(stack) > 0 and s[i] == stack[-1]:
            # Pop the stack
            stack.pop()

        # If the element not the same push the element to stack
        else:
            # Push current element to stack
            stack.append(s[i])

    # Return the answer
    return "".join(stack)


# Take user input for string
s = input()


# Get the final duplicate removed string
print(remove_duplicates(s))
