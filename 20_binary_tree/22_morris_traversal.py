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
def buildBinaryTree(arr, root, i, n):
    # Base case: If current index exceeds the array size or the element is None,
    # return the node as None
    if i >= n or arr[i] is None:
        return None

    # Create a new node with the current element in the array
    root = Node(arr[i])

    # Recursively build the left and right subtrees
    root.left = buildBinaryTree(arr, root.left, 2 * i + 1, n)
    root.right = buildBinaryTree(arr, root.right, 2 * i + 2, n)

    # Return the root node
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


# Morris traversal to retrieve the preorder traversal of binary tree
def morrisPreorder(root):
    # List to store the preorder traversal
    preorder = []

    # Start with the root node
    current = root

    # Traverse till current node is not none
    while current:
        # If left child not exist
        if current.left is None:
            # Visit the current node
            preorder.append(current.data)

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

                # Visit the current node
                preorder.append(current.data)

                # Move the current to left child
                current = current.left

            # If right child of predecessor exist i.e. Temporary link exist
            else:
                # Break the temporary link
                pre.right = None

                # Move the current to right child
                current = current.right

    # Return the preorder traversal
    return preorder


# Function to perform Morris Traversal and return the postorder traversal as a list
def morrisPostorder(root):
    # List to store the postorder traversal
    postorder = []

    # Helper function to reverse the nodes in a given range
    def reverseNodes(start, end):
        # Base case -> If start and end are same
        if start == end:
            # Return start node
            return start

        # Initialize previous node to None
        prev = None

        # Initialize current node to start
        curr = start

        # Iterate till prev is not equal to end
        while prev != end:
            # Store the next node
            next = curr.right

            # Reverse the link between current and next node
            curr.right = prev

            # Update the previous node to current node
            prev = curr

            # Update the current node to next node
            curr = next

        return prev

    # Create a dummy node to handle the rightmost node
    dummy = Node(-1)

    # Set the left child of dummy node to root
    dummy.left = root

    # Set the current node to dummy
    current = dummy

    # Loop till current node is not None
    while current is not None:
        # If left child is None
        if current.left is None:
            # Move to right child
            current = current.right

        # Else
        else:
            # Find the rightmost child in left subtree

            # Move into left subtree
            pre = current.left

            # If right child exist
            while pre.right is not None and pre.right != current:
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

                # Reverse the nodes from left child to current node
                prev = reverseNodes(current.left, pre)

                # Store the rightmost node
                temp = prev

                # Traverse the reversed nodes
                while temp is not None:
                    # Visit the node
                    postorder.append(temp.data)

                    # Move to right
                    temp = temp.right

                # Reverse the nodes again to retain the original structure of the tree
                current = current.right

    # Return the postorder traversal
    return postorder


# Input array representing the binary tree
input_arr = tree = [1, 2, 3, 4, None, 5, 6, None, None, None, None, 7]

"""
The above binary tree will look like this:

       1
      / \
     2   3
    /     \
   4       5
  / \
 6   7
"""

# Build the binary tree from the array
root_node = buildBinaryTree(input_arr, None, 0, len(input_arr))


# Print the inorder traversal of the binary tree using Morris traversal
print(morrisInorder(root_node))


# Print the preorder traversal of the binary tree using Morris traversal
print(morrisPreorder(root_node))


# Print the postorder traversal of the binary tree using Morris traversal
print(morrisPostorder(root_node))
