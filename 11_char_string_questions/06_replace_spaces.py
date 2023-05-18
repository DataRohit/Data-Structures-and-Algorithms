# Function to replace space by @40
def replace_spaces(s):
    # Replace spaces with @40
    return s.replace(" ", "@40")


# Take user input for string
s = input()


# Get and print the space replaced string
print(replace_spaces(s))
