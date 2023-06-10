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


# Function to perform level order traversal of the binary tree
def levelOrderTraversal(root):
    # If root is None, return an empty list
    if root is None:
        return []

    # Create an empty list to store the result
    result = []

    # Initialize a queue and enqueue root node
    queue = [root]

    # Loop till queue is empty
    while queue:
        # Pop the front node from the queue
        node = queue.pop(0)

        # If node is not None
        if node is not None:
            # Append the data to the result
            result.append(node.data)

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)
            else:
                queue.append(None)

            # Enqueue right child
            if node.right is not None:
                queue.append(node.right)
            else:
                queue.append(None)

        # Else append None to the result
        else:
            result.append(None)

    # Return the result
    return result


# Function to return the root of flattened binary tree
def flatten(root):
    # Initialize current node to root
    curr = root

    # Loop till current node is None
    while curr is not None:
        # If left child exist
        if curr.left:
            # Find the right most child in left sub tree

            # Move to left sub tree
            pred = curr.left

            # Find right most child
            while pred.right:
                # Update pred
                pred = pred.right

            # Link pred to the right sub tree of current node
            pred.right = curr.right

            # Add the left sub tree of the curr to right
            curr.right = curr.left

            # Make left child none
            curr.left = None

        # Move to right child
        curr = curr.right


# Input array representing the binary tree
input_arr = [1, 2, 3, 4, 5, None, 7, None, None, 8]


# Build the binary tree from the array
root_node = buildBinaryTree(input_arr, None, 0, len(input_arr))


# Print the level order traversal of the binary tree
print(levelOrderTraversal(root_node))


# Function to flatten the binary tree
flatten(root_node)


# Print the level order traversal of the flattened binary tree
print(levelOrderTraversal(root_node))
