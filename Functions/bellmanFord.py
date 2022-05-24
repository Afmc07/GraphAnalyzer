import sys
from Classes.adjacencyMatrix import AdjacencyMatrix
from Classes.adjacencyList import AdjecencyList
from .visualizer import visualizers as vs

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def bellmanFord(matrix:AdjacencyMatrix, sourceIdx:int):
    adjList = AdjecencyList(matrix.getverts())
    adjList.matrixAdapter(matrix)

    vertex_amount = adjList.getVerts()
    distances = [sys.maxsize] * vertex_amount
    distances[sourceIdx] = 0

    road_map = {}

    neg_loop = False

    for _ in range(vertex_amount-1):
        for start, dest, weight in adjList.graph:
            if start not in road_map.keys():
                road_map[start]= []

            if distances[start] != sys.maxsize and distances[start] + weight < distances[dest]:
                distances[dest] = distances[start] + weight
                mapInsert(road_map, start, dest)

    for start, dest, weight in adjList.graph:
        if distances[start] != sys.maxsize and distances[start] + weight < distances[dest]:
            neg_loop = True
            break

    if not neg_loop:
        print_result(sourceIdx, distances, adjList.labels)
        vs.WeightedMapVisualizer(road_map, "dot", matrix.weights, matrix.labels)
    else:
        print("This graph contains a negative weight cycle")

def mapInsert(road:dict, parentIdx:int, addedIdx:int):
    keys = road.keys()
    for key in keys:
        if key == parentIdx:
            continue
        elif addedIdx in road[key]:
            road[key].remove(addedIdx)
            break
    road[parentIdx].append(addedIdx)          
                           
def print_result(startIdx:int, distances:list, labels:list):
    print("-------------------------------\n")
    if len(labels) != 0:
        for idx in range(len(distances)):
            print(f'Distance from {labels[startIdx]} to {labels[idx]}: {distances[idx]}')
    else:
        for idx in len(distances):
            print(f'Distance from {startIdx} to {idx}: {distances[idx]}')
    print("\n-------------------------------\n")        