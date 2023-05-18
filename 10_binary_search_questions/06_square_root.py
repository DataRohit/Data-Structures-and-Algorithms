# Binary search function to calculate square root
def binary_search(n):
    # Initialize start and end
    start, end = 0, n

    # Initialize answer
    ans = -1

    # Loop till start <= end
    while start <= end:
        # Calculate mid
        mid = start + (end - start) // 2

        # Get square of mid
        mid_square = mid * mid

        # Compare mid_square to n
        if n == mid_square:
            return mid

        # Search closest sqrt in left half
        elif n < mid_square:
            end = mid - 1

        # Search closes sqrt in right half
        else:
            # Update answer
            ans = mid

            # Search in right half
            start = mid + 1

    # Return the answer
    return ans


# Function to calculate square root
def square_root(n):
    # Return the answer
    return binary_search(n)


# User input for number of elements
n = int(input())


# Get and print the square root of number
print(square_root(n))
