# Function to chech palindrome
def check_palindrome(s):
    # Convert the string to lowercase
    s = s.lower()

    # Check every character in the string
    for i in s:
        # Check if character is not letter or digit
        if not i.isalnum():
            # Replace it by empty space
            s = s.replace(i, "")

    # Check the string with reversed characters
    return s == s[::-1]


# Take user input for test cases
T = int(input())


# Loop over for T test cases
for i in range(T):
    # Take user input for string
    s = input()

    # Apply the function to check palindrome
    print(check_palindrome(s))
