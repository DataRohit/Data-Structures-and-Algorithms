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


def is_balanced_bt(root):
    # Function to check if binary tree is balanced
    def is_balanced_fast(node):
        # Base case -> Node is None
        if node is None:
            # Return True and height 0
            return True, 0

        # Call for left and right subtree
        left_bal, left_height = is_balanced_fast(node.left)
        right_bal, right_height = is_balanced_fast(node.right)

        # Get the difference between heights
        height_diff = abs(left_height - right_height) <= 1

        # Update the height of the current node
        current_height = max(left_height, right_height) + 1

        # Check if left and right subtrees are balanced and the height difference is <= 1
        if left_bal and right_bal and height_diff:
            # The current node is balanced
            return True, current_height
        else:
            # The current node is not balanced
            return False, current_height

    # Call the function with the root node and return the balanced status
    return is_balanced_fast(root)[0]


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


# Print if binary tree is balanced
print(is_balanced_bt(root_node))
