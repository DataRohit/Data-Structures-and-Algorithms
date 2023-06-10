# Initialize node structure of binary tree
class Node(object):
    # Constructor to initialize node
    def __init__(self, data=None):
        # Assign data to current node
        self.data = data

        # Initialize left and right children as None
        self.left = None
        self.right = None


# Postorder traversal of binary tree
def postorder_traversal(root):
    # Base case: If root is None
    if not root:
        # Return an empty list
        return []

    # List to store the postorder traversal
    result = []

    # Recursively traverse the left subtree
    result.extend(postorder_traversal(root.left))

    # Recursively traverse the right subtree
    result.extend(postorder_traversal(root.right))

    # Add the data of the root node to list
    result.append(root.data)

    # Return the list
    return result


# Recursive function to build the tree
def build_tree(inorder, preorder):
    # Base case -> If inorder or preorder is empty
    if not inorder or not preorder:
        # Return None
        return None

    # Extract the root value from preorder
    root_val = preorder[0]

    # Create a node with root value
    root = Node(root_val)

    # Find the index of root value in inorder
    root_index = inorder.index(root_val)

    # Recursively build the left and right subtree
    root.left = build_tree(inorder[:root_index], preorder[1 : root_index + 1])
    root.right = build_tree(inorder[root_index + 1 :], preorder[root_index + 1 :])

    # Return the root node
    return root


# Take user input for inorder and preorder traversal of a tree and print the tree
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))


# Call the function to build the tree
root = build_tree(inorder, preorder)


# Print the postorder traversal of the tree
print(*postorder_traversal(root))
