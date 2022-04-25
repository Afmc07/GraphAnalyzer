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
    connection_map = {}
    if process_select == 'R':
        __DFS_Recursive(graph, idx, connection_map)
        print("Showing Depth Tree") 
    elif process_select == 'S':
        __DFS_Stack(graph, idx, connection_map)
        print("Showing Depth Tree")  
    vs.MapVisualizer(connection_map)    

def __DFS_Recursive(graph:model, idx:int, connections:dict):
    graph.setVisited(idx)

    adj_idxs = [i for i, x in enumerate(graph.edges[idx]) if x == '1']
    connections[idx] = []

    for item in adj_idxs:
        if not graph.visited[item]:
            connections[idx].append(item)
            __DFS_Recursive(graph, item, connections)

def __DFS_Stack(graph:model, idx:int, connections:dict):
    stack = [idx]

    while stack:
        current_idx = stack.pop()
        if not graph.visited[current_idx]:
            connections[current_idx] = []
            graph.setVisited(current_idx)
            vert_idxs = [i for i, x in enumerate(graph.edges[current_idx]) if x == '1']
            vert_idxs.sort(reverse=True)
            for index in vert_idxs:
                stack.append(index)
                connections_mapUpdater(index, current_idx, connections, graph)


def connections_mapUpdater(adj_index:int, cur_index:int, connections:dict, graph:model):
    if not graph.visited[adj_index]:
        keys = connections.keys()
        for key in keys:
            if key == cur_index:
                continue
            elif adj_index in connections[key]:
                connections[key].remove(adj_index)
                break
        connections[cur_index].append(adj_index)    



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
    print("Tree:")
    graph.resetVisits()
    distDict = copy.deepcopy(dists)
    connection_map = {}
    connection_map[idx] = distDict[1]
    graph.setVisited(idx)
    keys = distDict.keys()

    for key in keys:
        for parent_index in distDict[key]:
            graph.setVisited(parent_index)
            connection_map[parent_index] = []
            vert_idxs = [i for i, x in enumerate(graph.edges[parent_index]) if x == '1']
            for adj_idx in vert_idxs:
                if key == 1:
                    if adj_idx != idx and adj_idx not in distDict[key] and not graph.visited[adj_idx]:
                        connection_map[parent_index].append(adj_idx)
                else:
                    if adj_idx not in distDict[key-1] and adj_idx not in distDict[key] and not graph.visited[adj_idx]:
                        connection_map[parent_index].append(adj_idx)       

    vs.MapVisualizer(connection_map)
    print("\n------------------------------\n")              

def PrintAdapter(array:list, format:str, end, sep):
    printable = [x+1 for x in array]
    print(format, end=end)
    print(*printable, sep=sep) 
    



    




    
            

    





