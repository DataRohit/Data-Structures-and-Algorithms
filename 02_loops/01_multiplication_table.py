# Function to print the multiplication table till 10
def print_table(num):
    # Loop on number from 1 to 10
    for i in range(1, 11, 1):
        # Print the multiplied number
        print(num * i)


# User input for number
num = int(input())

# Print the table
print_table(num)
