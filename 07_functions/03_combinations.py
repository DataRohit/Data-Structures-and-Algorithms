# Function to calculate factorial
def factorial(num):
    # Initialize factorial
    fact = 1

    # Loop to find factorial
    for i in range(num, 1, -1):
        # Multiply the number
        fact *= i

    # Return factorial
    return fact


# Function to calculate nCr
def nCr(n, r):
    # Calculate and return the answer
    return factorial(n) / (factorial(r) * factorial(n - r))


# User input for n and r
n, r = map(int, input().split())


# Get and print answer
print(nCr(n, r))
