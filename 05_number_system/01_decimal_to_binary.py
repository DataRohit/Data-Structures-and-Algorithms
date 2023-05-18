# Function to convert decimal to binary
def convert_to_binary(num):
    # Initialize answer
    ans = 0

    # Update number if num < 0
    if num < 0:
        num = ~num + 1

    # Loop to get bits and generate binary
    i = 0
    while num != 0:
        # Extract last bit
        bit = num & 1

        # Generate the ans
        ans = (bit * (10**i)) + ans

        # Right shift the number
        num = num >> 1

        # Update i
        i += 1

    # Return the answer
    return ans


# User input for number
num = int(input())


# Print the binary representation
print(convert_to_binary(num))
