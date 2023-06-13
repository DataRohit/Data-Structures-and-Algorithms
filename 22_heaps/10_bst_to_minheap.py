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


# Function to print inorder traversal
def inorderTraversal(root):
    # If root is none
    if root is None:
        # Return empty list
        return []

    # List to store inorder
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


# Function to print inorder traversal
def preorderTraversal(root):
    # If root is none
    if root is None:
        # Return empty list
        return []

    # List to store preorder
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


# Recursive function to build the minheap tree
def buildMinHeapTree(root, inorder):
    # If leaf node
    if root is None:
        # Return
        return

    # Insert the data into tree
    root.data = inorder.pop(0)

    # Traverse into left subtree
    buildMinHeapTree(root.left, inorder)

    # Traverse into right subtree
    buildMinHeapTree(root.right, inorder)

    # Return the root
    return root


# Function to return preorder traversal of min heap
def convertBST(root):
    # Get inorder traversal of the binary tree
    inorder = inorderTraversal(root)

    # Recursive function to build the minheap
    root = buildMinHeapTree(root, inorder)

    # Print preorder traversal
    print(*preorderTraversal(root))


# Input array of elements for binary tree
arr = [8, 5, 10, 2, 6, -1, -1, -1, -1, -1, 7, -1, -1]


# Build the binary tree
root = build_binary_tree(arr, None, 0, len(arr))


# Function call to convert BST to min heap
convertBST(root)
