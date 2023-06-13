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


# Function to count nodes in BT
def countNodes(root):
    # Base case -> Root is None
    if root is None:
        # Return 0
        return 0

    # Call for left and right subtree
    ans = 1 + countNodes(root.left) + countNodes(root.right)

    # Return the answer
    return ans


# Function to check if tree is CBT
def isCBT(root, index, totalNodes):
    # Base case -> Root is None
    if root is None:
        # Return True
        return True

    # Base case -> right child filled before left
    if index >= totalNodes:
        # Return False
        return False

    # Else
    else:
        # Get the answer for left and right
        leftAns = isCBT(root.left, 2 * index + 1, totalNodes)
        rightAns = isCBT(root.right, 2 * index + 2, totalNodes)

        # Return the answer
        return leftAns and rightAns


# Function to check if the tree is following MaxHeap property
def isMaxOrder(root):
    # If leaf node
    if root.left is None and root.right is None:
        # Return True
        return True

    # If only left child exist
    if root.right is None:
        # If left child data < root data return True else False
        return root.left.data < root.data

    # If both child exist
    else:
        # Get the answer for left and right subtree
        leftAns = isMaxOrder(root.left)
        rightAns = isMaxOrder(root.right)

        # Check if current node follows the MaxHeap property
        currAns = root.left.data <= root.data and root.right.data <= root.data

        # Return the final answer
        return leftAns and rightAns and currAns


# Function to return True if BT is heap else False
def isBinaryHeapTree(root):
    # Initialize start index to 0
    index = 0

    # Count the total number of nodes in BT
    totalNodes = countNodes(root)

    # If BT is CBT and Follows MaxHeap Property
    if isCBT(root, index, totalNodes) and isMaxOrder(root):
        # Return True
        return True

    # Else
    else:
        # Return False
        return False


# Input for values of BT
treeElements1 = [10, 8, 9, 5, 5, 4, 5, 1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
treeElements2 = [15, 14, 10, 4, 5, 11, 5, 1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]


# Initialize root of BT
root1 = None
root2 = None


# Build the BT
root1 = build_binary_tree(treeElements1, root1, 0, len(treeElements1))
root2 = build_binary_tree(treeElements2, root2, 0, len(treeElements2))


# Print the result
print(isBinaryHeapTree(root1))
print(isBinaryHeapTree(root2))
