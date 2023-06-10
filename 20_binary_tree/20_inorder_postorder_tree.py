# Initialize node structure of binary tree
class Node(object):
    # Constructor to initialize node
    def __init__(self, data=None):
        # Assign data to current node
        self.data = data

        # Initialize left and right children as None
        self.left = None
        self.right = None


# Preorder traversal of binary tree
def preorder_traversal(root):
    # List to store the preorder traversal
    preorder = []

    # Function for preorder traversal
    def function(root=root):
        # Add the data of the root node to list
        preorder.append(root.data)

        # Traverse the left subtree
        if root.left:
            function(root.left)

        # Traverse the right subtree
        if root.right:
            function(root.right)

    # Call the function
    function()

    # Return the list
    return preorder


# Recursive function to build the tree
def build_tree(inorder, postorder):
    # Base case -> If inorder or postorder is empty
    if not inorder or not postorder:
        # Return None
        return None

    # Extract the root value from postorder
    root_val = postorder[-1]

    # Create a node with root value
    root = Node(root_val)

    # Find the index of root value in inorder
    root_index = inorder.index(root_val)

    # Recursively build the left and right subtree
    root.left = build_tree(inorder[:root_index], postorder[:root_index])
    root.right = build_tree(inorder[root_index + 1 :], postorder[root_index:-1])

    # Return the root node
    return root


# Take user input for inorder and postorder traversal of a tree and print the tree
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))


# Call the function to build the tree
root = build_tree(inorder, postorder)


# Print the preorder traversal of the tree
print(*preorder_traversal(root))
