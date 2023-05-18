# Import typing for type hinting
from typing import *


# Function to calculate the factorial
def modular_factorial(n: int, p: int) -> int:
    # If n >= p
    if n >= p:
        # Return 0
        return 0

    # Variable to store result
    res = 1

    # Loop from 1 to n
    for i in range(1, n + 1):
        res = (res * i) % p

    # Return the result
    return res


# User input for number of elements
n, p = map(int, input().split())


# Call the function and get the factorial
print(modular_factorial(n, p))
