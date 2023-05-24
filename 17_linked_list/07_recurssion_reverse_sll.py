# Import SinglyLinkedList from the module
# NOTE: Classes to implement linked list are coded in `linked_list_classes.py` file
from linked_list_classes import SinglyLinkedList


def reverse_linked_list(head):
    # Base case: if the list is empty or has only one node
    if head is None or head.next is None:
        return head

    # Reverse the rest of the linked list recursively
    reversed_list = reverse_linked_list(head.next)

    # Update the next pointer of the next node to point back to the current node
    head.next.next = head

    # Set the next pointer of the current node to None (to break the original connection)
    head.next = None

    # Return the new head of the reversed list
    return reversed_list


# Initialize a singly linked list
sll = SinglyLinkedList()


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
