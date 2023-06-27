# Import typing for type hinting
from typing import *


# Import collections for defaultdict
from collections import *


# Class to represent a graph
class Graph(object):
    # Constructor
    def __init__(self) -> None:
        # Dict to store the graph
        # Key: [[Neighbor, Weight], ...]
        self.adjList = defaultdict(list)

    # Method to add an edge to the graph
    def addEdge(self, src: int, dest: int, weight: int) -> None:
        # Create a list to store the neighbor and weight
        neighbor = [dest, weight]

        # Add the neighbor to the source
        self.adjList[src].append(neighbor)

    # Method to print the adjacency list
    def printGraph(self) -> None:
        # For each vertex in the graph
        for vertex in self.adjList:
            # Print the vertex
            print(vertex, end=" -> ")

            # For each neighbor in the vertex
            for neighbor, weight in self.adjList[vertex]:
                # Print the neighbor
                print(f"({neighbor}, {weight})", end=", ")

            # Print new line
            print()


    # Helper function to perform topological sort
    def __helperTopologicalSort(
        self, node: int, visited: Set[int], stack: List[int], adjList: Dict[int, List[Tuple[int, int]]]
    ) -> None:
        # Mark the node as visited
        visited.add(node)

        # If node in adjList
        if node in adjList:
            # Traverse over neighbors of node
            for neighbor, weight in adjList[node]:
                # If neighbor not visited
                if neighbor not in visited:
                    # Recursive call
                    self.__helperTopologicalSort(neighbor, visited, stack, adjList)

        # Push the node to stack
        stack.insert(0, node)


    # Return topological sort
    def topologicalSort(self, v: int, e: int) -> List[int]:
        # Set to store visited nodes
        visited = set()

        # Initialize an empty stack
        stack = []

        # Traverse over all components
        for item in range(v):
            # If item not visited
            if item not in visited:
                # Call the topological sort function
                self.__helperTopologicalSort(item, visited, stack, self.adjList)

        # Return the stack
        return stack
    

    # Method to find the shortest path
    def shortestPath(self, source: int, distance: List[int], stack: List[int]) -> None:
        # Set distance of source to 0
        distance[source] = 0

        # Traverse over the stack
        while stack:
            # Get the top element
            top = stack.pop(0)

            # If top in adjList
            if top in self.adjList:
                # If distance is not infinity
                if distance[top] != float("inf"):
                    # Traverse over neighbors of top
                    for neighbor, weight in self.adjList[top]:
                        # If current distance less than old distance
                        # Note: By default, distance[neighbor] is infinity
                        if distance[top] + weight < distance[neighbor]:
                            # Update the distance
                            distance[neighbor] = distance[top] + weight


# Create a graph
graph = Graph()


# Add edges to the graph
graph.addEdge(0, 1, 5)
graph.addEdge(0, 2, 3)
graph.addEdge(1, 2, 2)
graph.addEdge(1, 3, 6)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 4, 4)
graph.addEdge(2, 5, 2)
graph.addEdge(3, 4, -1)
graph.addEdge(4, 5, -2)


# Print the graph
graph.printGraph()


# Initialize number of nodes and edges
nNodes, nEdges = 6, 9


# Call the topological sort function
stack = graph.topologicalSort(nNodes, nEdges)


# Initialize source
source = 1


# Initialize distance array
distance = [float("inf")] * nNodes


# Set distance of source to 0
distance[source] = 0


# Call the shortest path function
graph.shortestPath(source, distance, stack)


# Print the distance array
print(distance)