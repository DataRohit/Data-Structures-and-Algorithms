# Import DoublyLinkedList from the module
# NOTE: Classes to implement linked list are coded in `linked_list_classes.py` file
from linked_list_classes import DoublyLinkedList


# Function to reverse the linked list
def reverse_linked_list(head):
    # Base case: if the list is empty or has only one element,
    # no reversal is needed, so we simply return the node itself
    if head is None or head.next is None:
        return head

    # Recursively reverse the sublist starting from the next node
    new_head = reverse_linked_list(head.next)

    # Reverse the current node and its next node

    # Adjust the next pointer of the next node to point back to the current node
    head.next.next = head

    # Adjust the prev pointer of the next node to point to the current node,
    # effectively reversing the direction of the sublist
    head.prev = head.next

    # Set the next pointer of the current node to None to detach it from the reversed sublist
    head.next = None

    # At each recursive step, the new_head is returned, which is the head of the reversed sublist

    # Return the new head of the reversed list
    return new_head


# Initialize a doubly linked list
sll = DoublyLinkedList()


# Set the head value and add data to linked list
sll.head = sll.Node(3)
sll.insert_at_tail(-2)
sll.insert_at_tail(1)
sll.insert_at_tail(-1)


# Print original linked list
sll.print_linked_list()


# Call the function to reverse the linked list and return new head
sll.head = reverse_linked_list(sll.head)


# Print reversed linked list
sll.print_linked_list()
