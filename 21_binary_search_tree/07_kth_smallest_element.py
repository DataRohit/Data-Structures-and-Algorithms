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


# Morris traversal to retrieve the inorder traversal of binary tree
def morrisInorderKthSmallest(root, k):
    # Initialize counter to 0
    count = 0

    # Variable to store kth smallest element
    kth_smallest = None

    # Start with the root node
    current = root

    # Traverse till current node is not none
    while current:
        # If left child not exist
        if current.left is None:
            # Update the counter
            count += 1

            # If counter is equal to k
            if count == k:
                # Update kth smallest element
                kth_smallest = current.data

            # Update the current node to right child
            current = current.right

        # Else
        else:
            # Find the rightmost child in left subtree

            # Move into left subtree
            pre = current.left

            # If right child exist
            while pre.right and pre.right != current:
                # Move to right
                pre = pre.right

            # If right child of predecessor is None
            if pre.right is None:
                # Update right of predecessor to current node i.e. Establish temporary link
                pre.right = current

                # Move the current to left child
                current = current.left

            # If right child of predecessor exist i.e. Temporary link exist
            else:
                # Break the temporary link
                pre.right = None

                # Update the counter
                count += 1

                # If counter is equal to k
                if count == k:
                    # Update kth smallest element
                    kth_smallest = current.data

                # Move the current to right child
                current = current.right

    # Return the kth smallest element
    return kth_smallest


# Take user input for elements of the BST
bst_elements = list(map(int, input().split()))


# Take user input for k
k = int(input())


# Construct BST from given array
root = constructBst(bst_elements)


# Function call to retrieve the kth smallest element
kth_smallest = morrisInorderKthSmallest(root, k)


# Print the kth smallest element
print(kth_smallest)
