# Function to check if number is even
def is_even(num):
    # If remainder == 0
    if num % 2 == 0:
        # Number is even
        return True
    else:
        # Number id odd
        return False


# User input for number
num = int(input())


# Get and print result
print(is_even(num))
