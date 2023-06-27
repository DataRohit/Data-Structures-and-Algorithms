# Import
from typing import *


def prepareAdjList(adjList: Dict[int, Set[int]], edges: List[Tuple[int, int]]) -> None:
    # This function prepares the adjacency list representation of the graph.
    # The adjacency list is a data structure that stores the list of neighbors for each vertex in the graph.
    # The function takes the list of edges as input and updates the adjacency list accordingly.

    for u, v in edges:
        adjList.setdefault(u, set()).add(v)
        adjList.setdefault(v, set()).add(u)


def dfs(
    node: int,
    parent: int,
    timer: int,
    disc: List[int],
    low: List[int],
    result: List[List[int]],
    adjList: Dict[int, Set[int]],
    visited: Set[int],
) -> None:
    # This function performs a depth-first search on the graph.
    # The function takes the current node, its parent node, the current time, the discovery time array,
    # the low value array, the list of bridges, the adjacency list, and the visited set as input.
    # The function updates the discovery time and low value arrays,
    # and checks if the current edge is a bridge.

    visited.add(node)
    disc[node] = low[node] = timer
    timer += 1

    if node in adjList:
        for nbr in adjList[node]:
            if nbr == parent:
                continue

            # If the neighbor is not visited, then we recursively call the DFS function on the neighbor.
            if nbr not in visited:
                dfs(nbr, node, timer, disc, low, result, adjList, visited)

                # We update the low value of the current node to the minimum of the low values of the neighbor and the current node.
                low[node] = min(low[node], low[nbr])

                # If the low value of the neighbor is greater than the discovery time of the current node, then the current edge is a bridge.
                if low[nbr] > disc[node]:
                    result.append([node, nbr])

            # Otherwise, we simply update the low value of the current node to the discovery time of the neighbor.
            else:
                low[node] = min(low[node], disc[nbr])


def findBridges(edges: List[Tuple[int, int]], v: int, e: int) -> List[List[int]]:
    # This function finds the bridges in the graph.
    # The function takes the list of edges, the number of vertices, and the number of edges as input.
    # The function returns the list of bridges.

    adjList = {}
    prepareAdjList(adjList, edges)

    timer = 0
    disc = [-1] * v
    low = [-1] * v
    visited = set()
    result = []

    # We iterate over all the vertices in the graph and call the DFS function on each vertex.
    for i in range(v):
        if i not in visited:
            dfs(i, -1, timer, disc, low, result, adjList, visited)

    return result


# Initialize number of vertices and edges
v, e = 6, 7


# Initialize edges
edges = [[1, 2], [1, 0], [0, 2], [0, 4], [5, 4], [5, 3], [3, 4]]


# Function call
print(findBridges(edges, v, e))
