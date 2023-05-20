# Import typing for type hinting
from typing import *


# Function to include and exclude elements and generate output
def solve(s: str, output: str, index: int, ans: List[str]) -> None:
    if index >= len(s):
        # Add output is not an empty string
        if output != "":
            # Add it to the answer
            ans.append(output)
        return

    # Exclude the current character
    solve(s, output, index + 1, ans)

    # Get the element to include and add to output
    output += s[index]

    # Recursive call
    solve(s, output, index + 1, ans)

    # Backtrack by removing the last element
    output = output[:-1]


# Main function to return subsequences
def subsequences(s: str) -> str:
    # List to store all the possible subsequences
    ans = []

    # String to store the possible substring
    output = ""

    # Variable for tracking index
    index = 0

    # Call the solve function
    solve(s, output, index, ans)

    # Return the answer
    return ans


# Take user input for the string
s = input()


# Apply function to get the subsequences
ans = subsequences(s)


# Print the power set
print(ans)
