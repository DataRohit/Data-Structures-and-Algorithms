# Import
import sys


# Initialize INT_MIN and INT_MAX
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize - 1


# Function to reverse the integer
def reverse(num):
    # Initialize answer
    ans = 0

    # Loop till num != 0
    while num != 0:
        # Get right most digit
        digit = num % 10

        # Corner case
        if ans > INT_MAX and ans < INT_MAX:
            # Answer cannot be store
            return 0

        # Else add the digit to answer
        ans = ans * 10 + digit

        # Remove right most digit
        num //= 10

    # Return answer
    return ans


# User input for num
num = int(input())

# Get and print reversed integer
print(reverse(num))
