# Function to convert binary to decimal
def convert_to_decimal(num):
    # Initialize ans
    ans = 0

    # Loop to get bits and generate binary
    i = 0
    while num != 0:
        # Extract last bit
        digit = num % 10

        # Get binary of the right most digit
        if digit == 1:
            # Generate the answer
            ans = ans + (2**i)

        # Update the last bit
        num = num // 10

        # Increment the counter
        i += 1

    # Return the answer
    return ans


# User input for number
num = int(input())


# Print the binary representation
print(convert_to_decimal(num))
