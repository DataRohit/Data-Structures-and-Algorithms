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


# Function to find the LCA
def lowestCommonAncestor(root, x, y):
    # Base case -> If root node is null
    if root == None:
        # Return None
        return None

    # If current node is x or y
    if root.data == x or root.data == y:
        # Return current node
        return root.data

    # Search for x and y in left sub tree
    leftAns = lowestCommonAncestor(root.left, x, y)

    # Search for x and y in right sub tree
    rightAns = lowestCommonAncestor(root.right, x, y)

    # If current node is LCA
    if leftAns != None and rightAns != None:
        # Return current node
        return root.data

    # If leftAns is None and rightAns has value
    elif leftAns == None and rightAns != None:
        # Return the rightAns
        return rightAns

    # If leftAns has value and rightAns is None
    elif leftAns != None and rightAns == None:
        # Return the leftAns
        return leftAns

    # Else
    else:
        # Return None
        return None


# Input array representing the binary tree
input_arr = [4, 2, 5, 7, 1, 2, 3, None, 6]


# Build the binary tree from the array
root_node = build_binary_tree(input_arr, None, 0, len(input_arr))


# Call the function and find LCA of the nodes
print(lowestCommonAncestor(root_node, 7, 3))
