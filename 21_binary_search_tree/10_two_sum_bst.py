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
def morrisInorder(root):
    # Initialize an empty list to store the inorder traversal
    inorder = []

    # Start with the root node
    current = root

    # Traverse till current node is not none
    while current:
        # If left child not exist
        if current.left is None:
            # Visit the current node
            inorder.append(current.data)

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

                # Visit the current node
                inorder.append(current.data)

                # Move the current to right child
                current = current.right

    # Return the inorder traversal
    return inorder


# Function to find the two elements summing to target
def twoSumInBST(root, target):
    # Get the inorder traversal of the tree
    inorder = morrisInorder(root)

    # Pointers to track elements
    i, j = 0, len(inorder) - 1

    # Traverse till i < j
    while i < j:
        # Get the sum
        sumElements = inorder[i] + inorder[j]

        # If sum is less than target
        if sumElements < target:
            # Increment i
            i += 1

        # If sum is greater than target
        elif sumElements > target:
            # Decrement i
            j -= 1

        # If sum is equal to the target
        else:
            # Return true
            return True

    # Else
    else:
        # Return false
        return False


# Take user input for k
k = int(input())


# Take user input for elements of the BST
bst_elements = list(map(int, input().split()))


# Construct BST from given array
root = constructBst(bst_elements)


# Call the function to check if the BST contains two nodes whose sum is equal to k
print(twoSumInBST(root, root, k))
