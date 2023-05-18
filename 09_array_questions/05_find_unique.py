# Function to find unique element in array
def find_unique(arr, n):
    # Initialize answer
    ans = 0

    # Take XOR to find unique
    """
        Same element XOR with each other will give 0
        Unique element XOR with 0 will give the unique element
    """
    for i in arr:
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

"""
    All the elements in the array are
    repeated twice except one element.
"""
# Get and print the unique element
print(find_unique(arr, n))
