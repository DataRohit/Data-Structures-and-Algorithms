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


def getTopView(root):
    # Base case -> Root is None
    if root is None:
        return []

    # Mapping to store top node for every horizontal distance
    topNode = {}

    # Initialize a queue to store [Node, Horizontal Distance]
    queue = deque()

    # Push root element
    queue.append([root, 0])

    # Traverse till queue is empty
    while queue:
        # Pop and store the front
        front = queue.popleft()

        # Extract front node
        frontNode = front[0]

        # Horizontal distance
        hd = front[1]

        # If node value not present for horizontal distance
        if hd not in topNode.keys():
            # Create entry
            topNode[hd] = frontNode.val

        # Push left of frontNode
        if frontNode.left:
            queue.append([frontNode.left, hd - 1])

        # Push right of frontNode
        if frontNode.right:
            queue.append([frontNode.right, hd + 1])

    # Sort the nodes based on horizontal distance
    sorted_nodes = sorted(topNode.items(), key=lambda x: x[0])

    # Create and return answer list
    return [j for i, j in sorted_nodes]


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


# Print top view of binary tree
print(getTopView(root_node))
