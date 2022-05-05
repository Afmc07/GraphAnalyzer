import sys
from Classes.model import model

def dijkstra(graph:model, sourceIdx:int):
    vertex_amount = graph.getverts()
    distances = [sys.maxsize] * vertex_amount
    distances[sourceIdx] = 0

    for cout in range(vertex_amount):
        x = __minDistance(distances, graph)

        if x == -1:
            continue

        graph.setVisited(x)

        for yIdx in range(vertex_amount):
            if int(graph.weights[x][yIdx]) > 0 and not graph.visited[yIdx] and distances[yIdx] > distances[x]+graph.weights[x][yIdx]:
                distances[yIdx] = distances[x]+graph.weights[x][yIdx]
    __printResult(distances, sourceIdx)            

def __minDistance(dist:list, graph:model):
    min = sys.maxsize
    min_index = -1

    for idx in range(graph.getverts()):
        if dist[idx] < min and not graph.visited[idx]:
            min = dist[idx]
            min_index = idx
    return min_index

def __printResult(distance_list:list, startIdx:int):
    no_road = sys.maxsize
    no_road_vec = [i for i, x in enumerate(distance_list) if x == no_road]

    for idx in no_road_vec:
        distance_list[idx] = "No Road Available"

    print("\nMinimum Road Weights:")
    print("---------------------------------\n")
    for index in range(len(distance_list)):
        if index == startIdx:
            continue
        else:
            print(f'From {startIdx+1} to {index+1}: {distance_list[index]}')
    print("\n---------------------------------\n")        