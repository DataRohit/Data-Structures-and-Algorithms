# Function to wave print the matrix
def wave_print(matrix: List[List[int]], n: int, m: int) -> List[int]:
    # List to store the wave print traversal
    wave = []

    # Loop over columns
    for i in range(m):
        # If the column is even
        if i % 2 == 0:
            # Traverse from top to bottom
            for j in range(n):
                # Add the element to wave list
                wave.append(matrix[j][i])

        # If the column is odd
        else:
            # Traverse from bottom to top
            for j in range(n - 1, -1, -1):
                # Add the element to wave list
                wave.append(matrix[j][i])

    # Return the wave traversal list
    return wave


# Take user input for test cases
t = int(input())


# Loop for t test cases
for i in range(t):
    # Take user input for rows and columsn
    n, m = map(int, input().split())

    # Initialize the matrix
    matrix = [0] * n

    # Loop for rows
    for j in range(n):
        # Initialize array of size m with 0
        arr = [0] * m

        # Array input
        arr_input = input()

        # Loop over index
        for index, k in enumerate(arr_input.split()):
            # Break if index >= n
            if index >= m:
                # Break out of loop
                break

            # Get user input
            arr[index] = int(k)

        # Add row to matrix
        matrix[j] = arr

    # Call the function and wave print the result
    print(wave_print(matrix, n, m))
