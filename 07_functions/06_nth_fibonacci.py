# Function to get nth fibonacci term
def get_nth_fibonacci(n):
    # Initialize first 2 terms
    a, b = 0, 1

    # Check n
    if n < 1:
        # Invalid
        return -1
    elif n == 1:
        # First term
        return a
    elif n == 2:
        # Second term
        return b
    else:
        # Loop to find and return nth term
        for i in range(2, n):
            # Find next term to reach nth term
            a, b = b, a + b

        # Return the final answer
        return b


# User input for n
n = int(input())


# Get and print the nth term
print(get_nth_fibonacci(n))
