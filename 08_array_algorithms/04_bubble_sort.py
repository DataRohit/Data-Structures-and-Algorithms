# Function to apply bubble sort
def bubble_sort(arr, n):
    # Loop for rounds
    for i in range(n - 1):
        # Loop over elements
        for j in range(n - i - 1):
            # If current element greater than next
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# User input for number of elements
n = int(input())


# Initialize array of size n with 0
arr = arr = [0] * n


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


# Apply bubble sort algorithm
bubble_sort(arr, n)


# Print the sorted array
print(*arr)
