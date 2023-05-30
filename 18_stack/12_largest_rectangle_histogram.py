# Import collections to use deque
from collections import deque


# Function to get index of next smaller element in the array
def next_smaller_element(arr, n):
    # Initialize the result list with n
    result = [n] * n

    # Create an empty stack to store indices
    stack = []

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # Pop elements from stack while they are greater than or equal to the current element
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        # If stack has elements -> Top is < current
        if stack:
            # Add the current index to stack
            result[i] = stack[-1]

        # Push the current index to the stack
        stack.append(i)

    # Return the result list
    return result


# Function to get index of prev smaller element in the array
def prev_smaller_element(arr, n):
    # Initialize the result list with -1
    result = [-1] * n

    # Create an empty stack to store indices
    stack = []

    # Traverse the array from left to right
    for i in range(n):
        # Pop elements from stack while they are greater than or equal to the current element
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        # If stack has elements -> Top is < current
        if stack:
            # Add the current index to stack
            result[i] = stack[-1]

        # Push the current index to the stack
        stack.append(i)

    # Return the result list
    return result


def largest_rectangle(heights):
    # Store the size of the heights array
    n = len(heights)

    # Call the function to get the index of next smaller element for every element
    next = next_smaller_element(heights, n)

    # Call the function to get the index of prev smaller element for every element
    prev = prev_smaller_element(heights, n)

    # Initialize ans area
    ans_area = 0

    # Traverse the heights array
    for i in range(n):
        # Get the length of the current bar
        l = heights[i]

        # Get the width of the largest rectangle that includes the current bar
        b = next[i] - prev[i] - 1

        # Calculate the new area
        new_area = l * b

        # Update the ans area
        ans_area = max(ans_area, new_area)

    # Return the final answer
    return ans_area


# Take input from user
heights = list(map(int, input().split()))


# Get the area of largest rectangle
ans = largest_rectangle(heights)


# Print the answer
print(*ans)
