# Imports
from typing import List, Tuple
from sys import stdin, setrecursionlimit

setrecursionlimit(10**7)


# Edge class for storing the Edges of the graph
class Edge:
    def __init__(self, start: int, end: int, weight: int) -> None:
        self.start = start
        self.end = end
        self.weight = weight


# Function to build the set
def makeSet(parent: List[int], rank: List[int], V: int) -> None:
    # Initialize parent to itself
    # Initialize rank to 0
    for i in range(V):
        parent.append(i)
        rank.append(0)


# Function to find the parent node
def findParent(parent: List[int], node: int) -> int:
    # If node is the parent of itself
    if parent[node] == node:
        # Return the node
        return node

    # Recursive call to move up the graph to find the parent
    parent[node] = findParent(parent, parent[node])
    return parent[node]


# Function to get the union
def unionSet(u: int, v: int, parent: List[int], rank: List[int]) -> None:
    # Get the parent of both the nodes
    u = findParent(parent, u)
    v = findParent(parent, v)

    # If rank of u is less than rank of v
    if rank[u] < rank[v]:
        # Make v the parent of u
        parent[u] = v

    # If rank of u is greater than rank of v
    elif rank[u] > rank[v]:
        # Make u the parent of v
        parent[v] = u

    # If ranks are equal
    else:
        # Make u the parent of v
        parent[v] = u
        # Increment the rank of u
        rank[u] += 1


# Function to return the weight of MST
def minimumSpanningTree(edges: List[Tuple[int, int, int]], V: int, E: int) -> int:
    # Sort the edges based on their weights in ascending order
    edges.sort(key=lambda x: x.weight)

    # Initialize list to store parent and rank
    parent, rank = [], []

    # Call the function to build the set
    makeSet(parent, rank, V)

    # Variable to track minWeight
    minWeight = 0

    # Iterate over edges list
    for it in range(E):
        # Find parent
        u = findParent(parent, edges[it].start)
        v = findParent(parent, edges[it].end)

        # If not the same parent
        if u != v:
            # Update minWeight
            minWeight += edges[it].weight

            # Apply union
            unionSet(u, v, parent, rank)

    # Return minWeight
    return minWeight


# taking input using fast I/O
def takeInput():
    n_m = stdin.readline().strip().split(" ")
    V = int(n_m[0].strip())
    E = int(n_m[1].strip())

    edges = [Edge(0, 0, 0) for i in range(E)]
    for i in range(E):
        temp = list(map(int, stdin.readline().strip().split(" ")))
        edges[i] = Edge(temp[0], temp[1], temp[2])

    return edges, V, E


# main
edges, V, E = takeInput()
print(minimumSpanningTree(edges, V, E))


# Sample Input:
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8

# Sample Output:
# 9
