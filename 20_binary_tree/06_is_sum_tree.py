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


def is_sum_tree(root):
    # Recursive function to check sum tree
    def is_sum_tree_fast(root=root):
        # Base case -> Root node is None
        if root == None:
            # Return True and Sum
            return True, 0

        # Case for leaf node
        if root.left == root.right == None:
            # Return True and Current node value
            return True, root.val

        # Recursive call for left and right subtree
        left_is_sum, left_val = is_sum_tree_fast(root.left)
        right_is_sum, right_val = is_sum_tree_fast(root.right)

        # Check value at current node
        condition = root.val == left_val + right_val

        # Get the answer
        if left_is_sum and right_is_sum and condition:
            # Return True and Sum of val
            return True, 2 * root.val

        # Else
        else:
            # Return False
            return False, -1

    # Call the function
    return is_sum_tree_fast(root)[0]


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


# Print if tree is sum tree
print(is_sum_tree(root_node))
