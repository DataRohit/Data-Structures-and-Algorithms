# Function to reverse the array
def reverse_array(arr, n):
    # Initialize start and end index
    start, end = 0, n - 1

    # Swap elements till start <= end
    while start <= end:
        # Swap elements
        arr[start], arr[end] = arr[end], arr[start]

        # Update start and end index
        start += 1
        end -= 1


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


# Apply the reverse function
reverse_array(arr, n)


# Print the reversed array
print(*arr)
