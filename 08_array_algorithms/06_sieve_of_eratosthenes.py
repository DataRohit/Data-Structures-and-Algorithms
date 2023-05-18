# Import typing for type hinting
from typing import *


# Function to count the prime numbers
def count_primes(n: int) -> int:
    # Initialize count
    count = 0

    # Create an array assuming all numbers are prime
    prime = [True] * (n + 1)

    # Set 0 and 1 as composite numbers
    prime[0] = prime[1] = False

    # Loop over remaining numbers
    for i in range(2, n):
        # Check if number is prime
        if prime[i]:
            # Increment the count
            count += 1

            # Mark the multiples to composite
            for j in range(2 * i, n + 1, i):
                # Set the number to composite
                prime[j] = False

    # Return count
    return count


# User input for number of elements
n = int(input())


# Print the count of prime numbers
print(count_primes(n))
