# Import typing for type hinting
from typing import *


# Function to get the GCD of 2 numbers
def get_gcd(a: int, b: int) -> int:
    # If a is 0
    # Then b is gcd
    if a == 0:
        return b

    # If b is 0
    # Then a is gcd
    if b == 0:
        return a

    # Loop till a != b
    while a != b:
        # If a is larger
        if a > b:
            # Update a
            a = a - b

        # If b is larger
        else:
            b = b - a

        # Return the final answer
        return a


# User input for number of elements
m, n = map(int, input().split())


# Print the count of prime numbers
print(get_gcd(m, n))
