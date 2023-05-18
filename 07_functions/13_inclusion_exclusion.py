# Import typing for type hinting
from typing import *


# Function to count divisible numbers
def count_divisible(r, m, n):
    # Get the count of numbers divisible by m
    c1 = r // m

    # Get the count of numbers divisible by n
    c2 = r // n

    # Get the count of nubers divisbile by both m and n
    c3 = r // (m * n)

    # Apply inclusion exclusion rule
    # n(A ∪ B) = n(A) + n(B) - n(A ∩ B)
    return c1 + c2 - c3


# User input for number of elements
r, m, n = map(int, input().split())


# Apply the function to count numbers divisible by m and n in range r
print(count_divisible(r, m, n))
