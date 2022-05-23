import sys
from this import d
from Classes.adjacencyMatrix import AdjacencyMatrix
from Classes.adjacencyList import AdjecencyList

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def bellmanFord(matrix:AdjacencyMatrix, sourceIdx:int):
    adjList = AdjecencyList(matrix.getverts())
    adjList.matrixAdapter(matrix)

    vertex_amount = adjList.getVerts()
    distances = [sys.maxsize] * vertex_amount
    distances[sourceIdx] = 0

    neg_loop = False

    road_map = {} 

    for _ in range(vertex_amount-1):
        for start, dest, weight in adjList.graph:
            if distances[start] != sys.maxsize and distances[start] + weight < distances[dest]:
                distances[dest] = distances[start] + weight
                mapInsert(road_map, start, dest)

    for start, dest, weight in adjList.graph:
        if distances[start] != sys.maxsize and distances[start] + weight < distances[dest]:
            neg_loop = True
            break

    if not neg_loop:
        print(distances)
        print(road_map)
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
