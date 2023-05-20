# Import typing for type hinting
from typing import *


# Recursive function to calculate factorial
def factorial(n: int) -> int:
    # Base case to stop recursion
    if n == 0:
        return 1

    # Calculate the factorial
    return n * factorial(n - 1)


# Take user input for value
n = int(input())


# Call the function and print the factorial
print(factorial(n))
