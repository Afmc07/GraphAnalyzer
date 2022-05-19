import sys
from Classes.model import model

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def bellmanFord(graph:model, sourceIdx:int):
    vertex_amount = graph.getverts()
    distances = [sys.maxsize] * vertex_amount
    distances[sourceIdx] = 0

    road_map = {} 

    for _ in range(vertex_amount-1):

        for vert in range(vertex_amount):
            adjVerts = graph.getAdjacentVerts(vert)
            road_map[vert] = []
            for adj in adjVerts:
                if distances[vert] != sys.maxsize and distances[vert] + graph.weights[vert][adj] < distances[adj]:
                    distances[adj] = distances[vert] + graph.weights[vert][adj]
                    mapInsert(road_map, vert, adj)
    for adj in adjVerts:
                if distances[vert] != sys.maxsize and distances[vert] + graph.weights[vert][adj] < distances[adj]:
                    print("Negative Cycle?")

    print(distances)
    print(road_map)
    
                    

def mapInsert(road:dict, parentIdx:int, addedIdx:int):
    keys = road.keys()
    for key in keys:
        if key == parentIdx:
            continue
        elif addedIdx in road[key]:
            road[key].remove(addedIdx)
            break
    road[parentIdx].append(addedIdx)            
