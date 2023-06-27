# Imports
from collections import *
from typing import *


# Function to prepare adjList -> Directed graph
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


# Helper function to perform topological sort
def helperTopologicalSort(
    node: int, visited: Set[int], stack: List[int], adjList: Dict[int, Set[int]]
):
    # Mark the node as visited
    visited.add(node)

    # If node in adjList
    if node in adjList:
        # Traverse over neighbors of node
        for neighbor in adjList[node]:
            # If neighbor not visited
            if neighbor not in visited:
                # Recursive call
                helperTopologicalSort(neighbor, visited, stack, adjList)

    # Push the node to stack
    stack.insert(0, node)


# Return topological sort
def topologicalSort(adj: List[Tuple[int, int]], v: int, e: int):
    # Dictionary to store adjList
    adjList = {}

    # Prepare adjList by calling the function
    prepareAdjList(adjList, adj)

    # Set to store visited nodes
    visited = set()

    # Initialize an empty stack
    stack = []

    # Traverse over all components
    for item in range(v):
        # If item not visited
        if item not in visited:
            # Call the topological sort function
            helperTopologicalSort(item, visited, stack, adjList)

    # Return the stack
    return stack


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
