# Import SinglyLinkedList from the module
# NOTE: Classes to implement linked list are coded in `linked_list_classes.py` file
from linked_list_classes import SinglyLinkedList


# Function to return middle node of linked list
def find_middle(head):
    # Main two pointers
    slow_ptr = fast_ptr = head

    # Traverse the linked list with different speeds
    while fast_ptr is not None and fast_ptr.next is not None:
        # Slow pointer moves one node at a time
        slow_ptr = slow_ptr.next

        # Fast pointer moves two nodes at a time
        fast_ptr = fast_ptr.next.next

    # Return the middle node
    return slow_ptr


# Initialize a singly linked list
sll1 = SinglyLinkedList()


# Set the head value and add data to linked list
sll1.head = sll1.Node(4)
sll1.insert_at_tail(0)
sll1.insert_at_tail(32)
sll1.insert_at_tail(5)
sll1.insert_at_tail(48)
sll1.insert_at_tail(6)
sll1.insert_at_tail(-1)


# Print original linked list
sll1.print_linked_list()


# Print the data at middle node
print(find_middle(sll1.head).data)


# Initialize a singly linked list
sll2 = SinglyLinkedList()


sll2.head = sll2.Node(1)
sll2.insert_at_tail(2)
sll2.insert_at_tail(3)
sll2.insert_at_tail(4)
sll2.insert_at_tail(5)
sll2.insert_at_tail(-1)


# Print original linked list
sll2.print_linked_list()


# Print the data at middle node
print(find_middle(sll2.head).data)
