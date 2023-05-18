# Function to get first occurrence
def first_occ(arr, n, key):
    # Initialize start and end
    start, end = 0, n - 1

    # Initialize ans
    ans = -1

    # Loop till start <= end
    while start <= end:
        # Calculate mid
        mid = start + (end - start) // 2

        # Check at mid position
        if key == arr[mid]:
            # Update the answer
            ans = mid

            # Update the end index to search for occurrence in left half
            end = mid - 1

        # If key is less than arr[mid]
        elif key < arr[mid]:
            # Search in left half
            end = mid - 1

        # If key is greater than arr[mid]
        else:
            # Search in right half
            start = mid + 1

    # Return the answer
    return ans


# Function to get last occurrence
def last_occ(arr, n, key):
    # Initialize start and end
    start, end = 0, n - 1

    # Initialize ans
    ans = -1

    # Loop till start <= end
    while start <= end:
        # Calculate mid
        mid = start + (end - start) // 2

        # Check at mid position
        if key == arr[mid]:
            # Update the answer
            ans = mid

            # Update the end index to search for occurrence in left half
            start = mid + 1

        # If key is less than arr[mid]
        elif key < arr[mid]:
            # Search in left half
            end = mid - 1

        # If key is greater than arr[mid]
        else:
            # Search in right half
            start = mid + 1

    # Return the answer
    return ans


# Function to get the first and last occ
def first_and_last_pos(arr, n, key):
    # Initialize the pair
    pair = [-1, -1]

    # Get the first and last occurrence
    pair[0] = first_occ(arr, n, key)
    pair[1] = last_occ(arr, n, key)

    # Return the pair
    return pair


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


# Get the first and last pos and print
print(*first_and_last_pos(arr, n, key))
