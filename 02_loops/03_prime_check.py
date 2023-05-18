# Function to check prime number
def is_prime_number(num):
    # Start point
    i = 2

    # Check till num / 2
    while i <= num / 2:
        # Check if a factor exist
        if num % i == 0:
            # If a factor exist return true
            return True

        # Update the i counter
        i += 1

    # If factor not exist return false
    return False


# User input for number
num = int(input())

# Check and print if prime number
print(is_prime_number(num))
