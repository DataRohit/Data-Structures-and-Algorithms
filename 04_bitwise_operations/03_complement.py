# Function to calculate bitwise complement
def get_bitwise_complement(num):
    # Make a copy of number
    num_copy = num

    # Create a mask to ignore leading bits
    mask = 0

    # Check if number is 0
    if num == 0:
        return 1

    # If number != 0
    while num_copy != 0:
        # Create a mask to ignore leading bits
        mask = (mask << 1) | 1

        # Right shift the number
        num_copy = num_copy >> 1

    # Apply the mask
    return ~num & mask


# User input for number
num = int(input())


# Print the bit wise complement
print(get_bitwise_complement(num))
