# Function to get peak index
def get_peak_index(arr, n):
    # Initialize start and end
    start, end = 0, n - 1

    # Loop till start < end
    while start < end:
        # Calculate mid
        mid = start + (end - start) // 2

        # Compare with mid and mid + 1
        if arr[mid] < arr[mid + 1]:
            # Search in right half
            start = mid + 1

        # Search in left half
        else:
            # Update end
            end = mid

    # Return the index of peak element
    return start


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


# Get and print peak index
print(get_peak_index(arr, n))
