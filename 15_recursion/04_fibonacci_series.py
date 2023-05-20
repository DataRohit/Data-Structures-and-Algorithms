# Import typing for type hinting
from typing import *


# Recursive function to calculate fibonacci
def fibonacci(n: int) -> int:
    # Base case to stop recursion
    if n == 1 or n == 0:
        return n

    # Calculate the fibonacci term
    return fibonacci(n - 1) + fibonacci(n - 2)


# Take user input for value
n = int(input())


# Call the function and print the fibonacci series
for i in range(n):
    print(fibonacci(i), end=" ")
