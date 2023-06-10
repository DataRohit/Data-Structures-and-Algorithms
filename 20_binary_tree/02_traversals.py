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


# Level order traversal of binary tree
def level_order_traversal(root):
    # List to store the level order traversal
    level_order = []

    # Function for level order traversal
    def function():
        # Return if root is None
        if root is None:
            return

        # Initialize a queue
        queue = []

        # Push the root node to queue
        queue.append(root)

        # Iterate while queue is not empty
        while queue:
            # Pop the first node from queue
            node = queue.pop(0)

            # Add the data of the popped node to list
            level_order.append(node.data)

            # Push the left child of the popped node to queue
            if node.left:
                queue.append(node.left)

            # Push the right child of the popped node to queue
            if node.right:
                queue.append(node.right)

    # Call the function
    function()

    # Return the list
    return level_order


# Reverse level order traversal of binary tree
def reverse_level_order_traversal(root):
    # List to store the elements
    level_order = []

    # Function for level order traversal
    def function():
        # Return if root is None
        if root is None:
            return

        # Initialize a queue
        queue = []

        # Create a new node with the entered data
        queue.append(root)

        # Loop until queue is empty
        while queue:
            # Pop the first node from queue
            node = queue.pop(0)

            # Push the node's data to the stack
            level_order.append(node.data)

            # Push the right child of the popped node to queue
            if node.right:
                queue.append(node.right)

            # Push the left child of the popped node to queue
            if node.left:
                queue.append(node.left)

    # Call the function
    function()

    # Return the reversed list for reverse level order traversal
    return level_order[::-1]


# Inorder traversal of binary tree
def inorder_traversal(root):
    # List to store the inorder traversal
    inorder = []

    # Function for inorder traversal
    def function(root=root):
        # Traverse the left subtree
        if root.left:
            function(root.left)

        # Add the data of the root node to list
        inorder.append(root.data)

        # Traverse the right subtree
        if root.right:
            function(root.right)

    # Call the function
    function()

    # Return the list
    return inorder


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


# Postorder traversal of binary tree
def postorder_traversal(root):
    # List to store the postorder traversal
    postorder = []

    # Function for postorder traversal
    def function(root=root):
        # Traverse the left subtree
        if root.left:
            function(root.left)

        # Traverse the right subtree
        if root.right:
            function(root.right)

        # Add the data of the root node to list
        postorder.append(root.data)

    # Call the function
    function()

    # Return the list
    return postorder


# Input array representing the binary tree
input_arr = [1, 3, 5, 7, 11, 17, None]

"""

The above input array represents the following binary tree:

                1
        3               5
    7       11      17    None

"""


# Build the binary tree from the array
root_node = build_binary_tree(input_arr, None, 0, len(input_arr))


# Level order traversal of the binary tree
print("\nLevel order traversal of binary tree:")
print(*level_order_traversal(root_node))


# Reverse level order traversal of the binary tree
print("\nReverse level order traversal of binary tree:")
print(*reverse_level_order_traversal(root_node))


# Inorder traversal of the binary tree
print("\nInorder traversal of binary tree:")
print(*inorder_traversal(root_node))


# Preorder traversal of the binary tree
print("\nPreorder traversal of binary tree:")
print(*preorder_traversal(root_node))


# Postorder traversal of the binary tree
print("\nPostorder traversal of binary tree:")
print(*postorder_traversal(root_node))
