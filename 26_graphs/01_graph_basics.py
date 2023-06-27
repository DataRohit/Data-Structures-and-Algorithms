# Class to create a graph
class Graph(object):
    # Constructor - takes a dictionary
    def __init__(self, graphDict=None):
        # If no dictionary is provided, an empty dictionary is used
        if graphDict == None:
            graphDict = {}

        # Assign the dictionary to the graph
        self.__graphDict = graphDict

    # Method to add edges to the graph
    def addEdge(self, u, v, directed=False):
        # Check if the data type of the input is correct
        try:
            u, v = eval(u), eval(v)

        # If not, convert the data type to string
        except:
            pass

        # If the vertex is in the graph, add the edge to the vertex else add the vertex to the graph
        if u in self.__graphDict:
            self.__graphDict[u].append(v)
        else:
            self.__graphDict[u] = [v]

        # If the graph is undirected, the edge is added in the other direction
        if directed == False:
            if v in self.__graphDict:
                self.__graphDict[v].append(u)
            else:
                self.__graphDict[v] = [u]

    # Method to print the graph
    def printGraph(self):
        # Loop through the graph dictionary
        for vertex in self.__graphDict:
            # Print the vertex and its edges
            print(vertex, ":", self.__graphDict[vertex])


# Take user input for number of nodes
n = int(input("Enter the number of nodes: "))

# Take user input for the edges
e = int(input("Enter the number of edges: "))

# Take user input if the graph is directed or not (default is undirected)
# 0 -> undirected
# 1 -> directed
d = bool(int(input("\nGraph is directed or not: ")))

# Create the graph
graph = Graph()

# Add line break
print()

# Loop for number of edges
for i in range(e):
    # Take user input for the edge
    u, v = map(str, input("Enter the edge: ").split())

    # Add the edge to the graph
    graph.addEdge(u, v, d)

# Add line break
print()

# Print the graph
graph.printGraph()
