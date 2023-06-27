# Import typing for type hinting
from typing import *


# Function to prepare the adjList
def prepareAdjList(
    adjList: Dict[int, Set[int]], indegree: Dict[int, int], edges: List[Tuple[int, int]]
) -> None:
    # Extract start and end for every edge
    for u, v in edges:
        # If start already exist
        if u in adjList:
            # Add v to existing children list
            adjList[u].add(v)

        # If start no exist
        else:
            # Create a new set with v
            adjList[u] = {v}

        # If v already exist
        if v in indegree:
            # Increment its indegree
            indegree[v] += 1

        # Else initialize indegree
        else:
            indegree[v] = 1


# Function to detect cycle in directed graph
def detectCycleInDirectedGraph(n: int, edges: List[Tuple[int, int]]) -> bool:
    # Dictionary to store adjList and indegree
    adjList = {}
    indegree = {}

    # Call the function to prepare adjList
    prepareAdjList(adjList, indegree, edges)

    # Queue to track the elements
    queue = []

    # Initialize the count of elements included in BFS traversal
    count = 0

    # Traverse over all components
    for node in range(1, n + 1):
        # If indegree of node is 0
        if node not in indegree:
            # Add the node into queue
            queue.append(node)

    # Loop till queue becomes empty
    while queue:
        # Get the front element
        front = queue.pop(0)

        # Increment the count of valid elements to 1
        count += 1

        # If front has neighbors
        if front in adjList:
            # Traverse neighbors
            for neighbor in adjList[front]:
                # Decrement the indegree of neighbor
                indegree[neighbor] -= 1

                # If indegree of neighbor becomes 0 after update
                if indegree[neighbor] == 0:
                    # Push the neighbor onto queue
                    queue.append(neighbor)

                    # Pop the neighbor from the indegree dict
                    indegree.pop(neighbor)

    # Return the final answer
    return count != n


# Number of nodes and edges
nNodes, nEdges = 5, 6


# Given edges
edges = [(1, 2), (4, 1), (2, 4), (3, 4), (5, 2), (1, 3)]


# Call the function and print the result
print(detectCycleInDirectedGraph(nNodes, edges))
