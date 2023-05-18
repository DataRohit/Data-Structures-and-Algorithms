# Function to find triplets with sum equal to given sum
def findTriplets(arr, n, s):
    # Initialize array to store the pairs
    ans = []

    # Sort the array
    arr.sort()

    # Loop the array
    for i in range(n - 2):
        # Index of second and third element
        j = i + 1
        k = n - 1

        # While second element < third
        while j < k:
            # Get sum
            sum = arr[i] + arr[j] + arr[k]

            # Check sum
            if sum == s:
                # Create the triplet
                triplet = [arr[i], arr[j], arr[k]]

                # Check if triplet already exists
                if triplet not in ans:
                    # Add to ans
                    ans.append(triplet)

                # Increment j and Decrement k
                j += 1
                k -= 1

            # If sum < s
            elif sum < s:
                # Increase second index
                j += 1

            # If sum > s
            else:
                # Decrease third index
                k -= 1

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
result = findTriplets(arr, n, s)


# Print the result
print(*result)
