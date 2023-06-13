# Import heapq
import heapq


# Class Node represents a node in the linked list
class Node:
    def __init__(self, data=-1, nex=None):
        self.data = data
        self.next = nex


# Function to merge K sorted linked lists using a min heap
def mergeKLists(listArray):
    # Store the number of arrays in listArray
    k = len(listArray)

    # Check if the listArray is empty or k is 0
    if listArray is None or k == 0:
        # Return a default node
        return Node(-1)

    # Create a min heap
    heap = []

    # Traverse over each linked list
    for i in range(k):
        # If data is not -1
        if listArray[i].data != -1:
            # Push the head node data and linked list index into heap
            heapq.heappush(heap, (listArray[i].data, i))

    # Initialize the head and tail node
    head = None
    tail = None

    # While heap has elements
    while heap:
        # Get the top node from the heap
        value, index = heapq.heappop(heap)

        # Get the head node at the index
        curNode = listArray[index]

        # Update the head node of linked list
        listArray[index] = listArray[index].next

        # Delete the next pointer of the current node
        curNode.next = None

        # If head node is not -> First node
        if head is None:
            # Update the head and tail
            head = curNode
            tail = curNode

        # Else
        else:
            # Add the current node after the tail node
            tail.next = curNode

            # Update the tail
            tail = tail.next

        # Push the next node from the same list onto the heap
        if listArray[index] is not None and listArray[index].data != -1:
            heapq.heappush(heap, (listArray[index].data, index))

    # Add a marker node at the end of the merged list
    if tail is not None:
        tail.next = Node(-1)

    # If head is still None, it means all lists were empty
    if head is None:
        return Node(-1)

    # Return the head node
    return head
