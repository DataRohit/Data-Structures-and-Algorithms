# Import DoublyLinkedList from the module
# NOTE: Classes to implement linked list are coded in `linked_list_classes.py` file
from linked_list_classes import DoublyLinkedList


# Initialize a doubly linked list
dll = DoublyLinkedList()


# Set the head value of linked list
dll.head = dll.Node(10)
dll.print_linked_list()


# # Print the linked list using iteration and list comprehension
# print([node.data for node in dll])


# Insert node at head
dll.insert_at_head(12)
dll.print_linked_list()


# Insert node at head
dll.insert_at_head(14)
dll.print_linked_list()


# Insert node at tail
dll.insert_at_tail(16)
dll.print_linked_list()


# Insert node at tail
dll.insert_at_tail(18)
dll.print_linked_list()


# Insert node at index
dll.insert_at_index(20, 2)
dll.print_linked_list()


# Insert node at index
dll.insert_at_index(22, 5)
dll.print_linked_list()


# Fetch the length of the linked list using the __len__ prebuilt method
print(len(dll))


# Print original list before deletion of elements
dll.print_linked_list()


# Delete node at head
dll.delete_at_head()
dll.print_linked_list()


# Delete node at tail
dll.delete_at_tail()
dll.print_linked_list()


# Delete node at index
dll.delete_at_index(4)
dll.print_linked_list()


# Insert node at tail
dll.insert_at_tail(20)
dll.print_linked_list()


# Insert node at tail
dll.insert_at_tail(16)
dll.print_linked_list()


# Delete node by value
dll.delete_by_value(16)
dll.print_linked_list()


# update node at index
dll.update_at_index(3, 40)
dll.print_linked_list()
