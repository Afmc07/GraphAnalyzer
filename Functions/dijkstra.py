import sys
from Classes.adjacencyMatrix import AdjacencyMatrix
from utils.visualizer import visualizers as vs

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def dijkstra(graph:AdjacencyMatrix, sourceIdx:int):
    vertex_amount = graph.getverts()
    distances = [sys.maxsize] * vertex_amount
    distances[sourceIdx] = 0
    road_map = {}

    for _ in range(vertex_amount):
        x = __minDistance(distances, graph)

        if x == -1:
            continue

        graph.setVisited(x)
        road_map[x] = []

        for yIdx in range(vertex_amount):
            if int(graph.weights[x][yIdx]) > 0 and not graph.visited[yIdx] and distances[yIdx] > distances[x]+graph.weights[x][yIdx]:
                distances[yIdx] = distances[x]+graph.weights[x][yIdx]
                mapInsert(road_map, x, yIdx)
                
    __printResult(distances, sourceIdx, graph.labels)
    vs.WeightedMapVisualizer(road_map, "dot", graph.weights, graph.labels)            

def __minDistance(dist:list, graph:AdjacencyMatrix):
    min = sys.maxsize
    min_index = -1

    for idx in range(graph.getverts()):
        if dist[idx] < min and not graph.visited[idx]:
            min = dist[idx]
            min_index = idx
    return min_index

def mapInsert(road:dict, parentIdx:int, addedIdx:int):
    keys = road.keys()
    for key in keys:
        if key == parentIdx:
            continue
        elif addedIdx in road[key]:
            road[key].remove(addedIdx)
            break
    road[parentIdx].append(addedIdx)

def __printResult(distance_list:list, startIdx:int, labels:list):
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
            if len(labels) > 0:
                print(f'From {labels[startIdx]} to {labels[index]}: {distance_list[index]}')
            else:
                print(f'From {startIdx+1} to {index+1}: {distance_list[index]}')  
    print("\n---------------------------------\n")        