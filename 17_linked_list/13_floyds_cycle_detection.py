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


# Floyd's cycle detection algorithm to detect cycle
def floyd_cycle_detection(head):
    # Base case -> check for empty linked list
    if head is None:
        return False

    # Initialize slow and fast pointer
    slow_ptr = fast_ptr = head

    # Loop till slow ptr and fast ptr reach the end node
    while slow_ptr is not None and fast_ptr is not None:
        # Update slow ptr by 1 step
        slow_ptr = slow_ptr.next

        # Update fast ptr by 1 step
        fast_ptr = fast_ptr.next

        # Check if fast can be moved further
        if fast_ptr is not None:
            # Update fast ptr for 2nd step
            fast_ptr = fast_ptr.next

        # Check if slow ptr and fast ptr meet
        if slow_ptr is fast_ptr:
            # Loop detected
            return True

    # No loop detected
    return False


# Set the head value of linked list
n1 = head = Node(1)
n2 = n1.next = Node(2)
n3 = n2.next = Node(3)
n4 = n3.next = Node(4)
n5 = n4.next = Node(5)
n6 = n5.next = Node(6)


# Call the function to check if loop exist
print(floyd_cycle_detection(head))


# Add a loop
n6.next = n3


# Call the function to check if loop exist
print(floyd_cycle_detection(head))
