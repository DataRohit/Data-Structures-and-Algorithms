# Import typing for type hinting
from typing import *


# Recursive function to calculate power of number
def power(p: int) -> int:
    # Base case to stop recursion
    if p == 0:
        return 1

    # Calculate the power of 2 for lower power using recursion
    return 2 * power(p - 1)


# Take user input for power
p = int(input())


# Call the function and print the power
print(power(p))
