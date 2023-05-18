# Function to sort an array of 0s, 1s and 2s
def sort_012(arr, n):
    # Initialize the low, mid and high
    low, mid, high = 0, 0, n - 1

    # Loop till mid <= high
    while mid <= high:
        # Check if mid value == 0
        if arr[mid] == 0:
            # Swap low and mid values
            arr[low], arr[mid] = arr[mid], arr[low]

            # Increment low and mid index
            low += 1
            mid += 1

        # Check if mid value == 1
        elif arr[mid] == 1:
            # Increment mid index
            mid += 1

        # Check if mid value == 2
        else:
            # Swap with high index
            arr[mid], arr[high] = arr[high], arr[mid]

            # Decrement high index
            high -= 1


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


# Apply the function to sort the array
sort_012(arr, n)

# Print the sorted array
print(*arr)
