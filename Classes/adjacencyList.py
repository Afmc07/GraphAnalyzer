from model import model

class AdjecencyList:
    def __init__(self, vertexCount:int) -> None:
        self.vertices = vertexCount
        self.graph = []

    def addEdge(self, origin:int, destination:int, weight:int):
        self.graph.append([origin, destination, weight])

    def matrixAdapter(self, matrix:model):
        for vert in range(matrix.getverts()):
            print("WIP")    