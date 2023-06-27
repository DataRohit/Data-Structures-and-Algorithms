class DisjointSet:
    def __init__(self, n):
        # Parent list for each element (adjusted index range to include 1 to N)
        self.parent = [i for i in range(n + 1)]

        # Rank list for each element (adjusted index range to include 1 to N)
        self.rank = [0] * (n + 1)

    def find(self, x):
        # If x is not the parent of itself
        if self.parent[x] != x:
            # Path compression: Update x's parent to the root
            self.parent[x] = self.find(self.parent[x])

        # Return the parent/root of x
        return self.parent[x]

    def union(self, x, y):
        # Find the root of set containing x
        rootX = self.find(x)

        # Find the root of set containing y
        rootY = self.find(y)

        # If rank of rootX is less than rank of rootY
        if self.rank[rootX] < self.rank[rootY]:
            # Make rootY the parent of rootX
            self.parent[rootX] = rootY

        # If rank of rootX is greater than rank of rootY
        elif self.rank[rootX] > self.rank[rootY]:
            # Make rootX the parent of rootY
            self.parent[rootY] = rootX

        # Make rootX the parent of rootY
        else:
            self.parent[rootY] = rootX
            # Increment the rank of rootX
            self.rank[rootX] += 1


def calculatePrimsMST(n, e, edges):
    # If number of vertices is non-positive, return an empty list
    if n <= 0:
        return []

    # Sort the edges based on their weights in ascending order
    edges.sort(key=lambda x: x[2])

    # Create a disjoint set object
    disjoint_set = DisjointSet(n)

    # Minimum Spanning Tree (MST)
    mst = []

    for edge in edges:
        u, v, weight = edge

        # If including this edge does not form a cycle
        if disjoint_set.find(u) != disjoint_set.find(v):
            # Add the edge to the MST
            mst.append([u, v, weight])

            # Perform union operation to merge the sets
            disjoint_set.union(u, v)

    # Return the Minimum Spanning Tree
    return mst


# Initialize number of vertices and edges
N, E = 5, 14

# List of edges in the form (u, v, weight)
edges = [
    [1, 2, 2],
    [1, 4, 6],
    [2, 1, 2],
    [2, 3, 3],
    [2, 4, 8],
    [2, 5, 5],
    [3, 2, 3],
    [3, 5, 7],
    [4, 1, 6],
    [4, 2, 8],
    [4, 5, 9],
    [5, 2, 5],
    [5, 3, 7],
    [5, 4, 9],
]

# Function call to calculate the MST
mst = calculatePrimsMST(N, E, edges)

# Print the edges of the MST
print("Edges of the Minimum Spanning Tree:")
for edge in mst:
    print(edge)
