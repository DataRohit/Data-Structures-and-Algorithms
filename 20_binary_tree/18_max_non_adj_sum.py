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


# Recursive function to find the maximum su
def solve(root):
    # Base case -> Root is none
    if root is None:
        # Return [0, 0]
        return [0, 0]

    # Recursive call for left sub tree
    leftAns = solve(root.left)

    # Recursive call for right sub tree
    rightAns = solve(root.right)

    # Initialize result list to store the answer
    res = []

    # Sum including the current node
    res.append(root.data + leftAns[1] + rightAns[1])

    # Sum excluding the current node
    res.append(max(leftAns) + max(rightAns))

    # Return the result
    return res


# Function to return the maximum sum of non-adjacent nodes.
def getMaxSum(root):
    # Get the answer using the recursive solve function
    # ans[0] -> sum including current node
    # ans[1] -> sum excluding current node
    ans = solve(root)

    # Return the maximum element in the answer list
    return max(ans)


# Input array representing the binary tree
input_arr = [1, 2, 3, 1, None, 4, 5]


# Build the binary tree from the array
root_node = build_binary_tree(input_arr, None, 0, len(input_arr))


# Get the maximum sum of non-adjacent nodes
max_sum = getMaxSum(root_node)


# Print the maximum sum of non-adjacent nodes
print(max_sum)
