# Function to get minimum and maximum element in array
def get_min_max(arr, n):
    # Initialize minimum and maximum element with first element
    mini = maxi = arr[0]

    # Loop over elements
    for i in arr:
        # Store minimum element and maximum element
        mini = min(mini, i)
        maxi = max(maxi, i)

    # Return the answer
    return mini, maxi


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


# Get the minimum and maximum element in array
mini, maxi = get_min_max(arr, n)

# Print the mini and maxi element
print(mini, maxi)
