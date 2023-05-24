# Import SinglyLinkedList from the module
# NOTE: Classes to implement linked list are coded in `linked_list_classes.py` file
from linked_list_classes import SinglyLinkedList


# Initialize a singly linked list
sll = SinglyLinkedList()


# Set the head value of linked list
sll.head = sll.Node(10)
sll.print_linked_list()


# # Print the linked list using iteration and list comprehension
# print([node.data for node in sll])


# Insert node at head
sll.insert_at_head(12)
sll.print_linked_list()


# Insert node at head
sll.insert_at_head(14)
sll.print_linked_list()


# Insert node at tail
sll.insert_at_tail(16)
sll.print_linked_list()


# Insert node at tail
sll.insert_at_tail(18)
sll.print_linked_list()


# Insert node at index
sll.insert_at_index(20, 2)
sll.print_linked_list()


# Insert node at index
sll.insert_at_index(22, 5)
sll.print_linked_list()


# Fetch the length of the linked list using the __len__ prebuilt method
print(len(sll))


# Print original list before deletion of elements
sll.print_linked_list()


# Delete node at head
sll.delete_at_head()
sll.print_linked_list()


# Delete node at tail
sll.delete_at_tail()
sll.print_linked_list()


# Delete node at index
sll.delete_at_index(4)
sll.print_linked_list()


# Insert node at tail
sll.insert_at_tail(20)
sll.print_linked_list()


# Insert node at tail
sll.insert_at_tail(16)
sll.print_linked_list()


# Delete node by value
sll.delete_by_value(16)
sll.print_linked_list()


# update node at index
sll.update_at_index(3, 40)
sll.print_linked_list()
