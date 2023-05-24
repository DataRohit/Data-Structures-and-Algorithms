# Class for node -> singly linked list node with child
class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None


# Function to print linked list
def print_linked_list(head):
    # Temp node to traverse
    temp = head

    # Traverse till last node
    while temp is not None:
        # Print the node value
        print(temp.data, end=" ")

        # Move to next node
        temp = temp.child

    # Add line break
    print()


# Function to return the merged linked list
def merge_two_lists(head_1, head_2):
    # If first list is empty
    if head_1 is None:
        # Return second list
        return head_2

    # If second list is empty
    if head_2 is None:
        # Return first list
        return head_1

    # Create a node to store new head
    new_head = None

    # Pointer to track current nodes in both lists
    if head_1.data <= head_2.data:
        new_head = head_1
        head_1 = head_1.child
    else:
        new_head = head_2
        head_2 = head_2.child

    # Current node for merging
    new_curr = new_head

    # Merge the lists
    while head_1 is not None and head_2 is not None:
        if head_1.data <= head_2.data:
            new_curr.child = head_1
            head_1 = head_1.child
        else:
            new_curr.child = head_2
            head_2 = head_2.child

        new_curr.child.next = None
        new_curr = new_curr.child

    # Append the remaining nodes
    if head_1 is not None:
        new_curr.child = head_1
    else:
        new_curr.child = head_2

    # Return the new head
    return new_head


# Function to get the head of flattened linked list
def flatten_linked_list(head):
    # Base case -> If linked list is empty or has only one node
    if head is None:
        return head

    # Get the head node for downward list
    down_head = head
    next_head = head.next

    # Break the downward list from the rightward list
    down_head.next = None

    # Recursive call for flattening the right list
    right_head = flatten_linked_list(next_head)

    # Merge linked lists
    new_head = merge_two_lists(down_head, right_head)

    # Return the new head
    return new_head


# Initialize a linked list
head = Node(1)
head.child = Node(2)
head.child.child = Node(3)

head.next = Node(4)
head.next.child = Node(5)
head.next.child.child = Node(6)

head.next.next = Node(7)
head.next.next.child = Node(8)

head.next.next.next = Node(9)
head.next.next.next.child = Node(12)

head.next.next.next.next = Node(20)


# Call the function to get the head of flattened sorted linked list
new_head = flatten_linked_list(head)

# Print the flattened linked list
print_linked_list(new_head)
