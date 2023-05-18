# Function to calculate the pair sum
def pair_sum(arr, n, s):
    # Initialize array to store the pairs
    ans = []

    # Traverse the array for first element
    for i in arr:
        # Traverse the array for second element
        for j in arr:
            # Check sum
            if arr[i] + arr[j] == s:
                # Get the pair
                pair = [min(arr[i], arr[j]), max(arr[i], arr[j])]

                # Add pair to ans if not exists
                if pair not in ans:
                    # Add pair to ans
                    ans.append(pair)

    # Sort the answer vector
    ans.sort()

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


# User input for sum
s = int(input())


# Get result
result = pair_sum(arr, n, s)


# Print the result
print(*result)
