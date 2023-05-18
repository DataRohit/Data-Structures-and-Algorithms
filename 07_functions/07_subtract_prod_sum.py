# Function to calculate product and sum
def subtract_product_sum(num):
    # Initialize product and sum
    prod, sum = 1, 0

    # Loop till number becomes 0
    while num > 0:
        # Get right most digit
        rem = num % 10

        # Update prod and num
        prod *= rem
        sum += rem

        # Remove right most digit
        num //= 10

    # Return the answer
    return prod - sum


# User input for num
num = int(input())


# Get and print result
print(subtract_product_sum(num))
