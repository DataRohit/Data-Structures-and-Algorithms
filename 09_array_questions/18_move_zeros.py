# Function to push zero at end
def push_zeros_at_end(arr, n):
    # Var for non zero pointer
    i = 0

    # Loop over elements to search for first non zero element
    for j in range(n):
        # Check if number is 0
        if arr[j] != 0:
            # Swap
            arr[j], arr[i] = arr[i], arr[j]

            # Increment non zero pointer
            i += 1


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

# Apply the function
push_zeros_at_end(arr, n)


# Print the array
print(*arr)
