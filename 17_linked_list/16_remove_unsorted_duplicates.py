# Class for node -> singly linked list node
class Node(object):
    # Constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Function to print linked list
def print_linked_list(head):
    # Temp node to traverse
    temp = head

    # Traverse till last node
    while temp is not None:
        # Print the node value
        print(temp.data, end=" ")

        # Move to next node
        temp = temp.next

    # Add line break
    print()


# Function to add node to tail
def insert_at_tail(head, data):
    # If head is None
    if head == None:
        # Set the new node to head
        head = Node(data)

    # Else
    else:
        # Initialize temp with head for traversal
        temp = head

        # Traverse to find the last node
        while temp.next is not None:
            # Move to next node
            temp = temp.next

        # Create a new node and add the node to the tail
        temp.next = Node(data)

        # Delete the temp variable
        del temp


# Function to remove duplicates in sorted linked list
def unique_unsorted_list(head):
    # If list is empty or head is only element
    if head is None or head.next is None:
        return head

    # Create a set to track visited values
    visited = set()

    # Initialize pointers to traverse the linked list
    curr = head
    prev = None

    # Traverse the linked list
    while curr is not None:
        # Check if the current value is already visited
        if curr.data in visited:
            # Remove the current node
            prev.next = curr.next

        else:
            # Add the current value to the visited set
            visited.add(curr.data)

            # Move the previous pointer to the current node
            prev = curr

        # Move the current pointer to the next node
        curr = curr.next

    # Return the new head
    return head


# Initialize a linked list
head = Node(4)
insert_at_tail(head, 2)
insert_at_tail(head, 5)
insert_at_tail(head, 4)
insert_at_tail(head, 2)
insert_at_tail(head, 2)
insert_at_tail(head, -1)


# Print linked list
print_linked_list(head)


# Call the function to remove duplicates
head = unique_unsorted_list(head)


# Print linked list
print_linked_list(head)
