# Import typing for type hinting
from typing import *


# Recursive function to get number as digits name
def say_digits(n: int, names: List[str]) -> None:
    # If number becomes 0
    if n == 0:
        return

    # Get the digit
    digit = n % 10

    # Reduce the number
    n = n // 10

    # Recursive function to print the remaining number
    say_digits(n, names)

    # Print the name of the digit
    print(names[digit], end=" ")


# Take user input for total stairs
n = int(input())


# Array storing the name of digits
names = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


# Call the function and print the total ways to climb stairs
print(say_digits(n, names))
