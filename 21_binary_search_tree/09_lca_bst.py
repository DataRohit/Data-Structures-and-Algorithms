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


# Function to return the LCA
def LCAinaBST(root, P, Q):
    # Base case -> Root is none
    if root is None:
        # Return none
        return None

    # If root node data less than both the nodes
    if root.data < P.data and root.data < Q.data:
        # Call for right sub tree
        return LCAinaBST(root.right, P, Q)

    # If root node data larger than both the nodes
    elif root.data > P.data and root.data > Q.data:
        # Call for left sub tree
        return LCAinaBST(root.left, P, Q)

    # Else
    else:
        # Current node is answer
        return root


# Input value for nodes to find LCA
P, Q = map(int, input().split())


# Take user input for elements of the BST
bst_elements = list(map(int, input().split()))


# Construct BST from given array
root = constructBst(bst_elements)


# Call the function to get the LCA
lca = LCAinaBST(root, Node(P), Node(Q))


# Print the LCA
print(lca.data)
