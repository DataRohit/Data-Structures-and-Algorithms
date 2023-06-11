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


# Preorder traversal of binary tree
def preorderTraversal(root):
    # If root is None
    if root is None:
        # Return empty list
        return []

    # List to store the preorder traversal
    preorder = []

    # Add the data of the root node to list
    preorder.append(root.data)

    # Traverse the left subtree
    if root.left:
        preorder += preorderTraversal(root.left)

    # Traverse the right subtree
    if root.right:
        preorder += preorderTraversal(root.right)

    # Return the list
    return preorder


# Postorder traversal of binary tree
def postorderTraversal(root):
    # If root is None
    if root is None:
        # Return empty list
        return []

    # List to store the postorder traversal
    postorder = []

    # Traverse the left subtree
    if root.left:
        postorder += postorderTraversal(root.left)

    # Traverse the right subtree
    if root.right:
        postorder += postorderTraversal(root.right)

    # Add the data of the root node to list
    postorder.append(root.data)

    # Return the list
    return postorder


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


# Take user input for elements of the BST
bst_elements = list(map(int, input().split()))


# Construct BST from given array
root = constructBst(bst_elements)


# Print the inorder traversal of the BST
print(inorderTraversal(root))


# Print the preorder traversal of the BST
print(preorderTraversal(root))


# Print the postorder traversal of the BST
print(postorderTraversal(root))
