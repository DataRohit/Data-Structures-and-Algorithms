# Function to get the maximum occuring character
def get_max_occurring_char(S: str) -> str:
    # Get list of all unique characters
    unique_chars = sorted(set(S))

    # Initialize the max count and max count character by first character
    max_count, max_char = S.count(unique_chars[0]), unique_chars[0]

    # Loop over each unique character
    for i in range(1, len(unique_chars)):
        # Check if count of current element > count of prior element
        if S.count(unique_chars[i]) > max_count:
            # Update the max count and max count character
            max_count, max_char = S.count(unique_chars[i]), unique_chars[i]

    # Return the max occuring character
    return max_char


# Take user input for string
S = input()


# Get and print the most occuring character
print(get_max_occurring_char(S))
