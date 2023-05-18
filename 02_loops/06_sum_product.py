# Function to calculate the sum and product
def get_sum_product(num):
    # Initialize the sum and product
    sum, product = 0, 1

    # Loop till number becomes 0
    while num > 0:
        # Get the left most digit
        rem = num % 10

        # Update the sum and product
        sum += rem
        product *= rem

        # Update the number
        num //= 10

    # Return the final sum and product
    return sum, product


# User input for number
num = int(input())

# Get the sum and product of digits
sum, product = get_sum_product(num)

# Print the sum and product
print(sum, product)
