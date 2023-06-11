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


# Inorder traversal of binary tree
def inorderTraversal(root):
    # If root is None
    if root is None:
        # Return empty list
        return []

    # List to store the inorder traversal
    inorder = []

    # Traverse the left subtree
    if root.left:
        inorder += inorderTraversal(root.left)

    # Add the data of the root node to list
    inorder.append(root.data)

    # Traverse the right subtree
    if root.right:
        inorder += inorderTraversal(root.right)

    # Return the list
    return inorder


# Function to flatten the BST into a sorted doubly linked list
def flatten(root):
    # Base case  -> If root is None
    if root is None:
        # Return None
        return None

    # Helper function to perform inorder traversal
    def inorder(node, prev):
        # Access the global variable head
        nonlocal head

        # If node is not None
        if node:
            # Traverse the left subtree
            prev = inorder(node.left, prev)

            # If prev is not None
            if prev:
                # Add current node to the right of previous node
                prev.right = node

                # Make previous node as left child of current node
                node.left = prev

            # If prev is None
            else:
                # Update head node
                head = node

            # Update prev node
            prev = node

            # Traverse the right subtree
            prev = inorder(node.right, prev)

        # Return prev node
        return prev

    # Initialize head node as None
    head = None

    # Perform inorder traversal
    inorder(root, None)

    # Return head node
    return head


# Function to merge two sorted doubly linked lists
def merge(head1, head2):
    # If either of the list is None, return the other list
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # Create a dummy node
    dummy = Node(None)

    # Create a pointer to dummy node
    curr = dummy

    # Traverse both the lists
    while head1 and head2:
        # If data of head1 < data of head2
        if head1.data < head2.data:
            # Add head1 to the list
            curr.right = head1

            # Make head1 as left child of curr
            head1.left = curr

            # Update head1
            head1 = head1.right

        # If data of head1 > data of head2
        else:
            # Add head2 to the list
            curr.right = head2

            # Make head2 as left child of curr
            head2.left = curr

            # Update head2
            head2 = head2.right

        # Update curr
        curr = curr.right

    # If head1 is not None
    if head1:
        # Add head1 to the list
        curr.right = head1

        # Make head1 as left child of curr
        head1.left = curr

    # If head2 is not None
    if head2:
        # Add head2 to the list
        curr.right = head2

        # Make head2 as left child of curr
        head2.left = curr

    # Return the head of the merged list
    return dummy.right


# Function to build a balanced BST from a sorted doubly linked list
def buildBalancedBST(head):
    # Base case -> If head is None
    if head is None:
        # Return None
        return None

    # Find the middle node of the linked list using slow and fast pointer approach
    slow = head
    fast = head

    # Initialize prev node as None
    prev = None

    # Iterate until fast and fast.right exist
    while fast and fast.right:
        # Update prev node
        prev = slow

        # Move slow by one step
        slow = slow.right

        # Move fast by two steps
        fast = fast.right.right

    # Create a new node with data as slow.data
    node = Node(slow.data)

    # If prev is not None
    if prev:
        # Make prev.right as None
        prev.right = None

        # Build the left subtree
        node.left = buildBalancedBST(head)

    # Build the right subtree
    node.right = buildBalancedBST(slow.right)

    # Return the root node
    return node


# Take user input for elements of the BST1 and BST2
bst_elements_1 = list(map(int, input().split()))
bst_elements_2 = list(map(int, input().split()))


# Construct BST from given array
root1 = constructBst(bst_elements_1)
root2 = constructBst(bst_elements_2)


# Print inorder traversal of the first and second BST
print(inorderTraversal(root1))
print(inorderTraversal(root2))


# Flatten the both BST into a sorted doubly linked list
head1 = flatten(root1)
head2 = flatten(root2)


# Merge the two sorted doubly linked lists
head = merge(head1, head2)


# Build a balanced BST from the sorted doubly linked list
root = buildBalancedBST(head)


# Print inorder traversal of the merged BST
print(inorderTraversal(root))
