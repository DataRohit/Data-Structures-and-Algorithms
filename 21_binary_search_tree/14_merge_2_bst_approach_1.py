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
    mid = s + (e - s) // 2

    # Create a node using the mid value
    root = Node(inorder[mid])

    # Recursive call for left and right
    root.left = inorderToBST(s, mid - 1, inorder)
    root.right = inorderToBST(mid + 1, e, inorder)

    # Return root node
    return root


# Function to return the root node of merged trees
def mergeBST(root1, root2):
    # Step 1: Get inorder for root1 and root2
    inorder1 = inorderTraversal(root1)
    inorder2 = inorderTraversal(root2)

    # Step 2: Merge the two inorder into one single list and sort it
    inorder = inorder1 + inorder2

    # Delete the inorder1 and inorder2
    del inorder1, inorder2

    # Step 3: Sort the joined inorder
    inorder.sort()

    # Step 4: Build tree from the inorder and return root node
    return inorderToBST(0, len(inorder) - 1, inorder)


# Take user input for elements of the BST1 and BST2
bst_elements_1 = list(map(int, input().split()))
bst_elements_2 = list(map(int, input().split()))


# Construct BST from given array
root1 = constructBst(bst_elements_1)
root2 = constructBst(bst_elements_2)


# Print inorder traversal of the first and second BST
print(inorderTraversal(root1))
print(inorderTraversal(root2))


# Merge the two BSTs
root = mergeBST(root1, root2)


# Print the inorder traversal of the merged BST
print(inorderTraversal(root))
