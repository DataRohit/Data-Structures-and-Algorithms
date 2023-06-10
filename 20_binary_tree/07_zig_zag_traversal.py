# Import collections for deque
from collections import *


# Initialize node structure of binary tree
class Node(object):
    # Constructor to initialize node
    def __init__(self, data=None):
        # Assign data to current node
        self.data = data

        # Initialize left and right children as None
        self.left = None
        self.right = None


# Function to build a binary tree from level order traversal
def build_binary_tree(arr, root, i, n):
    # Base case: If current index exceeds the array size or the element is None,
    # return the node as None
    if i >= n or arr[i] is None:
        return None

    # Create a new node with the current element in the array
    root = Node(arr[i])

    # Recursively build the left and right subtrees
    root.left = build_binary_tree(arr, root.left, 2 * i + 1, n)
    root.right = build_binary_tree(arr, root.right, 2 * i + 2, n)

    # Return the root node
    return root


def zigZagTraversal(root):
    # List to store zig zag traversal
    zig_zag_traversal = []

    # Function to get zig zag traversal
    def function(root=root):
        # Base case -> Root node is None
        if root is None:
            # Return
            return

        # Initialize an empty queue
        queue = deque()

        # Push the first node to queue
        queue.append(root)

        # Variable to track direction
        left_to_right = True

        # Loop till queue is empty
        while queue:
            # Get the current level size
            level_size = len(queue)

            # List to store the current level elements
            level_elements = []

            for _ in range(level_size):
                # Pop and store the front of the queue
                front = queue.popleft()

                # Add front data to level elements list
                level_elements.append(front.data)

                # Add left and right children to the queue
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)

            # Append the level elements in zigzag order
            if left_to_right:
                zig_zag_traversal.extend(level_elements)
            else:
                zig_zag_traversal.extend(level_elements[::-1])

            # Toggle the direction for the next level
            left_to_right = not left_to_right

    # Call the function
    function(root)

    # Return the answer list
    return zig_zag_traversal


# Input array representing the binary tree
input_arr = [1, 3, 5, 7, 11, 17, None]

"""

The above input array represents the following binary tree:

                1
        3               5
    7       11      17    None

"""


# Build the binary tree from the array
root_node = build_binary_tree(input_arr, None, 0, len(input_arr))


# Print zig zag traversal of the tree
print(zigZagTraversal(root_node))
