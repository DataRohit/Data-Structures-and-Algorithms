# Class for node -> singly linked list node
class Node(object):
    """
    Class for a node in the singly linked list.
    """

    # Constructor
    def __init__(self, data=None):
        """
        Initializes a node with the given data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None


# Function to detect loop in a linked list
def detect_loop(head):
    # Base case -> check for empty linked list
    if head is None:
        return False

    # Dictionary to track visited nodes
    visited = {}

    # Create temp for traversal
    temp = head

    # Loop till temp reaches last node
    while temp is not None:
        # Check if node already visited
        try:
            if visited[temp] is True:
                # Cycle is present
                return True
        except:
            # Update the node status and move to next node
            visited[temp] = True
            temp = temp.next

    # Delete the dictionary
    del visited

    # Cycle not detected
    return False


# Set the head value of linked list
n1 = head = Node(1)
n2 = n1.next = Node(2)
n3 = n2.next = Node(3)
n4 = n3.next = Node(4)
n5 = n4.next = Node(5)
n6 = n5.next = Node(6)


# Call the function to check if loop exist
print(detect_loop(head))


# Add a loop
n6.next = n3


# Call the function to check if loop exist
print(detect_loop(head))
