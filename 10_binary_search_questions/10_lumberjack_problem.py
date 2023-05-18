# Function to get the sawblade height
def get_sawblade_height(arr, n, m):
    # Sort the list of trees in descending order
    arr.sort(reverse=True)

    # Loop over saw blade height length from arr[0] to 0
    for height in range(arr[0], -1, -1):
        # Calculate the amount of wood cut for the height
        wood_cut_at_height = sum(max(tree - height, 0) for tree in arr)

        # Check if wood cut at height is feasible
        if wood_cut_at_height >= m:
            # Return the current height
            return height

    # If no solution is found return the height of smallest tree
    return arr[-1]


# User input for number of elements
n, m = map(int, input().split())


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


# Get the height of the sawblade
ans = get_sawblade_height(arr, n, m)


# Print the sawblade height
print(ans)
