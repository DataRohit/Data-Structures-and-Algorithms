# Function to apply insertion sort
def insertion_sort(arr, n):
    # Counter for rounds
    i = 0

    # Loop for rounds
    while i < n:
        # Store current element
        temp = arr[i]

        # Counter fr second loop
        j = i - 1

        # Loop for previous elements
        while j >= 0:
            # Previous element greater than current element
            if arr[j] > temp:
                # Move element to +1 index
                arr[j + 1] = arr[j]

            # Else break the loop and move to next element
            else:
                break

            # Compare with more previous elements
            j -= 1

        # Add element to the created empty place
        arr[j + 1] = temp

        # Go to next round
        i += 1


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


# Apply insertion sort function
insertion_sort(arr, n)


# Print the sorted array
print(*arr)
