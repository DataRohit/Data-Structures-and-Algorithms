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
        return None

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
            # Loop detected -> return intersection node
            return slow_ptr

    # No loop detected
    return None


# Function to get the staring node of the loop
def get_loop_start_node(head):
    # Base case -> check for empty linked list
    if head is None:
        return False

    # Get the intersection
    intersection = floyd_cycle_detection(head)

    # Check if loop actually exists
    if intersection is None:
        # Return None
        return None

    # Set slow pointer to head
    slow_ptr = head

    # Traverse till slow and intersection pointer meets
    while slow_ptr is not intersection:
        # Update slow and intersection pointer by 1 node
        slow_ptr = slow_ptr.next
        intersection = intersection.next

    # Return the loop start node
    return slow_ptr


# Function to remove the loop from the linked list
def remove_loop(head):
    # Base case -> check for empty linked list
    if head is None:
        return

    # Store the start of loop
    start_of_loop = get_loop_start_node(head)

    # Check if loop exist
    if start_of_loop is None:
        return

    # Initialize variable for traversing
    temp = start_of_loop

    # Traverse to find the node pointing to start_of_loop
    while temp.next is not None and temp.next is not start_of_loop:
        # Update the temp
        temp = temp.next

    # Remove the loop by pointing the last node to None
    temp.next = None

    # Delete vars
    del start_of_loop, temp


# Set the head value of linked list
n1 = head = Node(1)
n2 = n1.next = Node(2)
n3 = n2.next = Node(3)
n4 = n3.next = Node(4)
n5 = n4.next = Node(5)
n6 = n5.next = Node(6)


# Call the function to check if loop exist
print(
    get_loop_start_node(head).data
    if get_loop_start_node(head)
    else get_loop_start_node(head)
)


# Add a loop
n6.next = n3


# Call the function to check if loop exist
print(
    get_loop_start_node(head).data
    if get_loop_start_node(head)
    else get_loop_start_node(head)
)


# Call the function to remove the loop
remove_loop(head)


# Call the function to check if loop exist
print(
    get_loop_start_node(head).data
    if get_loop_start_node(head)
    else get_loop_start_node(head)
)
