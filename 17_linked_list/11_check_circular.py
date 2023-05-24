# Import SinglyCircularLinkedList from the module
# NOTE: Classes to implement linked list are coded in `linked_list_classes.py` file
from linked_list_classes import SinglyCircularLinkedList


# Function to check for circular linked list
def is_circular(head):
    # If head is already NULL, then it is the circular linked list
    # with length zero.
    if head == None:
        return True

    # If next pointer of head is already NULL, then it the linear linked
    # list of length 1, hence we return false here.
    if head.next == None:
        return False

    # Initializing slow and fast pointers with head.
    slow, fast = head, head

    # Iterating through the linked list till, fast doesn't reach end of
    # linked list or slow pointer will not become equal to fast pointer.
    while fast != None and fast.next != None:
        # Moving slow pointer by one step.
        slow = slow.next

        # Moving fast pointer by two steps.
        fast = fast.next.next

        # Checking if updated slow and fast pointer values are same or not.
        if slow == fast:
            break

    # After completing the traversal, if slow and fast pointers meet and
    # the node of meeting is node pointed by head, then linked list is circular.
    if slow == fast and slow == head:
        return True

    # If linked list is not circular, then return false.
    return False


# Initialize a singly circular linked list
scll = SinglyCircularLinkedList()


# Set the head value of linked list
scll.head = scll.Node(1)
scll.insert_at_head(2)
scll.insert_at_head(3)
scll.insert_at_head(4)
scll.insert_at_head(5)
scll.insert_at_head(6)
scll.insert_at_head(7)


# Print original linked list
scll.print_linked_list()


# Check if list is circular
print(is_circular(scll.head))
