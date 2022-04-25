import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualization:
   
    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

class visualizers:
    def DFSR(connections:dict):
        visual = GraphVisualization()
        keys = connections.keys()

        for key in keys:
            for item in connections[key]:
                visual.addEdge(key+1, item+1)

        visual.visualize()

    def DFSS(connections:dict):
        visual = GraphVisualization()
        keys = connections.keys()
        visited = []  

        while len(connections)>0:
            for key in keys:
                print(key)
