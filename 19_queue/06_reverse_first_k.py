# Import collections to use deque
from collections import deque


# Function to reverse first k elements of the array
def reverse_first_k(arr, n, k):
    # Initialize an empty stack
    dq = deque()

    # Traverse the array from left to right
    for i in range(k):
        # Push the current element to stack
        dq.append(arr.pop(0))

    # Pop till stack is empty and push to array
    while len(dq) > 0:
        arr.append(dq.pop())

    # Traverse the arr for remaining elements
    for i in range(n - k):
        # Push the current element to the rear of array
        arr.append(arr.pop(0))

    # Return the array
    return arr


# Take input from user
arr = list(map(int, input().split()))
k = int(input())


# Call the function to reverse first k elements of the array
print(reverse_first_k(arr, len(arr), k))
