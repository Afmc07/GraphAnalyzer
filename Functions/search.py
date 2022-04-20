from Classes.model import model
from .visualizer import visualizers as vs
import copy

def BFS(graph:model, idx:int):
    queue = []
    queue.append(idx)
    distance_count = 0
    distance_map = {}
    graph.setVisited(idx)

    while queue:
        current_vert = queue.pop(0)
        vert_idxs = [i for i, x in enumerate(graph.edges[current_vert]) if x == '1']

        for i in vert_idxs:
            if not graph.visited[i]:
                queue.append(i)
                graph.setVisited(i)

        if distance_count != len(queue) and distance_count == 0:
            distance_count += 1
            aux = copy.deepcopy(queue)
            distance_map[distance_count] = aux 

        elif distance_count > 0 and len(queue) > 0:
            presenceFlag = False
            for i in queue:
                if i in distance_map[distance_count]:
                    presenceFlag = True
                    break
            if not presenceFlag:
                distance_count += 1
                aux = copy.deepcopy(queue)
                distance_map[distance_count] = aux

    __distancePrinter(idx, distance_map)
    __roadPrinter(idx, graph, distance_map)
    __treePrinter(idx, distance_map, graph)

def DFS(graph:model, idx:int, process_select:str):
        if process_select == 'R':
            connection_map = {}
            __DFS_Recursive(graph, idx, connection_map)
            print("Showing Depth Tree")
            vs.DFSR(connection_map)
        elif process_select == 'S':
            __DFS_Stack(graph, idx)       

def __DFS_Recursive(graph:model, idx:int, connections:dict):
    graph.visited[idx] = True

    adj_idxs = [i for i, x in enumerate(graph.edges[idx]) if x == '1']
    connections[idx] = []

    for item in adj_idxs:
        if not graph.visited[item]:
            connections[idx].append(item)
            __DFS_Recursive(graph, item, connections)

def __DFS_Stack(graph, idx):
    print("Stack")            


def __distancePrinter(start:int, dists:dict):
    print("------------------------------\n")
    print("Distances:\n")

    print("start: "+str(start+1))
    distDict = copy.deepcopy(dists)
    keys = distDict.keys()

    for key in keys:
        PrintAdapter(distDict[key], f'Distance of {str(key)}:', ' ', ', ')
    print("\n------------------------------\n")    

def __roadPrinter(start:int, graph:model, dists:dict):
    print("------------------------------\n")
    print("Roads:\n")
    for dest in range(0, len(graph.edges)):
        distDict = copy.deepcopy(dists)
        if dest == start:
            continue
        else:
            if dest in distDict[1]:
                print(f'Road({start+1} to {dest+1}): {start+1} - {dest+1}')
            else:
                end = dest
                road = [end]
                distTrav = 2
                while True:
                    if end in distDict[distTrav]:
                        break
                    else:
                        distTrav += 1
                while distTrav > 1:
                    for vert in distDict[distTrav-1]:
                        if graph.edges[vert][end] == '1':
                            road.insert(0, vert)
                            end = vert
                            distTrav -= 1
                            break
                road.insert(0, start)
                PrintAdapter(road, f'Road({start+1} to {dest+1}):', ' ', ' - ')
    print("\n------------------------------\n")                  

def __treePrinter(idx:int, dists:dict, graph:model):
    print("------------------------------\n")
    print("Tree Adjacency:\n")
    graph.resetVisits()
    distDict = copy.deepcopy(dists)
    PrintAdapter(distDict[1], f'{idx+1}:', ' ', ', ')
    graph.setVisited(idx)
    
    last_dist = 1
    keys = distDict.keys()

    while last_dist in keys:
        for index in distDict[last_dist]:
            graph.setVisited(index)
            connections = [i for i, x in enumerate(graph.edges[index]) if x == '1']
            kids = []
            for item in connections:
                if not graph.visited[item] and item not in distDict[last_dist]:
                    kids.append(item)
            PrintAdapter(kids, f'{index+1}:', " ", ", ")        
        last_dist += 1
    print("\n------------------------------\n")              

def PrintAdapter(array:list, format:str, end, sep):
    printable = [x+1 for x in array]
    print(format, end=end)
    print(*printable, sep=sep) 
    



    




    
            

    





