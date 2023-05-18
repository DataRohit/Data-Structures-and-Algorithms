# Import typing for type hinting
from typing import *


# Function to update answer to the array
def update_answer(chars, ans, i, count):
    # Add the current element to the ans
    ans.append(chars[i])

    # If count > 1
    if count > 1:
        # Loop over count elements
        for j in str(count):
            # Add count to ans
            ans.append(j)


# Function to compress the string
def compress(chars: List[str]) -> int:
    # Initialize answer array
    ans = []

    # Intialize var to count the occurences
    count = 1

    # Variable for loop
    i = 0

    # Loop over elements
    while i < len(chars) - 1:
        # Check if current element == next element
        if chars[i] == chars[i + 1]:
            # Update the count
            count += 1

        # If current element != next element
        else:
            # Update the answer to array
            update_answer(chars, ans, i, count)

            # Reset the count
            count = 1

        # Update the i pointer
        i += 1

    # Update the final answer to array
    update_answer(chars, ans, i, count)

    # Change chars array to answer array
    chars[:] = ans

    # Return the answer
    return len(chars)


# Take user input for string
chars = [i for i in input()]


# Print the total elements in final array
print(compress(chars))
