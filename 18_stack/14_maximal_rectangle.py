def largest_rectangle_area(heights):
    # Create an empty stack to store the indices of increasing heights
    stack = []

    # Variable to store the maximum area
    max_area = 0

    # Start index
    i = 0

    # Iterate over the heights array
    while i < len(heights):
        # If the stack is empty or the current height is greater than or equal to the height at the top of the stack
        if not stack or heights[i] >= heights[stack[-1]]:
            # Push the current index onto the stack
            stack.append(i)

            # Move to the next index
            i += 1

        else:
            # Current height is smaller than the height at the top of the stack
            # Pop the index at the top of the stack
            top = stack.pop()

            # Calculate the area using the popped height
            area = heights[top] * (i if not stack else i - stack[-1] - 1)

            # Update the maximum area if necessary
            max_area = max(max_area, area)

    # Process the remaining heights in the stack
    while stack:
        # Pop the index at the top of the stack
        top = stack.pop()

        # Calculate the area using the popped height
        area = heights[top] * (i if not stack else i - stack[-1] - 1)

        # Update the maximum area if necessary
        max_area = max(max_area, area)

    # Return the maximum area
    return max_area


def maximal_rectangle(matrix) -> int:
    # Check if the matrix is empty
    if not matrix:
        return 0

    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create an array to store the heights for each column
    heights = [0] * cols

    # Variable to store the maximum rectangle area
    max_area = 0

    # Iterate over each row of the matrix
    for i in range(rows):
        # Update the heights array based on the values in the matrix for the current row
        for j in range(cols):
            # If the current cell is '1', increment the height for the corresponding column
            if matrix[i][j] == "1":
                heights[j] += 1

            # If the current cell is '0', reset the height for the corresponding column to 0
            else:
                heights[j] = 0

        # Calculate the maximum rectangle area for the current row using the largest_rectangle_area function
        row_max_area = largest_rectangle_area(heights)

        # Update the overall maximum area if necessary
        max_area = max(max_area, row_max_area)

    # Return the overall maximum rectangle area
    return max_area


# User input for number of rows and cols
rows, cols = map(int, input().split())


# Initialize the matrix
matrix = []


# User input for matrix
for i in range(rows):
    matrix.append(list(map(str, input().split()))[:cols])


# Print the maximum rectangle area
print(maximal_rectangle(matrix))
