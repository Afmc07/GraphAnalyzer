from .adjacencyMatrix import AdjacencyMatrix

class AdjecencyList:
    def __init__(self, vertexCount:int) -> None:
        self.vertices = vertexCount
        self.graph = []
        self.labels = []

    def addEdge(self, origin:int, destination:int, weight:int):
        self.graph.append([origin, destination, weight])

    def getVerts(self):
        return self.vertices    

    def matrixAdapter(self, matrix:AdjacencyMatrix):
        self.labels = matrix.labels
        for vert in range(matrix.getverts()):
            adjList = matrix.getAdjacentVerts(vert);
            for idx in adjList:
                self.addEdge(vert, idx, matrix.weights[vert][idx])