# Import collections for deque
from collections import *


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


# Function to create node to parent mapping
# Function to find and return the target node
def createNodeToParentMapping(root, target):
    # Dict to store mapping
    nodeToParent = {}

    # Temp node to store the target node
    targetNode = None

    # Queue for level order traversal
    # Initialize queue with root node
    q = deque([root])

    # Set parent of root node to None
    nodeToParent[root] = None

    # Traverse till queue is empty
    while q:
        # Pop and store the front element
        front = q.popleft()

        # If front node is target node
        if front.data == target:
            # Update targetNode
            targetNode = front

        # If left exist
        if front.left:
            # Update mapping
            nodeToParent[front.left] = front

            # Push left node to queue
            q.append(front.left)

        # If right exist
        if front.right:
            # Update mapping
            nodeToParent[front.right] = front

            # Push right node to queue
            q.append(front.right)

    # Return the answer
    return nodeToParent, targetNode


# Function to burn the tree
def burnTree(targetNode, nodeToParent):
    # Variable to track time
    time = 0

    # List to store visited nodes
    visited = []

    # Queue for level order traversal
    # Initialize queue with targetNode node
    q = deque([targetNode])

    # Set targetNode node to visited
    visited.append(targetNode)

    # Traverse till queue is empty
    while q:
        # Get size of queue
        qSize = len(q)

        # Flag to track if node burnt (added to queue) or not
        flag = False

        # Process all elements of queue -> all connected nodes
        for i in range(qSize):
            # Get the front of queue
            front = q.popleft()

            # If left node exist and left node not visited
            if front.left and front.left not in visited:
                # Update the flag
                flag = True

                # Push the node to queue
                q.append(front.left)

                # Mark left node to visited
                visited.append(front.left)

            # If right node exist and right node not visited
            if front.right and front.right not in visited:
                # Update the flag
                flag = True

                # Push the node to queue
                q.append(front.right)

                # Mark right node to visited
                visited.append(front.right)

            # If parent node exist
            if nodeToParent[front] and nodeToParent[front] not in visited:
                # Update the flag
                flag = True

                # Push the node to queue
                q.append(nodeToParent[front])

                # Mark right node to visited
                visited.append(nodeToParent[front])

        # If node added to queue (node burnt)
        if flag:
            # Increment the time
            time += 1

    # Return time
    return time


# Input array representing the binary tree
input_arr = [1, 2, 3, 4, None, None, 5, None, None, None, None]


# Target node to start burning from
target = 2


# Build the binary tree from the array
root_node = build_binary_tree(input_arr, None, 0, len(input_arr))


# Call the function to get the mapping dict and get target node
nodeToParent, targetNode = createNodeToParentMapping(root_node, target)

# Call the function and store the answer
ans = burnTree(targetNode, nodeToParent)

# Return the answer
print(ans)
