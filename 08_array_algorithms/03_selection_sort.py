# Function to apply selection sort
def selection_sort(arr, n):
    # Loop for rounds
    for i in range(n):
        # Initialize min index
        min_idx = i

        # Loop over elements
        for j in range(i + 1, n):
            # Check if element less than current element
            if arr[j] < arr[min_idx]:
                # Update min_idx
                min_idx = j

        # Swap to bring smaller element to left
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


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


# Apply the selection sort algorithm
selection_sort(arr, n)

# Print the sorted array
print(*arr)
