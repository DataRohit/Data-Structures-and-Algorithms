# Function to check if mid value is possible
def is_possible(arr, n, m, mid):
    # Initialize cow count
    cow_count = 1

    # Get the last position
    last_pos = arr[0]

    # Loop over distances array
    for i in range(n):
        # Check if distance between last cow
        # and current position is more than mid
        if arr[i] - last_pos >= mid:
            # Cow can be placed
            cow_count += 1

            # Check if all cows are placed
            if cow_count == m:
                # Return True
                return True

            # If more cows are to be placed
            # Set last position of cow to current position
            last_pos = arr[i]

    # If the cows cannot be placed
    return False


# Function to get the maximum distance between cows
def get_maximum_distance(arr, n, m):
    # Sort the array
    arr.sort()

    # Initialize start and end
    start, end = 0, arr[n - 1]

    # Initialize answer
    ans = -1

    # Loop till start <= end
    while start <= end:
        # Calculate mid
        mid = start + (end - start) // 2

        # Check if mid value is possible
        if is_possible(arr, n, m, mid):
            # Update the answer to mid
            ans = mid

            # Search for larger value in right half
            start = mid + 1

        # If current distance is not possible
        else:
            # Search for smaller value in left half
            end = mid - 1

    # Return the answer
    return ans


# User input for number of elements
n, m = map(int, input().split())


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


# Get the maximum number distance between cows
ans = get_maximum_distance(arr, n, m)


# Print the maximum distance between cows
print(ans)
