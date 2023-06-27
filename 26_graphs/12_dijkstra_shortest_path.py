# Imports
from os import *
from sys import *
from collections import *
from math import *
from typing import *


# Global INT_MAX and INT_MIN values
INT_MAX = 2147483647
INT_MIN = -2147483648


# Function to prepare adjList
def prepareAdjList(adjList: Dict[int, List[Tuple[int, int]]], edges: List[Tuple[int, int, int]]) -> None:
    # Loop over all edges
    for i in range(len(edges)):
        # Get the start, end and weight of the edge
        src, dest, weight = edges[i]

        # Add [dest, weight] to src
        adjList[src].append([dest, weight])

        # Add [src, weight] to source
        adjList[dest].append([src, weight])


# Function to return shortest path
def dijkstra(edges: List[Tuple[int, int, int]], nVertices: int, nEdges: int, source: int) -> List[int]:
    # Dict to store the graph
    # Key: [[Neighbor, Weight], ...]
    adjList = defaultdict(list)

    # Prepare the adjacency list
    prepareAdjList(adjList, edges)

    # Initialize a distance list with "inf"
    dist = [INT_MAX] * nVertices

    # Initialize a list representing
    st = []

    # Distance from source to source will be 0
    dist[source] = 0

    # Insert the source node to set
    st.append([0, source])

    # Traverse till st is not empty
    while st:
        # Get the top distance and top node
        nodeDist, topNode = st.pop(0)

        # If topNode in adjList
        if topNode in adjList:
            # Traverse neighbors
            for neighborNode, neighborDist in adjList[topNode]:
                # Compare distance
                if nodeDist + neighborDist < dist[neighborNode]:
                    # If entry exist in st
                    if [dist[neighborNode], neighborNode] in st:
                        # Remove
                        st.remove([dist[neighborNode], neighborNode])

                    # Update distance
                    dist[neighborNode] = nodeDist + neighborDist

                    # Push record to stack
                    st.append([dist[neighborNode], neighborNode])

    # Return distance array
    return dist


# Initialize number of vertices and edges
nVertices, nEdges = 5, 7


# Initialize edges
edges = [
    [0, 1, 7],
    [0, 2, 1],
    [0, 3, 2],
    [1, 2, 3],
    [1, 3, 5],
    [1, 4, 1],
    [3, 4, 7]
]


# Initialize source
source = 0


# Get the shortest path
path = dijkstra(edges, nVertices, nEdges, source)


# Print the shortest path
print(path)