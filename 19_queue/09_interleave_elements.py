# Import collections to use deque
from collections import deque


# Function to interleave the first half of the queue with the second half
def interleave_queue(queue):
    # Initialize an empty deque
    new_queue = deque()

    # Traverse first half elements
    for i in range(len(queue) // 2):
        # Pop the front of the queue and push to new queue
        new_queue.append(queue.popleft())

    # Traverse till the new_queue is empty
    while len(new_queue) != 0:
        # Pop the front of new queue and push to original queue
        queue.append(new_queue.popleft())

        # Pop the from of the original queue and push to original queue
        queue.append(queue.popleft())

    # Return the queue
    return queue


# Take user input for number of number of elements
N = int(input())


# Take user input for elements
elements = list(map(int, input().split()))[:N]


# Call the function to interleave the queue
print(interleave_queue(deque(elements)))
