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


# Recursive function to search for x in BST
def recursiveSearchInBST(root, x):
    # Base case -> Root is none
    if root is None:
        return False

    # Element found at root
    if root.data == x:
        # Return True
        return True

    # If root data > element
    if root.data > x:
        # Search in left subtree
        return recursiveSearchInBST(root.left, x)

    # Else
    else:
        # Search in right subtree
        return recursiveSearchInBST(root.right, x)


# Iterative function to search for x in BST
def iterativeSearchInBST(root, x):
    # Store the root node in temp
    temp = root

    # Iterate while temp is not None
    while temp:
        # If data found at temp
        if temp.data == x:
            # Return True
            return True

        # If temp data greater than x
        elif temp.data > x:
            # Move to left subtree
            temp = temp.left

        # Else
        else:
            # Move to right subtree
            temp = temp.right

    # Else
    else:
        # Return False
        return False


# Take user input for element to search in BST
x = int(input())


# Take user input for elements of the BST
bst_elements = list(map(int, input().split()))


# Construct BST from given array
root = constructBst(bst_elements)


# Search for x in BST
if recursiveSearchInBST(root, x):
    print("Found")

else:
    print("Not Found")


# Search for x in BST
if iterativeSearchInBST(root, x):
    print("Found")

else:
    print("Not Found")
