# Function to find the duplicate element in array
def find_duplicate(arr, n):
    # Initialize the answer
    ans = 0

    # XOR every element in array
    # Repeated elements will cancel out
    for i in range(n):
        ans = ans ^ arr[i]

    # XOR again
    # Repeated element will remain
    # Other will cancel
    for i in range(n):
        ans = ans ^ i

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
print(find_duplicate(arr, n))
