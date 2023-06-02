# Import collections to use deque
from collections import deque


# Function to reverse the queue
def reverse_queue(queue):
    # Base case
    if len(queue) == 0:
        return

    # Dequeue current item (from front)
    data = queue.popleft()

    # Reverse remaining queue
    reverse_queue(queue)

    # Enqueue current item (to rear)
    queue.append(data)


# Initialize a queue
queue = deque([10, 6, 8, 12, 3])


# Print the queue
print(queue)


# Reverse the queue
reverse_queue(queue)


# Print the queue
print(queue)
