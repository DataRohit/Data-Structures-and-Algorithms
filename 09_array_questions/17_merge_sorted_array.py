# Function to merge two sorted arrays
def merge_sorted(arr1, m, arr2, n):
    # Create array to store elements
    arr3 = []

    # Initialize pointers
    s1 = s2 = 0

    # Loop till s1 < m and s2 < n
    while s1 < m and s2 < n:
        # Check smaller element
        if arr1[s1] < arr2[s2]:
            # Store element
            arr3.append(arr1[s1])

            # Update pointer
            s1 += 1

        else:
            # Store element
            arr3.append(arr2[s2])

            # Update pointer
            s2 += 1

    # Add remaining elements of arr1
    while s1 < m:
        arr3.append(arr1[s1])
        s1 += 1

    # Add remaining elements of arr2
    while s2 < n:
        arr3.append(arr2[s2])
        s2 += 1

    # Return answer
    return arr3


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
    # Break if index >= n
    if index >= n:
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


# Get the merged sorted array
arr3 = merge_sorted(arr1, m, arr2, n)


# Print the merged sorted array
print(*arr3)
