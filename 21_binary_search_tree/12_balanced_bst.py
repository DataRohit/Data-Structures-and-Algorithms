# Initialize node structure of binary tree
class Node(object):
    # Constructor to initialize node
    def __init__(self, data=None):
        # Assign data to current node
        self.data = data

        # Initialize left and right children as None
        self.left = None
        self.right = None


# Function to insert node in bst
def insertIntoBST(root, data):
    # If tree is empty, return a new node
    if root is None:
        return Node(data)

    # If current data < root data
    if data < root.data:
        # Insert data in left subtree
        root.left = insertIntoBST(root.left, data)

    # If current data > root data
    else:
        # Insert data in right subtree
        root.right = insertIntoBST(root.right, data)

    # Return the root node
    return root


# Function to construct BST from given array
def constructBst(bst_elements):
    # Initialize root node as None
    root = None

    # Iterate over the bst_elements
    for element in bst_elements:
        # Insert each element into the BST
        root = insertIntoBST(root, element)

    # Return root node
    return root


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


# Function to build tree from inorder
def inorderToBST(s, e, inorder):
    # Base case
    if s > e:
        # Return none
        return None

    # Find the mid position
    mid = (s + e) // 2

    # Create a node using the mid value
    root = Node(inorder[mid])

    # Recursive call for left and right
    root.left = inorderToBST(s, mid - 1, inorder)
    root.right = inorderToBST(mid + 1, e, inorder)

    # Return root node
    return root


# Function to return the balanced BST root node
def balancedBst(root):
    # Get inorder of the tree
    inorder = inorderTraversal(root)

    # Return the new root node
    return inorderToBST(0, len(inorder) - 1, inorder)


# Take user input for elements of the BST
bst_elements = list(map(int, input().split()))


# Construct BST from given array
root = constructBst(bst_elements)


# Print the inorder traversal of the BST
print(inorderTraversal(root))


# Get the root node of the balanced BST
root = balancedBst(root)


# Print the inorder traversal of the balanced BST
print(inorderTraversal(root))
