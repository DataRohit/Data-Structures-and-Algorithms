# Import SinglyCircularLinkedList from the module
# NOTE: Classes to implement linked list are coded in `linked_list_classes.py` file
from linked_list_classes import SinglyCircularLinkedList


# Initialize a singly circular linked list
scll = SinglyCircularLinkedList()


# Set the head value of linked list
scll.head = scll.Node(10)
scll.print_linked_list()


# # Print the linked list using iteration and list comprehension
# print([node.data for node in scll])


# Insert node at head
scll.insert_at_head(12)
scll.print_linked_list()


# Insert node at head
scll.insert_at_head(14)
scll.print_linked_list()


# Insert node at tail
scll.insert_at_tail(16)
scll.print_linked_list()


# Insert node at tail
scll.insert_at_tail(18)
scll.print_linked_list()


# Insert node at index
scll.insert_at_index(20, 2)
scll.print_linked_list()


# Insert node at index
scll.insert_at_index(22, 5)
scll.print_linked_list()


# Fetch the length of the linked list using the __len__ prebuilt method
print(len(scll))


# Print original list before deletion of elements
scll.print_linked_list()


# Delete node at head
scll.delete_at_head()
scll.print_linked_list()


# Delete node at tail
scll.delete_at_tail()
scll.print_linked_list()


# Delete node at index
scll.delete_at_index(4)
scll.print_linked_list()


# Insert node at tail
scll.insert_at_tail(20)
scll.print_linked_list()


# Insert node at tail
scll.insert_at_tail(16)
scll.print_linked_list()


# Delete node by value
scll.delete_by_value(16)
scll.print_linked_list()


# update node at index
scll.update_at_index(3, 40)
scll.print_linked_list()
