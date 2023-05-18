# Function to calculate GCD
def get_gcd(a, b):
    # Initialize the gcd
    gcd = min(a, b)

    # Loop to find gcd
    for i in range(gcd, 0, -1):
        # Check divisibility for both a and b
        if a % i == 0 and b % i == 0:
            # Update gcd
            gcd = i

            # If common divisor found break
            break

    # Return the gcd
    return gcd


# Function to calculate LCM
# NOTE: Place get_lcm function after get_gcd function
def get_lcm(a, b):
    # Calculate and return lcm
    return (a * b) / get_gcd(a, b)


# User input for num1 and num2
a, b = map(int, input().split())

# Get and print GCD
print(get_gcd(a, b))

# Get and print LCM
print(get_lcm(a, b))
