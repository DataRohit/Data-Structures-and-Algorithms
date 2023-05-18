# Function to get pivot element index
def get_pivot_element_index(arr, n):
    # Check if array is empty
    if len(arr) == 0:
        # No pivot element exist
        return -1

    # If array has only 1 element
    # Or array is sorted
    if len(arr) == 1 or arr[0] < arr[n - 1]:
        # Return index of first element
        return 0

    # Initialize start and end pointer
    start, end = 0, n - 1

    # Loop till start <= end
    while start <= end:
        # Calculate the mid
        mid = start + (end - start) // 2

        # Check mid
        if mid < n - 1 and arr[mid] > arr[mid + 1]:
            # Index mid + 1 is pivot
            return mid + 1

        # Search in right half
        elif arr[start] <= arr[mid]:
            start = mid + 1

        # Else search in left half
        else:
            end = mid - 1

    # If no condition satisfied
    return 0


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

# Get and print pivot element index
print(get_pivot_element_index(arr, n))
