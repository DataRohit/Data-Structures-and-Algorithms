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


# Function to find the minimum value node in BST
def minValueNode(node):
    # Temp variable to store current node
    current = node

    # Traverse till left subtree exists
    while current.left is not None:
        # Update current node
        current = current.left

    # Return the minimum value node
    return current


# Function to find the maximum value node in BST
def maxValueNode(node):
    # Temp variable to store current node
    current = node

    # Traverse till right subtree exists
    while current.right is not None:
        # Update current node
        current = current.right

    # Return the maximum value node
    return current


# Function to delete a node from BST
def deleteNode(root, key):
    # Base case -> Root is none
    if root is None:
        # Return root
        return root

    # Base case -> root data == key
    if root.data == key:
        # 0 Children
        if root.left is None and root.right is None:
            # Return None
            return None

        # 1 Child
        elif root.left is None:
            # Return right child
            return root.right

        elif root.right is None:
            # Return left child
            return root.left

        # 2 Children
        if root.left and root.right:
            # Find the minimum value node in right subtree
            temp = minValueNode(root.right)

            # Copy the inorder successor's content to this node
            root.data = temp.data

            # Delete the inorder successor
            root.right = deleteNode(root.right, temp.data)

            # Return root
            return root

    # If key < root data
    elif key < root.data:
        # Delete key from left subtree
        root.left = deleteNode(root.left, key)

        # Return root
        return root

    # If key > root data
    else:
        # Delete key from right subtree
        root.right = deleteNode(root.right, key)

        # Return root
        return root


# Input value to search predecessor and successor for
key = int(input())


# Take user input for elements of the BST
bst_elements = list(map(int, input().split()))


# Construct BST from given array
root = constructBst(bst_elements)


# Function to print inorder traversal of BST
print(inorderTraversal(root))


# Delete the node with given key
root = deleteNode(root, key)


# Print inorder traversal of the modified BST
print(inorderTraversal(root))
