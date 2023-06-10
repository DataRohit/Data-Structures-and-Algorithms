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


# Function to diagonally traverse a binary tree
def diagonalTraversal(root):
    # Function to traverse the binary tree
    def traverse(node, level, diagonal_map):
        # Base case: If node is None, return
        if node is None:
            return

        # Check if the current level exists in the diagonal map
        if level in diagonal_map:
            # If it exists, append the node's value to the corresponding diagonal list
            diagonal_map[level].append(node.data)

        else:
            # If it doesn't exist, create a new list for that level in the diagonal map
            diagonal_map[level] = [node.data]

        # Traverse the left child with an increased level -> Start of next diagonal
        traverse(node.left, level + 1, diagonal_map)

        # Traverse the right child with the same level -> Part of diagonal
        traverse(node.right, level, diagonal_map)

    # Create an empty dictionary to store diagonal elements
    diagonal_map = {}

    # Start the traversal from the root with level 0
    traverse(root, 0, diagonal_map)

    # Collect the diagonal elements in a list
    diagonal_elements = []
    for level, values in diagonal_map.items():
        diagonal_elements.extend(values)

    # Return the list of diagonal elements
    return diagonal_elements


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


# Print diagonal traversal
print(diagonalTraversal(root_node))
