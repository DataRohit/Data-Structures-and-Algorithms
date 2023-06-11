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
def morrisInorderKthLargest(root, k):
    # Initialize counter to 0
    count = 0

    # Variable to store kth largest element
    kth_largest = None

    # Start with the root node
    current = root

    # Traverse till current node is not none
    while current:
        # If right child not exist
        if current.right is None:
            # Update the counter
            count += 1

            # If counter is equal to k
            if count == k:
                # Update kth largest element
                kth_largest = current.data

            # Update the current node to left child
            current = current.left

        # Else
        else:
            # Find the leftmost child in right subtree

            # Move into right subtree
            suc = current.right

            # If left child exist
            while suc.left and suc.left != current:
                # Move to left
                suc = suc.left

            # If left child of successor is None
            if suc.left is None:
                # Update left of successor to current node i.e. Establish temporary link
                suc.left = current

                # Move the current to right child
                current = current.right

            # If left child of successor exist i.e. Temporary link exist
            else:
                # Break the temporary link
                suc.left = None

                # Update the counter
                count += 1

                # If counter is equal to k
                if count == k:
                    # Update kth largest element
                    kth_largest = current.data

                # Move the current to left child
                current = current.left

    # Return the kth largest element
    return kth_largest


# Take user input for elements of the BST
bst_elements = list(map(int, input().split()))


# Take user input for k
k = int(input())


# Construct BST from given array
root = constructBst(bst_elements)


# Function call to retrieve the kth largest element
kth_largest = morrisInorderKthLargest(root, k)


# Print the kth largest element
print(kth_largest)
