# Function to check vowel
def check_vowel(ch):
    # Match case to check and print
    match ch:
        case "a" | "e" | "i" | "o" | "u":
            return True
        case _:
            return False


# User input for character
ch = input()


# Check and print result
print(check_vowel(ch))
