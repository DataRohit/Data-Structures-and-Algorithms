# Function to count set bits
def count_set_bits(num):
    # Var to count set bits
    count = 0

    # Loop till number becomes 0
    while num != 0:
        # Check if right most digit is 1
        if num & 1 == 1:
            # Increment count
            count += 1

        # Right shift the number
        num = num >> 1

    # Return the final count
    return count


# User input for number
num = int(input())


# Get the count of set bits
print(count_set_bits(num))
