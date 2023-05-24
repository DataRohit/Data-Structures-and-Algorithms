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
def unique_sorted_list(head):
    # If list is empty or head is only element
    if head is None or head.next is None:
        return head

    # Initialize pointer to traverse
    curr = head

    # Traverse till curr reaches end of linked list
    while curr.next is not None:
        # Check if current node value == next node value
        if curr.data == curr.next.data:
            # Remove the node
            curr.next = curr.next.next

        # Else move to next node
        else:
            curr = curr.next

    # Return the final new head
    return head


# Initialize a linked list
head = Node(1)
insert_at_tail(head, 2)
insert_at_tail(head, 2)
insert_at_tail(head, 3)
insert_at_tail(head, -1)


# Print linked list
print_linked_list(head)


# Call the function to remove duplicates
head = unique_sorted_list(head)


# Print linked list
print_linked_list(head)
