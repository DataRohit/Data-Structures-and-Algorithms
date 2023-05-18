# Function to calculate average
def calculate_average(total, vals):
    return total / vals


# User input for number of values
vals = int(input())

# Initialize total sum
total = 0

# Take user input for values
for i in range(vals):
    # Take user input
    total += float(input())

# Calculate and print the average
print(calculate_average(total, vals))
