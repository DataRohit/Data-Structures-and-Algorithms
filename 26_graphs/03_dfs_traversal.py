# Import typing for type hinting
from typing import List, Dict, Set


# Function to prepare adjList
def prepareAdjList(adjList: Dict[int, Set[int]], edges: List[List[int]]):
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


# Recursive dfs function to add elements to component list
def dfs(
    node: int, visited: Set[int], adjList: Dict[int, Set[int]], component: List[int]
):
    # Add the node to component
    component.append(node)

    # Mark node as visited
    visited.add(node)

    # If node in adjList
    if node in adjList:
        # Traverse for every node value
        for item in adjList[node]:
            # If item not visited
            if item not in visited:
                # Recursive call for the item
                dfs(item, visited, adjList, component)


# Function to return the DFS traversal
def depthFirstSearch(V: int, E: int, edges: List[List[int]]) -> List[List[int]]:
    # Prepare an adjList
    adjList = {}

    # List to store answer
    ans = []

    # Initialize a set to track visited nodes
    visited = set()

    # Prepare the adjList
    prepareAdjList(adjList, edges)

    # Traverse all components of the graph
    for i in range(V):
        # If node not visited
        if i not in visited:
            # Initialize a list to store the answer for the component
            component = []

            # Function call to populate the component
            dfs(i, visited, adjList, component)

            # Push the component to the answer
            ans.append(sorted(component))

    # Return the ans list
    return ans


# Initialize vertex and edges
V, E = 9, 7


# Initialize edges
edges = [[0, 1], [0, 2], [0, 5], [3, 6], [7, 4], [4, 8], [7, 8]]


# Function call to return the DFS traversal
for l in depthFirstSearch(V, E, edges):
    print(*l)
