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
def buildBinaryTree(arr, root, i, n):
    # Base case: If current index exceeds the array size or the element is None,
    # return the node as None
    if i >= n or arr[i] is None:
        return None

    # Create a new node with the current element in the array
    root = Node(arr[i])

    # Recursively build the left and right subtrees
    root.left = buildBinaryTree(arr, root.left, 2 * i + 1, n)
    root.right = buildBinaryTree(arr, root.right, 2 * i + 2, n)

    # Return the root node
    return root


# Function to check if a binary tree is a BST
# Recursive function to check for valid BST
def isBST(root, mini, maxi):
    # Base case -> Root is none
    if root is None:
        # Return True
        return True

    # First case
    if mini <= root.data <= maxi:
        # Get answer for left
        leftAns = isBST(root.left, mini, root.data - 1)

        # Get answer for right
        rightAns = isBST(root.right, root.data + 1, maxi)

        # Return the answer
        return leftAns and rightAns

    # Else
    else:
        # Return False
        return False


# Function to check if give binary tree is BST
def validateBST(root):
    # Call the recursive function and return the answer
    return isBST(root, float("-inf"), float("inf"))


# Take user input for elements of the BST
input_arr = list(map(int, input().split()))


# Build the binary tree from the array
root_node = buildBinaryTree(input_arr, None, 0, len(input_arr))
