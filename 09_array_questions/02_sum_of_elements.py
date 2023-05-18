# Function to calculate the sum
def get_sum(arr):
    # Initialize sum
    sum = 0

    # Loop over elements
    for i in arr:
        # Update sum
        sum += i

    # Return the sum
    return sum


# User input for number of elements
n = int(input())


# Initialize array of size n with 0
arr = [0] * n


# Array input
arr_input = input()


# Loop over index
for index, i in enumerate(arr_input.split()):
    # Break if index >= n
    if index >= n:
        # Break out of loop
        break

    # Get user input
    arr[index] = int(i)


# Get the sum of elements in array
sum = get_sum(arr)

# Print the sum
print(sum)
