# Initialize node structure of binary tree
class Node(object):
    # Constructor to initialize node
    def __init__(self, data=None):
        # Assign data to current node
        self.data = data

        # Initialize left and right children as None
        self.left = None
        self.right = None


# Function to build a binary tree
def build_binary_tree(root=Node()):
    # Enter the data for node
    data = int(input("Enter data for node: "))

    # Return None if input is -1, indicating no node ahead
    if data == -1:
        return None

    # Create a new node with the entered data
    root = Node(data)

    # Enter left child of the current node
    print(f"\nEnter left child of {root.data}")
    # Recursively build the left subtree
    root.left = build_binary_tree()

    # Enter right child of the current node
    print(f"\nEnter right child of {root.data}")
    # Recursively build the right subtree
    root.right = build_binary_tree()

    # Return root node
    return root


# Function to print the binary tree
def print_binary_tree(root=Node()):
    # Return if root is None
    if root is None:
        return

    # Print the root node
    print(root.data, end=": ")

    # Print the left child
    if root.left is not None:
        print(f"L {root.left.data}", end=", ")

    # Print the right child
    if root.right is not None:
        print(f"R {root.right.data}", end="")

    # Print new line
    print()

    # Recursively print left subtree
    print_binary_tree(root.left)

    # Recursively print right subtree
    print_binary_tree(root.right)


# Initialize a binary tree
bt = Node()


# Build a binary tree and return root node
# Sample Input: 1 3 7 -1 -1 11 -1 -1 5 17 -1 -1 -1
bt = build_binary_tree(bt)


# Print the binary tree
print_binary_tree(bt)
