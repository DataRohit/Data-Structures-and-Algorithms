# Imports
from typing import *


# Function to prepare adjList -> Directed graph
def prepareAdjList(
    adjList: Dict[int, Set[int]],
    indegree: Dict[int, Set[int]],
    edges: List[Tuple[int, int]],
) -> None:
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

        # If v in indegree dict
        if v in indegree:
            # Increment the indegree by 1
            indegree[v] += 1

        # If v not in indegree dict
        else:
            # Create a new entry of v with indegree 1
            indegree[v] = 1


# Return topological sort
def topologicalSort(adj: List[Tuple[int, int]], v: int, e: int):
    # Dictionary to store adjList
    adjList = {}

    # Dictionary to store indegree
    indegree = {}

    # Prepare adjList by calling the function
    prepareAdjList(adjList, indegree, adj)

    # Initialize a queue to track element
    queue = []

    # Traverse over all elements
    for item in range(v):
        # If item not in indegree
        if item not in indegree:
            # Push item to queue
            queue.append(item)

    # List to store answer
    ans = []

    # Traverse till queue is empty
    while queue:
        # Get the front element
        front = queue.pop(0)

        # Store the answer
        ans.append(front)

        # If front in adjList
        if front in adjList:
            # Traverse over neighbor
            for neighbor in adjList[front]:
                # If neighbor in indegree
                if neighbor in indegree:
                    # Decrement the indegree
                    indegree[neighbor] -= 1

                    # If indegree after decrement is 0
                    if indegree[neighbor] == 0:
                        # Push neighbor to queue
                        queue.append(neighbor)

                        # Remove neighbor from the indegree list
                        indegree.pop(neighbor)

    # Return the answer
    return ans


# Initialize number of vertices and edges
v = 4
e = 4


# Initialize edges
edges = [
    (0, 1),
    (0, 3),
    (1, 2),
    (3, 2),
]


# Function call
print(topologicalSort(edges, v, e))
