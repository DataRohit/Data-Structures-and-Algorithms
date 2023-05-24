# Import SinglyLinkedList from the module
# NOTE: Classes to implement linked list are coded in `linked_list_classes.py` file
from linked_list_classes import SinglyLinkedList


# Function to reverse linked list in group of k elements
def k_reverse(head, k):
    # Base case -> If head is None
    if head is None:
        return None

    # Step 1: Reverse first k nodes
    next = None
    curr = head
    prev = None

    # Count the no of elements traversed
    count = 0

    # Loop till we reach last node and also elements traversed < k
    while curr != None and count < k:
        # Update the links in first k elements
        next = curr.next
        curr.next = prev

        # Move to further nodes
        prev = curr
        curr = next

        # Update the count
        count += 1

    # Step 2: Recursion
    if next != None:
        head.next = k_reverse(next, k)

    # Step 3: Return node
    return prev


# Initialize a singly linked list
sll = SinglyLinkedList()


# Set the head value and add data to linked list
sll.head = sll.Node(5)
sll.insert_at_tail(4)
sll.insert_at_tail(3)
sll.insert_at_tail(7)
sll.insert_at_tail(9)
sll.insert_at_tail(2)
sll.insert_at_tail(-1)


# Print original linked list
sll.print_linked_list()


# Take user input for value of k
k = int(input())


# Reverse the linked lest and get new head
sll.head = k_reverse(sll.head, k)


# Print original linked list
sll.print_linked_list()
