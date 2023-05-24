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


# Function to sort the linked list by updating data
def sort_list_change_data(head):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    # Variables to track the count of 0, 1 and 2
    count_dict = {0: 0, 1: 0, 2: 0}

    # Variable to traverse
    curr = head

    # Loop till we reach last node
    while curr is not None:
        # Check the data and update the respective count
        count_dict[curr.data] += 1

        # Move to next node
        curr = curr.next

    # Reset the curr variable
    curr = head

    # Loop till we reach the last node
    for key, value in count_dict.items():
        # Loop till value becomes 0
        while value != 0 and curr is not None:
            # Update the value at node
            curr.data = key

            # Reduce the value and value in dict
            value -= 1
            count_dict[key] -= 1

            # Move to next node
            curr = curr.next

    # Delete the count dict
    del count_dict, curr, value

    # Return head
    return head


# Initialize the linked list
head = Node(1)
insert_at_tail(head, 0)
insert_at_tail(head, 2)
insert_at_tail(head, 1)
insert_at_tail(head, 2)


# Print linked list
print_linked_list(head)


# Call the function to sort the list and return new head by updating data
head = sort_list_change_data(head)


# Print linked list
print_linked_list(head)
