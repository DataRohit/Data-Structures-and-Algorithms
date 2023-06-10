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


def verticalOrderTraversal(root):
    # Map to store nodes
    nodes = {}

    # Queue for level order traversal
    q = deque()

    # List to store the answer
    ans = []

    # If root is None
    if root is None:
        return ans

    # Push [Node, [Horizontal Dist, Level]] to queue
    q.append([root, [0, 0]])

    # Loop till queue is empty
    while q:
        # Pop and store front element
        front = q.popleft()

        # Extract Node from front
        frontNode = front[0]

        # Extract horizontal distance and level
        hd = front[1][0]
        lv = front[1][1]

        # If entry exists
        if hd in nodes:
            if lv in nodes[hd]:
                nodes[hd][lv].append(frontNode.data)
            else:
                nodes[hd][lv] = [frontNode.data]
        else:
            nodes[hd] = {lv: [frontNode.data]}

        # If left node exists
        if frontNode.left:
            # Push to queue
            q.append([frontNode.left, [hd - 1, lv + 1]])

        # If right node exists
        if frontNode.right:
            # Push to queue
            q.append([frontNode.right, [hd + 1, lv + 1]])

    # Sort the nodes based on horizontal distance
    sorted_nodes = sorted(nodes.items(), key=lambda x: x[0])

    # Extract data from map
    for i, j in sorted_nodes:
        # Sort the nodes based on level
        sorted_nodes_level = sorted(j.items(), key=lambda x: x[0])
        for _, values in sorted_nodes_level:
            ans.extend(values)

    # Return answer
    return ans


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


# Print vertical order traversal
print(verticalOrderTraversal(root_node))
