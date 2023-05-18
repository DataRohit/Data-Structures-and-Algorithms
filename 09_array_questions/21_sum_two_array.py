# Function to find sum of two arrays
def find_sum(arr1, m, arr2, n):
    # Initialize answer array
    ans = []

    # Generate number from array1
    num1 = int("".join(arr1))
    num2 = int("".join(arr2))

    # Calculate the sum
    ans_num = num1 + num2

    # Get the rightmost digit and add to array
    while ans_num != 0:
        # Get remainder
        rem = ans_num % 10

        # Add remainder to array
        ans.append(rem)

        # Update the sum
        ans_num //= 10

    # Reverse the ans array
    ans = ans[::-1]

    # Return the answer array
    return ans


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
    arr1[index] = i


# Array input
arr2_input = input()


# Loop over index
for index, i in enumerate(arr2_input.split()):
    # Break if index >= n
    if index >= n:
        # Break out of loop
        break

    # Get user input
    arr2[index] = i


# Get the answer array
ans = find_sum(arr1, m, arr2, n)

# Print the answer array
print(*ans)
