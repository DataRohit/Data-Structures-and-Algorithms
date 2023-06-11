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


# Function to find predecessor and successor for given key
def inorderPredecessorSuccessor(root, key):
    # If root is None
    if root is None:
        # Predecessor and successor don't exist
        return None, None

    # Initialize predecessor and successor as None
    predecessor = None
    successor = None

    # Traverse till root is not None
    while root is not None:
        # If key value is less than root value
        if key < root.data:
            # Root is potential successor
            successor = root

            # Search for key in left subtree
            root = root.left

        # If key value is greater than root value
        elif key > root.data:
            # Root is potential predecessor
            predecessor = root

            # Search for key in right subtree
            root = root.right

        # If key value is equal to root value
        else:
            # If left subtree exists find predecessor
            # Else predecessor is parent
            if root.left is not None:
                # Find maximum value node in left subtree
                predecessor = maxValueNode(root.left)

            # If right subtree exists find successor
            # Else successor is parent
            if root.right is not None:
                # Find minimum value node in right subtree
                successor = minValueNode(root.right)

            # Break the loop
            break

    # Return predecessor and successor
    return (
        predecessor.data if predecessor else None,
        successor.data if successor else None,
    )


# Input value to search predecessor and successor for
key = int(input())


# Take user input for elements of the BST
bst_elements = list(map(int, input().split()))


# Construct BST from given array
root = constructBst(bst_elements)


# Function to print inorder traversal of BST
print(inorderTraversal(root))


# Find predecessor and successor for given key
predecessor, successor = inorderPredecessorSuccessor(root, key)


# Print predecessor and successor
print(predecessor, successor)
