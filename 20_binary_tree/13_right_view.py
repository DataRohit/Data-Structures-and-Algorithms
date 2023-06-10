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


# Function to get the right view of a binary tree
def getRightView(root):
    # List to store the right view of binary tree
    ans = []

    # Recursive function to generate ans
    def traverse(node, level):
        # If node is None -> Return
        if node is None:
            return

        # New level condition
        if level == len(ans):
            # Push the current node data to ans
            ans.append(node.data)

        # Recursive call for right and left subtree
        traverse(node.right, level + 1)
        traverse(node.left, level + 1)

    # Recursive function to generate the ans
    traverse(root, 0)

    # Return the final ans
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


# Print right view of binary tree
print(getRightView(root_node))
