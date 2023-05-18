# Function to check case and number
def check_case_number(ch):
    # Get the ASCII value of the input character
    ascii_val = ord(ch)

    # Condition for number
    if ascii_val >= ord("0") and ascii_val <= ord("9"):
        return "number"

    # Condition for lower case
    elif ascii_val >= ord("a") and ascii_val <= ord("z"):
        return "lower"

    # Condition for upper case
    elif ascii_val >= ord("A") and ascii_val <= ord("Z"):
        return "upper"

    # Other symbol
    else:
        return "symbol"


# Take user input
ch = input()

# Call the function and print the output
print(check_case_number(ch))
