# Function to find all unique elements
def find_duplicates(arr, n):
    # Initialize answer list
    ans = []

    # Sort the list
    arr.sort()

    # Loop over elements
    for i in range(n - 1):
        # Check if number is unique
        if arr[i] == arr[i + 1]:
            # Append to answer list
            ans.append(arr[i])

    # Return the answer
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

# Get and print the duplicate element
print(*find_duplicates(arr, n))
