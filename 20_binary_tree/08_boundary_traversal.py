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


# Function to traverse the left part
def traverseLeft(root, ans):
    # If root is None or root is leaf node
    if (root == None) or (root.left == root.right == None):
        return

    # Store the data
    ans.append(root.data)

    # If left exist
    if root.left:
        traverseLeft(root.left, ans)

    # Else
    else:
        traverseLeft(root.right, ans)


# Function to traverse the leaf nodes
def traverseLeaf(root, ans):
    # If root is None
    if root == None:
        return

    # If node is leaf node
    if root.left == root.right == None:
        # Add the node to answer
        ans.append(root.data)

        # Return
        return

    # Traverse left and right sub tree
    traverseLeaf(root.left, ans)
    traverseLeaf(root.right, ans)


# Function to traverse the right part
def traverseRight(root, ans):
    # If root is None or root is leaf node
    if (root == None) or (root.left == root.right == None):
        return

    # If right exist
    if root.right:
        # Traverse right
        traverseRight(root.right, ans)

    # Else
    else:
        # Traverse left
        traverseRight(root.left, ans)

    # Push the value to ans in reverse order
    ans.append(root.data)


def traverseBoundary(root):
    # List to store the answer
    ans = []

    # If root is None
    if root == None:
        # Return the answer array
        return ans

    # Push the root data to ans
    ans.append(root.data)

    # Traverse left part
    traverseLeft(root.left, ans)

    # Traverse leaf node
    traverseLeaf(root.left, ans)
    traverseLeaf(root.right, ans)

    # Traverse right part
    traverseRight(root.right, ans)

    # Return ans
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


# Print boundary traversal of the binary tree
print(traverseBoundary(root_node))
