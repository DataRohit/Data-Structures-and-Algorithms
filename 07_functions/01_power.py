# Function to calculate the power
def get_power(num, power):
    # Initialize answer
    ans = 1

    # Loop power times
    for i in range(power):
        # Update answer
        ans *= num

    # Return final answer
    return ans


# User input for number and power
num, power = map(int, input().split())


# Get and print the answer
print(get_power(num, power))
