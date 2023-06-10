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


# Recursive function to find the sum of the longest path from root to leaf node
def solve(root, curr_sum, max_sum, curr_len, max_len):
    # Base case -> If root is none
    if root is None:
        # If current length is greater than max length
        if curr_len > max_len:
            # Update max length and max sum
            max_len = curr_len
            max_sum = curr_sum

        # If current length is equal to max length
        elif curr_len == max_len:
            # Update max sum
            max_sum = max(max_sum, curr_sum)

        # Return max sum and max length
        return max_sum, max_len

    # Update the sum
    curr_sum += root.data

    # Call for left and right subtrees
    max_sum, max_len = solve(root.left, curr_sum, max_sum, curr_len + 1, max_len)
    max_sum, max_len = solve(root.right, curr_sum, max_sum, curr_len + 1, max_len)

    # Return max sum and max length
    return max_sum, max_len


# Function to find the sum of the longest path from root to leaf node
def sum_longest_path(root):
    # Variable to store the current length and max length
    curr_len = 0
    max_len = 0

    # Variable to store the sum and max sum
    curr_sum = 0
    max_sum = 0

    # Recursive solve function
    max_sum, _ = solve(root, curr_sum, max_sum, curr_len, max_len)

    # Return the max sum
    return max_sum


# Input array representing the binary tree
input_arr = [4, 2, 5, 7, 1, 2, 3, None, 6]


# Build the binary tree from the array
root_node = build_binary_tree(input_arr, None, 0, len(input_arr))


# Find the sum of the longest path from root to leaf node
print(sum_longest_path(root_node))
