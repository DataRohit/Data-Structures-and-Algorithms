# Import SinglyCircularLinkedList from the module
# NOTE: Classes to implement linked list are coded in `linked_list_classes.py` file
from linked_list_classes import SinglyCircularLinkedList


# Python function to print a circular linked list
def print_circular_linked_list(head):
    # Initialize the variable to iterate
    tail = head

    # Check if the list is empty
    if head is None:
        return head

    # Loop till we reach the head node again
    while True:
        # Print the data of tail node
        print(tail.data, end=" ")

        # Move to the next node
        tail = tail.next

        # Check if we have reached the head node again
        if tail is head:
            break

    # Add a line break
    print()


# Function to break circular linked list into half and return new heads
def break_circular_list(linked_list):
    # Check if linked list is empty or have only one element
    if linked_list.head is None or linked_list.head.next is None:
        return linked_list.head

    # Initialize slow and fast pointers
    head_ptr = slow_ptr = fast_ptr = linked_list.head

    # Traverse till fast pointer cannot be moved forward
    while fast_ptr.next is not head_ptr and fast_ptr.next.next is not head_ptr:
        # Update the slow and fast pointers
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    # Initialize the heads of new linked lists
    head_1 = head_ptr
    head_2 = slow_ptr.next

    # Make the first linked list circular
    slow_ptr.next = head_1

    # Make the second linked list circular
    if fast_ptr.next is head_ptr:
        fast_ptr.next = head_2
    else:
        fast_ptr.next.next = head_2

    # Return new heads
    return head_1, head_2


# Initialize a circular linked list
linked_list_even = SinglyCircularLinkedList()


# Initialize the head and add data to linked list
linked_list_even.head = linked_list_even.Node(1)
linked_list_even.insert_at_tail(2)
linked_list_even.insert_at_tail(3)
linked_list_even.insert_at_tail(4)
linked_list_even.insert_at_tail(5)
linked_list_even.insert_at_tail(6)


# Print circular linked list
print_circular_linked_list(linked_list_even.head)


# Call the function to split the linked list
head_1, head_2 = break_circular_list(linked_list_even)


# Print new linked lists
print_circular_linked_list(head_1)
print_circular_linked_list(head_2)


# Initialize a circular linked list
linked_list_odd = SinglyCircularLinkedList()


# Initialize the head and add data to linked list
linked_list_odd.head = linked_list_odd.Node(1)
linked_list_odd.insert_at_tail(2)
linked_list_odd.insert_at_tail(3)
linked_list_odd.insert_at_tail(4)
linked_list_odd.insert_at_tail(5)
linked_list_odd.insert_at_tail(6)
linked_list_odd.insert_at_tail(7)


# Print circular linked list
print_circular_linked_list(linked_list_odd.head)


# Call the function to split the linked list
head_1, head_2 = break_circular_list(linked_list_odd)


# Print new linked lists
print_circular_linked_list(head_1)
print_circular_linked_list(head_2)
