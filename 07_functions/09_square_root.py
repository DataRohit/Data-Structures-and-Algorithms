# Function to calculate the square root of a number
def square_root(n, d):
    # Store the square root of n in sqrtNum
    sqrtNum = n / 2

    # Temp to track the decimal
    temp = 0

    # Check if square root == temp
    while sqrtNum != temp:
        # Store the value of sqrtNum in temp
        temp = sqrtNum

        # Calculate the decimal
        sqrtNum = (n / temp + temp) / 2

    # Return the final value of sqrtNum
    return round(sqrtNum, d)


# User input for number of elements
n, d = map(int, input().split())


# Get and print the square root of element
print(square_root(n, d))
