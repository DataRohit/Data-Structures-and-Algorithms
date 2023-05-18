# Import typing for type hinting
from typing import *


# Import math for mathematical operations
import math


# Function to calculate the power of number
def modular_exponentiation(x: int, n: int, m: int) -> int:
    # Variable to store the result
    res = 1

    # Loop for calculating the power of number
    while n > 0:
        # If power is odd
        if n & 1:
            # Update the result
            res = (res * (x % m)) % m

        # Update x to x^2
        x = ((x % m) * (x % m)) % m

        # Divide n by 2
        n = n >> 1

    # Return final answer
    return res


# User input for number of elements
x, n, m = map(int, input().split())


# Call the function and get the power
print(modular_exponentiation(x, n, m))
