# Function to reverse words in string
def reverse_words(s: str) -> str:
    split_words = s.split(" ")

    # Reverse the words in string
    return " ".join([i[::-1] for i in split_words])


# Take user input for string
s = input()


# Get and print the reverse words string
print(reverse_words(s))
