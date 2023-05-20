# Import typing for type hinting
from typing import *


# Function to generate all possible combinations
def solve(digits: str, output: str, index: int, ans: List[str], mapping: dict) -> None:
    # Base case -> index > length of string
    if index >= len(digits):
        # Push the output to answer list
        ans.append(output)

        # Return
        return

    # Get the mapping for the first number
    value = mapping[digits[index]]

    # Recursive call for every character in value
    for i in value:
        # Push the character to output
        output += i

        # Recursive call for the elements of next character
        solve(digits, output, index + 1, ans, mapping)

        # Back track - remove the current character for new combination
        output = output[:-1]


# Main function to return all possible combinations
def letter_combinations(digits: str) -> List[str]:
    # Check if empty string
    if len(digits) == 0:
        return []

    # Initialize an array to store all the combinations
    ans = []

    # Initialize an output string to hold the individual combination
    output = ""

    # Initialize the start index
    index = 0

    # Create a dictionary to map the number with string
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    # Call the solve function
    solve(digits, output, index, ans, mapping)

    # Return the list containing all the possible combinations
    return ans


# Take user input for number
digits = input()


# Get the results
ans = letter_combinations(digits)


# Print teh results
print(ans)
