# Initialize node structure of binary tree
class Node(object):
    # Constructor to initialize node
    def __init__(self, data=None):
        # Assign data to current node
        self.data = data

        # Initialize left and right children as None
        self.left = None
        self.right = None


# Inorder traversal of binary tree
def inorderTraversal(root):
    # If root is None
    if root is None:
        # Return empty list
        return []

    # List to store the inorder traversal
    inorder = []

    # Traverse the left subtree
    if root.left:
        inorder += inorderTraversal(root.left)

    # Add the data of the root node to list
    inorder.append(root.data)

    # Traverse the right subtree
    if root.right:
        inorder += inorderTraversal(root.right)

    # Return the list
    return inorder


# Recursive function to build the tree using Preorder
def solve(preorder, mini, maxi, index):
    # If index if out of range
    if index[0] >= len(preorder):
        # Return none
        return None

    # If number not in range
    if preorder[index[0]] < mini or preorder[index[0]] > maxi:
        # Return none
        return None

    # Create a node
    root = Node(preorder[index[0]])

    # Increment the index
    index[0] += 1

    # Recursive call for left and right
    root.left = solve(preorder, mini, root.data, index)
    root.right = solve(preorder, root.data, maxi, index)

    # Return root node
    return root


# Function to return the root node of the constructed BST
def preorderToBST(preorder):
    # Initialize the starting range for root node
    mini = float("-inf")
    maxi = float("inf")

    # Index
    index = [0]

    # Call the solve function
    root = solve(preorder, mini, maxi, index)

    # Return root node
    return root


# Take user input for preorder of the BST
bst_preorder = list(map(int, input().split()))


# Function call to convert preorder to BST
root = preorderToBST(bst_preorder)


# Print the inorder traversal of the BST
print(inorderTraversal(root))
