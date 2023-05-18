# Function to get pivot element
def get_pivot_element_index(arr, n):
    # Initialize start and end
    start, end = 0, n - 1

    # Loop till start < end
    while start < end:
        # Calculate mid
        mid = start + (end - start) // 2

        # Compare mid with left most element
        if arr[mid] >= arr[0]:
            # Search in right half
            start = mid + 1

        else:
            # Search in right half
            end = mid

    # Return pivot element index
    return start


# Function to search element
def binary_search(arr, start, end, key):
    # Loop till start <= end
    while start <= end:
        # Calculate mid
        mid = start + (end - start) // 2

        # Check with mid
        if key == arr[mid]:
            return mid

        # Search in right half
        elif key > arr[mid]:
            start = mid + 1

        # Search if left half
        else:
            end = mid - 1

    # If element not present
    return -1


# Function to search element
def search(arr, n, k):
    # Get the pivot element
    pivot = get_pivot_element_index(arr, n)

    # Initialize answer
    ans = -1

    # Search in right half
    if k >= arr[pivot] and k <= arr[n - 1]:
        ans = binary_search(arr, pivot, n - 1, k)

    # Search in left half
    else:
        ans = binary_search(arr, 0, pivot - 1, k)

    # Return the answer
    return ans


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


# Get and print the index of search element
print(search(arr, n, key))
