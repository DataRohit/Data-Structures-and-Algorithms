# Function to remove all occurrences of part
def remove_occurrences(s, part):
    # Loop till part in s
    while part in s:
        # Replace the first occurrence of part by empty string
        s = s.replace(part, "", 1)

    # Return the answer string
    return s


# Take user input for string and part
s, part = map(str, input().split())


# Get and print the final string
print(remove_occurrences(s, part))
