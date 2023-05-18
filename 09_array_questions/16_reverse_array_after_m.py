# Function to reverse the array after m
def reverse_after_m(arr, n, m):
    # Initialize the start and end index
    start = m + 1
    end = n - 1

    # Loop till start <= end
    while start <= end:
        # Swap elements
        arr[start], arr[end] = arr[end], arr[start]

        # Update start and end pointer
        start += 1
        end -= 1


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


# User input for index to reverse after
m = int(input())

# Reverse after m
print(*(arr[: m + 1 :] + arr[n - 1 : m : -1]))

# Reverse the array using swapping
reverse_after_m(arr, n, m)

# Print the reversed array
print(*arr)
