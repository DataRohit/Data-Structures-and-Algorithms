# Function to check if power of 2
def is_power_of_two(num):
    # Count set bits
    set_bits = 0

    # Loop till num != 0
    while num > 0:
        # Check for set bit
        if num & 1 == 1:
            # Increment set bits
            set_bits += 1

        # Right shift the number
        num = num >> 1

    # Check power of 2
    if set_bits == 1:
        return True
    else:
        return False


# User input for number
num = int(input())


# Check and print if power of 2
print(is_power_of_two(num))
