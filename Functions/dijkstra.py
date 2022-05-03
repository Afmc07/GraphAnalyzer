from multiprocessing.dummy import Array
import sys
from Classes.model import model

def dijkstra(graph:model, sourceIdx:int):
    vertex_amount = graph.getverts()
    dist = [sys.maxsize] * vertex_amount
    dist[sourceIdx] = 0

    for cout in range(vertex_amount):
        x = __minDistance(dist, graph)

        graph.setVisited(x)

        for yIdx in range(vertex_amount):
            if int(graph.weights[x][yIdx]) > 0 and not graph.visited[yIdx] and dist[yIdx] > dist[x]+graph.weights[x][yIdx]:
                dist[yIdx] = dist[x]+graph.weights[x][yIdx]
    print(dist)            



def __minDistance(dist:list, graph:model):
    min = sys.maxsize

    for idx in range(graph.getverts()):
        if dist[idx] < min and not graph.visited[idx]:
            min = dist[idx]
            min_index = idx

    return min_index        