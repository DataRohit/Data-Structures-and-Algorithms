# Import DoublyCircularLinkedList from the module
# NOTE: Classes to implement linked list are coded in `linked_list_classes.py` file
from linked_list_classes import DoublyCircularLinkedList


# Initialize a doubly circular linked list
dcll = DoublyCircularLinkedList()


# Set the head and tail value of linked list
dcll.head = dcll.tail = dcll.Node(10)
dcll.print_linked_list()


# # Print the linked list using iteration and list comprehension
# print([node.data for node in dcll])


# Insert node at head
dcll.insert_at_head(12)
dcll.print_linked_list()


# Insert node at head
dcll.insert_at_head(14)
dcll.print_linked_list()


# Insert node at tail
dcll.insert_at_tail(16)
dcll.print_linked_list()


# Insert node at tail
dcll.insert_at_tail(18)
dcll.print_linked_list()


# Insert node at index
dcll.insert_at_index(20, 2)
dcll.print_linked_list()


# Insert node at index
dcll.insert_at_index(22, 5)
dcll.print_linked_list()


# Fetch the length of the linked list using the __len__ prebuilt method
print(len(dcll))


# Print original list before deletion of elements
dcll.print_linked_list()


# Delete node at head
dcll.delete_at_head()
dcll.print_linked_list()


# Delete node at tail
dcll.delete_at_tail()
dcll.print_linked_list()


# Delete node at index
dcll.delete_at_index(4)
dcll.print_linked_list()


# Insert node at tail
dcll.insert_at_tail(20)
dcll.print_linked_list()


# Insert node at tail
dcll.insert_at_tail(16)
dcll.print_linked_list()


# Delete node by value
dcll.delete_by_value(16)
dcll.print_linked_list()


# update node at index
dcll.update_at_index(3, 40)
dcll.print_linked_list()
