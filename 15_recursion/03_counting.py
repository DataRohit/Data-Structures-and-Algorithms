# Import typing for type hinting
from typing import *


# Recursive function to print counting numbers from 1 to n
def head_counting(n: int) -> None:
    # Base case
    if n == 0:
        return

    # Head Recurssion Function call to lower number
    head_counting(n - 1)

    # Print the current n value
    print(n, end=" ")


# Recursive function to print counting numbers from n to 1
def tail_counting(n: int) -> None:
    # Base case
    if n == 0:
        return

    # Print the current n value
    print(n, end=" ")

    # Tail Recurssion Function call to lower number
    tail_counting(n - 1)


# Take user input for value
n = int(input())


# Call the function and print the counting
print(head_counting(n))
print(tail_counting(n))
