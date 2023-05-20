# Import typing for type hinting
from typing import *


# Function to reverse the string
def reverse_string(s: str) -> str:
    # Base case -> string with 1 character
    if len(s) <= 1:
        return s

    # Recursive call -> remove first element and add to last
    else:
        return reverse_string(s[1:]) + s[0]


# Take user input for string
s = input()


# Call the function and get the reversed string
rs = reverse_string(s)


# Print reversed string
print(rs)
