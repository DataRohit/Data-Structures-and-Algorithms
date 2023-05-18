# Function to check for unique occurrences
def unique_occurrences(arr, n):
    # List to store element
    a = [0] * 2002
    b = [0] * 1001

    """
        Increase the count of element by 1
        at respective index in a
    """
    for i in arr:
        a[i + 1000] += 1

    """
        Increase the count of count of element by 1
        at respective index in b
    """
    for i in range(2001):
        if a[i] != 0:
            b[a[i]] += 1

            # If count > 1 return False
            if b[a[i]] > 1:
                return False

    # If unique return True
    return True


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

# Get and print the unique occurrences
print(unique_occurrences(arr, n))
