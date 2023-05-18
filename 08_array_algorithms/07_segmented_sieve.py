# Import typing for type hinting
from typing import *


# Import math for mathematical operations
import math


# Function to count the prime numbers
def count_primes(n: int) -> int:
    # Step 1: Generate all primes up to sqrt(n)
    sqrt_n = int(math.sqrt(n))

    # Create a boolean list `primes` of length `sqrt(n) + 1` and initialize all values to `True`.
    primes = [True] * (sqrt_n + 1)

    # Mark the values at indices 0 and 1 as `False`, since they are not prime.
    primes[0] = primes[1] = False

    # Iterate over the remaining values from 2 to `sqrt(n)`, marking all multiples of each prime as `False` in the `primes` list.
    for i in range(2, int(sqrt_n**0.5) + 1):
        if primes[i] == True:
            for j in range(i * i, sqrt_n + 1, i):
                primes[j] = False

    # Step 2: Divide the range [2, n] into segments of size sqrt(n)
    count = 0

    # Iterate over each segment in the range.
    for i in range(2, n + 1, sqrt_n):
        segment_start = i
        segment_end = min(i + sqrt_n - 1, n)

        # Step 3: Generate all primes in the current segment using the sieve of Eratosthenes
        # Create a boolean list `is_prime` of length `sqrt(n) + 1` and initialize all values to `True`.
        is_prime = [True] * (sqrt_n + 1)

        # Iterate over all primes up to `sqrt(n)` in the `primes` list.
        for j in range(2, sqrt_n + 1):
            if primes[j] == True:
                # Calculate the smallest multiple of `j` in the current segment.
                start = math.ceil(segment_start / j) * j

                # Mark all multiples of `j` in the current segment as `False` in the `is_prime` list.
                for k in range(start, segment_end + 1, j):
                    is_prime[k - segment_start] = False

        # Step 4: Count the number of primes in the current segment
        # Sum the values in the `is_prime` list that are still `True`.
        count += sum(is_prime)

    # Step 5: Return the total count of primes in the range [2, n].
    return count


# User input for number of elements
n = int(input())


# Print the count of prime numbers
print(count_primes(n))
