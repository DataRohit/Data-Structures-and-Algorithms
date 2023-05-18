# Import typing for type hinting
from typing import *


# Function to calculate the nth catalan number
def catalan(n: int) -> int:
    # Initialize catalan array with 0
    catalan = [0 for i in range(n + 1)]

    # Base case
    catalan[0] = 1

    # Calculare catalan using dynamic programming
    for i in range(1, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]

    # Return the catalan number
    return catalan[n]


# User input for number of elements
n = int(input())


# Apply the function to get the nth catalan number
print(catalan(n))
