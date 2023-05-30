# Import collections to use deque
from collections import deque


# Function to find the minimum cost
def find_minimum_cost(exp):
    # Handle the condition for str containing odd characters
    if len(exp) & 1 == 1:
        # String cannot be converted to valid
        return -1

    # Initialize a stack
    s = deque()

    # Traverse the string
    for i in exp:
        # If open bracket
        if i == "{":
            # Push to stack
            s.append(i)

        # If closed bracket
        else:
            # Stack is not empty and
            # Open bracket for closed bracket found
            if len(s) > 0 and s[-1] == "{":
                # Pop the stack
                s.pop()

            # If no open bracket found
            else:
                # Push the bracket to stack
                s.append(i)

    # Stack contains invalid expression

    # Initialize vars to count opening and closing brackets
    a = 0
    b = 0

    # If stack is not empty
    while len(s) > 0:
        # If open bracket
        if s[-1] == "{":
            # Update a count
            a += 1

        # If close bracket
        else:
            # Update b count
            b += 1

        # Pop the stack
        s.pop()

    # Calculate the answer
    ans = (a + 1) // 2 + (b + 1) // 2

    # Return the answer
    return ans


# User input for expression
expression = input()


# Call the function and store the result
result = find_minimum_cost(expression)


# Print the result
print(result)
