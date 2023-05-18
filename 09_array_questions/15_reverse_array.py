# Function to reverse the array
def reverse_array(arr, n):
    # Loop over index till n // 2
    for i in range(n // 2):
        # Swap elements
        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]


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


# Print the reversed array
print(*arr[::-1])

# Apply the function to reverse the array
reverse_array(arr, n)

# Print reversed array
print(*arr)
