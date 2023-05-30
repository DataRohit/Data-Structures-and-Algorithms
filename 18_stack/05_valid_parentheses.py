#  Function to check for valid parenthesis
def is_valid_parenthesis(string):
    # Initialize a stack to store the brackets
    s = []

    # Map from end bracket to start bracket
    end_to_start_map = {"}": "{", ")": "(", "]": "["}

    # Loop over the string
    for i in string:
        # If opening bracket
        if i in ["{", "(", "["]:
            # Push to stack
            s.append(i)

        # If closing bracket
        else:
            # If stack is not empty
            if len(s) > 0:
                # Get the top of the stack
                top_element = s[-1]

                # Match the top element with the current closing bracket
                if top_element == end_to_start_map[i]:
                    # If brackets match pop the stack
                    s.pop()

                # If brackets dont match
                else:
                    # Return invalid parenthesis
                    return False

            # Invalid parentheses
            else:
                return False

    # Return the answer
    # If len(s) == 0 -> False
    # False -> Stack is empty -> Valid parentheses
    # Thus return `not False` -> True
    return not bool(len(s))


# User input for string of brackets
string = input()


# Call the function to check for valid parenthesis
valid = is_valid_parenthesis(string)


# Print the answer
print(valid)
