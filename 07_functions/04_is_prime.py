# Function to check if a number if prime
def is_prime(num):
    # Loop over numbers <= num / 2
    for i in range(2, (num // 2) + 1):
        # Check if factor exist
        if num % i == 0:
            # Number is not prime
            return False

    # Number is prime
    return True


# User input for number
num = int(input())


# Get and print result
print(is_prime(num))
