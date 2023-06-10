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


# Recursive function to traverse the paths and update the count
def solve(root, k, path):
    # Base case -> Root node is none
    if root is None:
        return 0

    # Add the current node data to path
    path.append(root.data)

    # Temp variable to track the sum
    temp_sum = 0
    count = 0

    # Traverse the path list in reverse order
    for i in range(len(path) - 1, -1, -1):
        temp_sum += path[i]

        if temp_sum == k:
            count += 1

    # Traverse left sub tree and right sub tree
    count += solve(root.left, k, path) + solve(root.right, k, path)

    # Pop the last element while returning
    path.pop()

    # Return the count
    return count


# Main function to return the total paths having sum k
def sumK(root, k):
    # List to store elements of current path
    path = []

    # Call recursive function to update the count
    count = solve(root, k, path)

    # Return the count
    return count


# Input array representing the binary tree
input_arr = [4, 2, 5, 7, 1, 2, 3, None, 6]


# Build the binary tree from the array
root_node = build_binary_tree(input_arr, None, 0, len(input_arr))


# Print the total paths having sum k
print(sumK(root_node, 9))
