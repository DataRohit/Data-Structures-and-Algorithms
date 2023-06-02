# Import collections to use deque
from collections import deque


# Function to get the first negative integer in every window of size k
def first_negative(arr, n, k):
    # Initialize an empty deque
    dq = deque()

    # Array to store the answer
    ans = []

    # Process first window of k size
    for i in range(k):
        # If current element is negative
        if arr[i] < 0:
            # Add the index to deque
            dq.append(i)

    # If deque has elements
    if len(dq) > 0:
        # Store the front element to ans
        ans.append(arr[dq[0]])

    # If deque is empty
    else:
        # Add 0 to ans list
        ans.append(0)

    # Process remaining windows
    for i in range(k, n):
        # If deque is not empty and
        # The front of deque not part of window
        if len(dq) > 0 and i - dq[0] >= k:
            # Pop the deque
            dq.popleft()

        # If current element is negative
        if arr[i] < 0:
            # Push the current index to deque
            dq.append(i)

        # If deque has elements
        if len(dq) > 0:
            # Store the front element to ans
            ans.append(arr[dq[0]])

        # If deque is empty
        else:
            # Add 0 to ans list
            ans.append(0)

    # Return the ans array
    return ans


# Take input from user
arr = list(map(int, input().split()))
size = int(input())


# Call the function to get the first negative integer in every window of size k
print(first_negative(arr, len(arr), size))
