# Import collections to use deque
from collections import deque


# Function to check for redundant brackets
def find_redundant_brackets(expression):
    # Declare and initialize the stack
    s = deque()

    # Traverse the expression
    for i in expression:
        # If current character is -> (, +. -, *, /
        if i in ["(", "+", "-", "*", "/"]:
            # Push to stack
            s.append(i)

        # Else -> character is closing bracket or letter
        else:
            # If character is closing bracket
            if i == ")":
                # Variable to track redundant brackets
                is_redundant = True

                # Loop till we find opening bracket
                while s[-1] != "(":
                    # Get the top of the stack
                    top = s[-1]

                    # If top is operator
                    if top in ["+", "-", "*", "/"]:
                        # Bracket is not redundant
                        is_redundant = False

                    # Pop the operator
                    s.pop()

                # If brackets are redundant are return
                if is_redundant == True:
                    return True

                # Pop the opening bracket
                s.pop()

    # Return false
    return False


# User input for expression
expression = input()


# Call the function and store the result
result = find_redundant_brackets(expression)


# Print the result
print(result)
