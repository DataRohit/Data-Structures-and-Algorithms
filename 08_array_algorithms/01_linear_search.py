# Function to implement linear search
def linear_search(arr, key):
    # Loop over arr elements
    for i in range(len(arr)):
        # Check if element == key
        if arr[i] == key:
            # Element exist
            return i

    # Element not exist
    return -1


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


# User input for key
key = int(input())


# Apply linear search function and check key
print(linear_search(arr, key))
