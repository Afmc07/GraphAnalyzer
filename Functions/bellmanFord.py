import sys

from numpy import source
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

    for idx in range(vertex_amount):
        road_map[idx] = ''

    neg_loop = False
    for _ in range(vertex_amount-1):
        for start, dest, weight in adjList.graph:
            if distances[start] != sys.maxsize and distances[start] + weight < distances[dest]:
                distances[dest] = distances[start] + weight
                road_map[dest]= start

    for start, dest, weight in adjList.graph:
        if distances[start] != sys.maxsize and distances[start] + weight < distances[dest]:
            neg_loop = True
            break

    print("-------------------------------\n")
    if neg_loop:
        print("This graph contains a negative weight cycle\n")
    print_distances(sourceIdx, distances, adjList.labels, road_map)
    print("\n-------------------------------\n")       
                           
def print_distances(startIdx:int, distances:list, labels:list, path:dict):
    if len(labels) != 0:
        for idx in range(len(distances)):
            if distances[idx] != sys.maxsize:
                if idx != startIdx:
                    idxPath = generate_path(idx, path, labels)
                    if len(idxPath) == 1:
                        print(f'Distance from {labels[startIdx]} to {labels[idx]}: {idxPath[0]}')
                    else:
                        message = f'Distance from {labels[startIdx]} to {labels[idx]}: {distances[idx]}'   
                        PrintAdapterStr(idxPath, message, '| Path: ', '-')
                else:
                    message = f'Distance from {labels[startIdx]} to {labels[idx]}: Origin'
                    print(message)
            else:
                print(f'Distance from {labels[startIdx]} to {labels[idx]}: No Road Available')            

def generate_path(target:int, path:dict, labels:list):
    current = target
    full_path = []
    while current != '':
        full_path.insert(0, labels[current])
        current = path[current]
        if current != '' and path[current] in path.keys():
            if current == path[path[current]]:
                return ['negative loop']
    return full_path    

def PrintAdapterStr(array:list, format:str, end, sep):
    printable = [x for x in array]
    print(format, end=end)
    print(*printable, sep=sep)