# Function to rotate the array
def rotate_array(arr, n, k):
    # Initialize an answer list
    ans = [0] * n

    # Loop over elements
    for i in range(n):
        # Move the element left by k places
        ans[(i + k) % n] = arr[i]

    # Return rotated array
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


# User input for k
k = int(input())


# Rotate the array after k places
ans = rotate_array(arr, n, k)

# Print rotated array
print(*ans)
