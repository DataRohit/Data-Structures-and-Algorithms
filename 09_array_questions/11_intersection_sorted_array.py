# Function to find intersection of two sorted arrays
def find_array_intersection(arr1, m, arr2, n):
    # List to store the result
    result = []

    # Loop over arr1
    for i in arr1:
        # Check if arr1 element is present in arr2
        if i in arr2:
            # Add element to result
            result.append(i)

    # Return result
    return result


# User input for number of elements
m, n = map(int, input().split())


# Initialize array1 of size m with 0
# Initialize array2 of size n with 0
arr1 = [0] * m
arr2 = [0] * n


# Array input
arr1_input = input()


# Loop over index
for index, i in enumerate(arr1_input.split()):
    # Break if index >= m
    if index >= m:
        # Break out of loop
        break

    # Get user input
    arr1[index] = int(i)


# Array input
arr2_input = input()


# Loop over index
for index, i in enumerate(arr2_input.split()):
    # Break if index >= n
    if index >= n:
        # Break out of loop
        break

    # Get user input
    arr2[index] = int(i)


# Get result
result = find_array_intersection(arr1, m, arr2, n)


# Print the answer vector
print(*result)
