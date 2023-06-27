# Import typing for type hinting
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


# Recursive function to check for cycle
def checkCycleDFS(
    node: int, visited: Set, dfsVisited: Set, adjList: Dict[int, Set[int]]
):
    # Mark node to visited
    visited.add(node)

    # Mark dfs visited of node to true
    dfsVisited.add(node)

    # If node in adjList
    if node in adjList:
        # Traverse over neighbors
        for item in adjList[node]:
            # If item not visited
            if item not in visited:
                # If cycle detected
                if checkCycleDFS(item, visited, dfsVisited, adjList):
                    # Return true
                    return True

            # If item visited
            # If item in dfsVisited
            elif item in dfsVisited:
                # Cycle detected
                return True

    # Undo dfs visited
    dfsVisited.remove(node)

    # Else no cycle detected
    return False


# Function to check if cycle exist in directed graph
def detectCycleInDirectedGraph(n: int, edges: List[Tuple[int, int]]):
    # Initialize a dictionary to represent adjacency list
    adjList = {}

    # Call the function to prepare the adjList
    prepareAdjList(adjList, edges)

    # Set to store visited nodes and dfs visited nodes
    visited = set()
    dfsVisited = set()

    # Traverse over all components
    for item in range(n):
        # If item not visited
        if item not in visited:
            # Function call for each item
            if checkCycleDFS(item, visited, dfsVisited, adjList):
                # Return true
                return True

    # Loop not found
    return False


# Number of nodes and edges
nNodes, nEdges = 5, 6


# Given edges
edges = [(1, 2), (4, 1), (2, 4), (3, 4), (5, 2), (1, 3)]


# Call the function and print the result
print(detectCycleInDirectedGraph(nNodes, edges))
