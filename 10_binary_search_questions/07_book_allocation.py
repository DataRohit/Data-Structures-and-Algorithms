# Function to check if it is possible to allocate pages
def is_possible(arr, n, m, mid):
    # Initialize students count
    student_count = 1

    # Initialize count of pages allocated to student
    page_sum = 0

    # Loop over pages array
    for i in range(n):
        # If allocated pages are less than mid
        # More pages can be allocated
        if page_sum + arr[i] <= mid:
            # Allocate pages to student
            page_sum += arr[i]

        # If allocated pages are more than mid
        else:
            # Request for new student
            student_count += 1

            # If total students are more than m
            # If current pages are more than mid
            if student_count > m or arr[i] > mid:
                # Return False
                return False

            # Reset page_sum to current book pages
            page_sum = arr[i]

    # Return True
    return True


# Function to allocate the pages
def allocate_book(arr, n, m):
    # Initialize start and end
    start, end = 0, sum(arr)

    # Initialize ans
    ans = -1

    # Loop till start <= end
    while start <= end:
        # Calculate mid
        mid = start + (end - start) // 2

        # Check if mid pages can be allocated
        if is_possible(arr, n, m, mid):
            # Update the answer
            ans = mid

            # Search for lower allocated pages in left half
            end = mid - 1

        # If mid pages cannot be allocated
        else:
            # Search for higher allocated pages in right half
            start = mid + 1

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


# Get the maximum number of allocated pages
ans = allocate_book(arr, n, m)


# Print the maximum allocated pages
print(ans)
