# Function to swap alternate elements
def swap_alternate(arr, n):
    # Loop over odd index
    for i in range(0, n, 2):
        # Swap elements
        arr[i], arr[i + 1] = arr[i + 1], arr[i]


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


# Apply the function to swap alternate elements
swap_alternate(arr, n)


# Print the swapped array
print(*arr)
