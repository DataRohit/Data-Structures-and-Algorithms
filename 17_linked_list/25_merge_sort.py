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


# Function to merge second list into first
def solve(first, second):
    # Check if only first element present in first
    if first.next is None:
        # Add second list after first
        first.next = second

        # Return the head of first
        return first

    # Initialize pointers
    curr1 = first
    next1 = curr1.next

    curr2 = second
    next2 = curr2.next

    # Loop till next1 at last element of first list
    # Loop till curr2 at last element of second list
    while next1 is not None and curr2 is not None:
        # Check if element from curr2 be inserted between curr1 and next1
        if curr2.data >= curr1.data and curr2.data <= next1.data:
            # Update the links if element inserted

            # The inserted element will be after curr1
            curr1.next = curr2

            # Move the next pointer of second
            next2 = curr2.next

            # After inserting the element update next of inserted element
            curr2.next = next1

            # Update current pointers
            curr1 = curr2
            curr2 = next2

        # If element cannot be inserted
        else:
            # Update pointers of first
            curr1 = next1
            next1 = next1.next

            # Stop if next1 is None
            if next1 is None:
                # Add the remaining second list at end
                curr1.next = curr2

                # Return the head of first element
                return first

    # Return first
    return first


# Function to return the merged linked list
def merge_two_list(first, second):
    # If first list is empty
    if first is None:
        # Return second list
        return second

    # If second list is empty
    if second is None:
        # Return first list
        return first

    # If first data <= second data
    if first.data <= second.data:
        # Make first list first
        return solve(first, second)

    # If second data < first data
    else:
        # Make second list first
        return solve(second, first)


# Function to find the mid node
def find_mid(head):
    # Main two pointers
    slow_ptr = head
    fast_ptr = head.next

    # Traverse the linked list with different speeds
    while fast_ptr is not None and fast_ptr.next is not None:
        # Slow pointer moves one node at a time
        slow_ptr = slow_ptr.next

        # Fast pointer moves two nodes at a time
        fast_ptr = fast_ptr.next.next

    # Return the middle node
    return slow_ptr


# Function to sort linked list using merge sort
def merge_sort(head):
    # Base case -> Empty or Single element
    if head is None or head.next is None:
        # Return the head node
        return head

    # Call the function to get the mid of the linked list
    mid = find_mid(head)

    # Initialize the heads for left and right sub list
    left_head = head
    right_head = mid.next

    # Point the tail of left list to None
    mid.next = None

    # Recursive call to sort the left and right sub list
    left_list = merge_sort(left_head)
    right_list = merge_sort(right_head)

    # Merge the sorted halves
    new_head = merge_two_list(left_list, right_list)

    # Return the new head
    return new_head


# Initialize a linked list
head = Node(1)
insert_at_tail(head, -2)
insert_at_tail(head, 3)
insert_at_tail(head, -1)


# Print the linked list
print_linked_list(head)


# Call the function and get the head of sorted linked list
new_head = merge_sort(head)


# Print the sorted linked list
print_linked_list(new_head)
