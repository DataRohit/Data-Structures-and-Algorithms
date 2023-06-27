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


# Function to check for cycle using BFS
def isCyclicBFS(src, visited, adjList):
    # Dictionary to store parent and child
    parentChild = {}

    # Add src node to dict
    parentChild[src] = -1

    # Mark the src node visited
    visited.add(src)

    # Initialize queue to track nodes to check
    queue = deque()

    # Push src node to queue
    queue.append(src)

    # Traverse till queue is empty
    while queue:
        # Pop and store the front node
        front = queue.popleft()

        # If front in adjList
        if front in adjList:
            # Traverse over the neighbors of the front node
            for neighbor in adjList[front]:
                # Cycle condition
                if (neighbor in visited) and (neighbor != parentChild[front]):
                    # Cycle is parent
                    return True

                # Cycle absent -> Node not visited
                elif neighbor not in visited:
                    # Push neighbor to the queue
                    queue.append(neighbor)

                    # Mark the neighbor as visited
                    visited.add(neighbor)

                    # Store the parent and child
                    parentChild[neighbor] = front

    # Else return false
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
            ans = isCyclicBFS(node, visited, adjList)

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
