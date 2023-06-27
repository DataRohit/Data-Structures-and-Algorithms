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


# Function to check for cycle using DFS
def isCyclicDFS(node, parent, visited, adjList):
    # Mark current node as visited
    visited.add(node)

    # If node in adjList
    if node in adjList:
        # Traverse and get all neighbors of the node
        for item in adjList[node]:
            # If item is not visited
            if item not in visited:
                # Call for neighbor
                cycleDetected = isCyclicDFS(item, node, visited, adjList)

                # If cycle detected
                if cycleDetected:
                    # Return true
                    return True

            # If item is visited
            elif item != parent:
                # Return false
                return True

    # Else no loop detected
    else:
        # Return false
        return False


# Function to detect cycle in undirected graph
def cycleDetection(edges: List[Tuple[int, int]], nNodes: int, nEdges: int) -> str:
    # Initialize a dictionary to represent adjacency list
    adjList = {}

    # Call the function to prepare the adjList
    prepareAdjList(adjList, edges)

    # Initialize a set to track visited nodes
    visited = set()

    # Traverse for every element to consider disconnected elements
    for node in range(nNodes):
        # If node is not visited
        if node not in visited:
            # Get the answer using the recursive function
            ans = isCyclicDFS(node, -1, visited, adjList)

            # If ans is True
            if ans:
                # Return yes
                return "Yes"

    # Else return No
    return "No"


# Number of nodes and edges
nNodes, nEdges = 4, 3


# Given edges
edges = [(1, 4), (4, 3), (3, 1)]


# Call the function and print the result
print(cycleDetection(edges, nNodes, nEdges))
