# Import collections to use deque
from collections import deque


# Function to get the next smaller element in the array
def find_smaller_element(arr, n):
    # Initialize a stack with -1 to store the answer
    stack = [-1]

    # Answer array
    ans = []

    # Loop over array elements in reverse
    for i in range(n - 1, -1, -1):
        # Store current element
        curr = arr[i]

        # Traverse till top is smaller than curr
        while stack[-1] >= curr:
            # Pop the stack
            stack.pop()

        # Update the answer array
        ans.append(stack[-1])

        # Add the element to stack
        stack.append(curr)

    # Return the answer array in reverse
    return ans[::-1]


# Take input from user
arr = list(map(int, input().split()))


# Get the next smaller element
ans = find_smaller_element(arr, len(arr))


# Print the answer
print(*ans)
