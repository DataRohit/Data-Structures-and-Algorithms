# Function to get the smallest greater character
def next_greater_char(arr, n, target):
    # Generate the list of all the characters greater than target
    greater_chars = [i for i in arr if i > target]

    # Return the smallest character or -1
    return min(greater_chars) if greater_chars else -1


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
    arr[index] = i


# User input for target character
target = input()


# Get the smallest greater character
print(next_greater_char(arr, n, target))
