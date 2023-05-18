# Function to check sorted and rotated array
def check_sorted_rotated(arr, n):
    # Initialize count of pairs i > i + 1
    count = 0

    # Loop over elements
    for i in range(n):
        # Compare with the next element in rotation
        # If next previous element is greater than next
        if arr[i % n] > arr[(i + 1) % n]:
            # Increment count
            count += 1

    # If count is greater than 1 return False else True
    return count <= 1


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

# Check and print result
print(check_sorted_rotated(arr, n))
