# Imports
from collections import deque


# Function to prepare adjList
def prepareAdjList(adjList, edges):
    # Loop over all edges
    for i in range(len(edges[0])):
        # Get the start and end of the edge
        u = edges[0][i]
        v = edges[1][i]

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


# Function to get the BFS traversal
def bfsTraversal(adjList, visited, ans, node):
    # Queue to store node
    queue = deque()

    # Push node to queue
    queue.append(node)

    # Mark the node as visited
    visited.add(node)

    # Loop till queue becomes empty
    while queue:
        # Get the front node
        front = queue.popleft()

        # Store front node into answer
        ans.append(front)

        # If front node has children
        if front in adjList:
            # Traverse all neighbors of front node
            for item in sorted(adjList[front]):
                # If item node is not visited
                if item not in visited:
                    # Push to queue
                    queue.append(item)

                    # Mark visited to true
                    visited.add(item)


# Function to return the BFS traversal
def BFS(vertex, edges):
    # 'vertex' is the number of vertices present in the graph
    # 'edges' is a matrix of the set of edges between two given vertices in the graph

    # Initialize a dictionary to represent adjacency list
    adjList = {}

    # List to store the BFS traversal
    ans = []

    # Initialize a set to track visited nodes
    visited = set()

    # Call the function to prepare the adjList
    prepareAdjList(adjList, edges)

    # Traverse all components of the graph
    for i in range(vertex):
        # If node not visited
        if i not in visited:
            # Call the function to populate the ans list with BST traversal
            bfsTraversal(adjList, visited, ans, i)

    # Return the answer list
    return ans


# Initialize number of vertices
vertex = 5


# Initialize edges
edges = [[0, 0, 1, 2, 2, 3, 3, 4], [1, 4, 2, 0, 4, 0, 2, 3]]


# Function call to get the BFS traversal
print(BFS(vertex, edges))
