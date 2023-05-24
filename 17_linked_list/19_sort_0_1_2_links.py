# Class for node -> singly linked list node
class Node(object):
    # Constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Function to print linked list
def print_linked_list(head):
    # Temp node to traverse
    temp = head

    # Traverse till last node
    while temp is not None:
        # Print the node value
        print(temp.data, end=" ")

        # Move to next node
        temp = temp.next

    # Add line break
    print()


# Function to add node to tail
def insert_at_tail(head, data):
    # If head is None
    if head == None:
        # Set the new node to head
        head = Node(data)

    # Else
    else:
        # Initialize temp with head for traversal
        temp = head

        # Traverse to find the last node
        while temp.next is not None:
            # Move to next node
            temp = temp.next

        # Create a new node and add the node to the tail
        temp.next = Node(data)

        # Delete the temp variable
        del temp


# Function to populate a linked list -> insert at tail
def populate(tail, curr):
    # Add curr at end
    tail.next = curr

    # Update tail pointer
    tail = curr

    # Return the tail node
    return tail


# Function to sort the linked list by changing links
def sort_list_change_link(head):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    # Create dummy nodes
    zero_head = Node(-1)
    zero_tail = zero_head

    one_head = Node(-1)
    one_tail = one_head

    two_head = Node(-1)
    two_tail = two_head

    # Variable to track the current node
    curr = head

    # Loop till we reach last node
    while curr is not None:
        # Get the value at current node
        value = curr.data

        # If data is 0
        if value == 0:
            # Update the zero linked list
            zero_tail = populate(zero_tail, curr)

        # Elif data is 1
        elif value == 1:
            # Update the one linked list
            one_tail = populate(one_tail, curr)

        # Elif data is 2
        elif value == 2:
            # Update the two linked list
            two_tail = populate(two_tail, curr)

        # Move to next node
        curr = curr.next

    # Merge linked list
    if one_head.next is not None:
        zero_tail.next = one_head.next
        one_tail.next = two_head.next
    else:
        zero_tail.next = two_head.next

    two_tail.next = None

    # Delete the pointers
    del zero_tail, one_head, one_tail, two_head, two_tail, curr

    # Return the new head
    return zero_head.next


# Initialize the linked list
head = Node(1)
insert_at_tail(head, 0)
insert_at_tail(head, 2)
insert_at_tail(head, 1)
insert_at_tail(head, 2)


# Print linked list
print_linked_list(head)


# Call the function to sort the list and return new head by updating link
head = sort_list_change_link(head)


# Print linked list
print_linked_list(head)
