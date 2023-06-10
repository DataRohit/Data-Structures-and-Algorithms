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


# Function to count leaf nodes
def no_of_leaf_nodes(root):
    # Recursive function to count leaf nodes
    def function(root):
        # Base case -> Root node is none
        if root is None:
            return 0

        # Check if the node is a leaf node
        if root.left is None and root.right is None:
            return 1

        # Recursively count leaf nodes in the left and right subtrees
        left_count = function(root.left)
        right_count = function(root.right)

        # Return the sum of leaf nodes in left and right subtrees
        return left_count + right_count

    # Call the function
    return function(root)


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


# Print the count of leaf nodes
print(no_of_leaf_nodes(root_node))
