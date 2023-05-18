# Function to count set bits
def count_set_bits(num1, num2):
    # Initialize ans
    ans = 0

    # Loop till num1 != 0
    while num1 != 0:
        # Check right most digit and update answer
        ans += num1 & 1

        # Right shift the number
        num1 = num1 >> 1

    # Loop till num1 != 0
    while num2 != 0:
        # Check right most digit and update answer
        ans += num2 & 1

        # Right shift the number
        num2 = num2 >> 1

    # Return final answer
    return ans


# User input for num1 and num2
num1, num2 = map(int, input().split())


# Get and print count of set bits
print(count_set_bits(num1, num2))
