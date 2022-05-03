import pydot
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

class GraphVisualization:
   
    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self, type:str):
        #G = nx.DiGraph()
        ans = input("Is Graphviz working? Y/N ")
        G = nx.Graph() if ans == "N" else nx.DiGraph()
        G.add_edges_from(self.visual)

        if ans == 'Y':
            nx.draw_networkx(G, graphviz_layout(G, prog=type))
        else:    
            nx.draw_networkx(G)
        plt.show()

class visualizers:
    def MapVisualizer(connections:dict, type:str):
        visual = GraphVisualization()
        keys = connections.keys()

        for key in keys:
            for item in connections[key]:
                visual.addEdge(key+1, item+1)

        visual.visualize(type)