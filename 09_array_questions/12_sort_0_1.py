# Function to sort an array of 0s and 1s
def sort_zeros_and_ones(arr, n):
    # Initialize the start and end
    start, end = 0, n - 1

    # Loop till start <= end
    while start <= end:
        # If start value == 0
        if arr[start] == 0:
            # Increment start
            start += 1

        # If end value == 1
        elif arr[end] == 1:
            # Decrement end
            end -= 1

        # If start value == 1 and end value == 0
        else:
            arr[start], arr[end] = arr[end], arr[start]


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


# Apply the function to sort the array
sort_zeros_and_ones(arr, n)

# Print the sorted array
print(*arr)
