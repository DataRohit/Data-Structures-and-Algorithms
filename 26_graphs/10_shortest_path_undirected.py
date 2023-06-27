# Import typing for type hinting
from typing import *


# Import deque to implement queue
from collections import deque


# Function to prepare adjList
def prepareAdjList(adjList: Dict[int, Set[int]], edges: List[Tuple[int, int]]) -> None:
    # Loop over all edges
    for i in range(len(edges)):
        # Get the start and end of the edge
        u = edges[i][0]
        v = edges[i][1]

        # If u in adjList
        if u in adjList:
            # Append v to end
            adjList[u].add(v)
        else:
            # Create a new entry for u
            adjList[u] = set([v])

        # If v in adjList
        if v in adjList:
            # Append u to end
            adjList[v].add(u)
        else:
            # Create a new entry for v
            adjList[v] = set([u])


# Function to get the shortest path
def shortestPath(edges: List[Tuple[int, int]], n: int, m: int, s: int, t: int):
    # Dict to store adjacency list
    adjList = {}

    # Call the function to prepare the adjList
    prepareAdjList(adjList, edges)

    # Set to store visited nodes
    visited = set()

    # Dict to store the parent
    parent = {}

    # Initialize a queue
    q = deque()

    # Push the start to queue
    q.append(s)

    # Set parent of start
    parent[s] = -1

    # Make the start as true
    visited.add(s)

    # Loop till queue is empty
    while q:
        # Get the front node
        front = q.popleft()

        # If front in adjList
        if front in adjList:
            # Traverse over the neighbors
            for neighbor in adjList[front]:
                # if neighbor not visited
                if neighbor not in visited:
                    # Mark the neighbor to visited
                    visited.add(neighbor)

                    # Mark parent
                    parent[neighbor] = front

                    # Push the neighbor to the queue
                    q.append(neighbor)

    # Prepare shortest path

    # List to store the answer
    ans = []

    # Start from end not in reverse order
    currNode = t

    # Push the last node to the ans list
    ans.append(t)

    # Traverse till we reach start
    while currNode != s:
        # Update current node
        currNode = parent[currNode]

        # Add the curr node to answer
        ans.append(currNode)

    # Return the answer
    return ans[::-1]


# Initialize the number of nodes and edges
n, m = 4, 4


# Initialize the edges
edges = [
    (1, 2),
    (2, 3),
    (3, 4),
    (1, 3)
]

# Call the function
print(shortestPath(edges, n, m, 1, 4))