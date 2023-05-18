# Function to implement binary search
def binary_search(arr, key):
    # Initialize start and end pointer
    start, end = 0, len(arr) - 1

    # Calculate mid pointer
    mid = start + (end - start) // 2

    # Loop till start <= end
    while start <= end:
        # Check key at mid
        if arr[mid] == key:
            # Return the index if found
            return mid

        # Check left sub array
        elif arr[mid] > key:
            # Update end
            end = mid - 1

        # Check right sub array
        elif arr[mid] < key:
            # Update start
            start = mid + 1

        # Update the mid index
        mid = start + (end - start) // 2

    # Element not found
    return -1


# User input for number of elements
n = int(input())


# Initialize array of size n with 0
arr = arr = [0] * n


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


# Apply binary search function and check key
print(binary_search(arr, key))
