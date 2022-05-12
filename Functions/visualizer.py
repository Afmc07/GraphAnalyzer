import pydot
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class GraphVisualization:
   
    def __init__(self):
        self.visual = []

    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self, type:str):
        ans = input("Is Graphviz working? Y/N ")
        G = nx.Graph() if ans == "N" else nx.DiGraph()
        G.add_edges_from(self.visual)

        if ans == 'Y':
            nx.draw_networkx(G, graphviz_layout(G, prog=type))
        else:    
            nx.draw_networkx(G)
        plt.show()

    def visualizeWeighted(self, type:str, labels:list, alph:bool):
        ans =  input("Is Graphviz working? Y/N: ")
        G = nx.Graph() if ans == "N" else nx.DiGraph()
        G.add_edges_from(self.visual)

        pos = nx.spring_layout(G)

        if ans == 'Y':
            nx.draw_networkx(G, graphviz_layout(G, prog=type))
        else:
            nx.draw_networkx(G, pos)
            if alph:
                edge_labels = dict([((n1, n2), f'{labels[alphabet.index(n1)][alphabet.index(n2)]}')
                    for n1, n2 in G.edges])
            else:
                edge_labels = dict([((n1, n2), f'{labels[n1-1][n2-1]}')
                    for n1, n2 in G.edges])
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()

class visualizers:
    def MapVisualizer(connections:dict, type:str):
        visual = GraphVisualization()
        keys = connections.keys()

        alph = True if input("are the vertex labels letters? Y/N: ") == 'Y' else False
        for key in keys:
            for item in connections[key]:
                if alph:
                    visual.addEdge(alphabet[key], alphabet[item])
                else:
                    visual.addEdge(key+1, item+1)

        visual.visualize(type)  

    def WeightedMapVisualizer(connections:dict, type:str, labels, alph):
        visual = GraphVisualization()
        keys = connections.keys()
        
        for key in keys:
            for item in connections[key]:
                if alph:
                    visual.addEdge(alphabet[key], alphabet[item])
                else:
                    visual.addEdge(key+1, item+1)

        visual.visualizeWeighted(type, labels, alph)  