# Function to check if mid board value is possible
def is_possible(arr, n, m, mid):
    # Initialize painter count
    painter_count = 1

    # Initialize allocated boards
    boards = 0

    # Loop over boards array
    for i in range(n):
        # If allocated boards are less than mid
        # More boards can be allocated
        if boards + arr[i] <= mid:
            # Allocate boards to painter
            boards += arr[i]

        # If allocated boards are more than mid
        else:
            # Allocate boards to new painter
            painter_count += 1

            # Check if painter count is more than m
            # Check if current board value is more than mid
            if painter_count > m or arr[i] > mid:
                # Mid value is not possible
                return False

            # Reset boards count to current board value
            boards = arr[i]

    # Return True
    return True


# Function to allocate the boards
def allocate_boards(arr, n, m):
    # Initialize the start and end
    start, end = 0, sum(arr)

    # Initialize the answer
    ans = -1

    # Loop till start <= end
    while start <= end:
        # Calculate mid
        mid = start + (end - start) // 2

        # Check if the mid boards can be allocated
        if is_possible(arr, n, m, mid):
            # Update the answer to mid
            ans = mid

            # Search for smaller value in left half
            end = mid - 1

        # If mid boards cannot be allocated
        else:
            # Try allocating more boards
            start = mid + 1

    # Return the final answer
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


# Get the maximum number of allocated boards
ans = allocate_boards(arr, n, m)


# Print the maximum allocated boards
print(ans)
