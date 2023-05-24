# Import SinglyLinkedList from the module
# NOTE: Classes to implement linked list are coded in `linked_list_classes.py` file
from linked_list_classes import SinglyLinkedList


# Function to reverse the linked list
def reverse_linked_list(sll):
    # Only reverse iƒ list is not empty
    if sll.head is not None:
        # Initialize prev and curr node
        prev_node = None
        curr_node = sll.head

        # Loop curr_node is None -> prev_node at last node
        while curr_node is not None:
            # Store the next node for further reversing
            next_node = curr_node.next

            # Reverse the link
            curr_node.next = prev_node

            # Update the prev and curr node
            prev_node = curr_node
            curr_node = next_node

        # Update the head
        sll.head = prev_node

        # Delete the pointers
        del prev_node, curr_node, next_node


# Initialize a singly linked list
sll = SinglyLinkedList()


# Set the head value and add data to linked list
sll.head = sll.Node(3)
sll.insert_at_tail(-2)
sll.insert_at_tail(1)
sll.insert_at_tail(-1)


# Print original linked list
sll.print_linked_list()


# Call the function which replaces the linked list inplace
reverse_linked_list(sll)


# Print reversed linked list
sll.print_linked_list()
