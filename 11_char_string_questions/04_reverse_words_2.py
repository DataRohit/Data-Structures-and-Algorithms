# Function to reverse words in string
def reverse_words(s: str) -> str:
    # Reverse the words in string
    return " ".join(s.split()[::-1])


# Take user input for string
s = input()


# Get and print the reverse words string
print(reverse_words(s))
