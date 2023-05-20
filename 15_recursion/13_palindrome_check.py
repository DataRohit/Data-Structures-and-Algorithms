# Import typing for type hinting
from typing import *


# Function to check if string is palindrome
def is_palindrome(s: str) -> bool:
    # Base case -> single character is palindrome
    if len(s) <= 1:
        return True

    # Compare first element with last
    elif s[0] != s[-1]:
        return False

    # Remove the first and last element and check again
    else:
        return is_palindrome(s[1:-1])


# Take user input for string
s = input()


# Check if string is palindrome
print(is_palindrome(s))
