# Function to get pivot element index
def get_pivot_element_index(arr, n):
    # Initialize left and right sum
    lsum, rsum = 0, sum(arr)

    # Loop over elements
    for i in range(n):
        # Assume current element as pivot
        rsum -= arr[i]

        # Check left and right sum
        if lsum == rsum:
            # Return the index
            return i

        # If not equal, update left sum
        lsum += arr[i]

    # If no pivot found
    return -1


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
