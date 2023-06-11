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


# Function to print level order traversal of BST
def levelOrderTraversal(root):
    # If tree is empty, return
    if not root:
        return []

    # List to store level order traversal
    result = []

    # Initialize queue
    queue = []

    # Add root node to queue
    queue.append(root)

    # Iterate while queue is not empty
    while queue:
        # Get the size of queue
        level_size = len(queue)

        # List to store current level nodes
        current_level = []

        # Iterate over the queue
        for _ in range(level_size):
            # Get the first node in queue
            node = queue.pop(0)

            # Add node data to current level list
            current_level.append(node.data)

            # If left child exists, add to queue
            if node.left:
                queue.append(node.left)

            # If right child exists, add to queue
            if node.right:
                queue.append(node.right)

        # Add current level list to result list
        result += current_level

    # Return the result list
    return result


# Inorder traversal of binary tree
def inorderNodeTraversal(root):
    # List to store the inorder traversal
    inorder = []

    # Traverse the left subtree
    if root.left:
        inorder += inorderNodeTraversal(root.left)

    # Add the root node to list
    inorder.append(root)

    # Traverse the right subtree
    if root.right:
        inorder += inorderNodeTraversal(root.right)

    # Return the list
    return inorder


# Function to flatten and return the root node
def flatten(root):
    # Get the nodes in inorder
    inorder = inorderNodeTraversal(root)

    # Store the length of inorder list
    nodesCount = len(inorder)

    # Make first node as root node
    root = inorder[0]

    # Temp variable to store current node
    curr = root

    # Traverse till we reach last node
    for i in range(1, nodesCount):
        # Add the next node to right of current node
        curr.right = inorder[i]

        # Set left subtree to none
        curr.left = None

        # Update current node
        curr = curr.right

    # Fix last node
    curr.left = curr.right = None

    # Return root node
    return root


# Take user input for elements of the BST
bst_elements = list(map(int, input().split()))


# Construct BST from given array
root = constructBst(bst_elements)


# Print level traversal of the BST
print(levelOrderTraversal(root))


# Flatten the BST
root = flatten(root)


# Print level order traversal of the flattened BST
print(levelOrderTraversal(root))
