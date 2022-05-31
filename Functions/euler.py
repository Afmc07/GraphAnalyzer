from array import array
from Classes.adjacencyMatrix import AdjacencyMatrix
import copy

def euler(AdjacencyMatrix:AdjacencyMatrix):
    dgs = AdjacencyMatrix.getdeg()
    cnto = 0
    for x in dgs:
        if (x % 2) != 0:
            cnto+=1
            if cnto > 2:
                break    
    if cnto == 0:
        road = __prinroad(AdjacencyMatrix, False)
        print("Euler Loop: "+str(road))
        print("Weighted: "+str(__roadWeight(AdjacencyMatrix.getWeights(), road)))
        return 1
    elif cnto == 2:
        road = __prinroad(AdjacencyMatrix, True)
        print("Euler Road: "+str(road))
        print("Weighted: "+str(__roadWeight(AdjacencyMatrix.getWeights(), road)))
        return 2
    else:
        return 0                

def __prinroad(AdjacencyMatrix:AdjacencyMatrix, semi:bool):
    n = AdjacencyMatrix.getverts()
    dgs = AdjacencyMatrix.getdeg()
    edgs = AdjacencyMatrix.getedg()
    if semi:
        for x in range(0, len(dgs)):
            if dgs[x]%2 == 1:
                line = AdjacencyMatrix.getLine(x)
                pstln = x
                res = [x+1]
                break
    else:    
        line = AdjacencyMatrix.getLine(0)
        pstln = 0
        res = [1]
    while '1' in line:
        for i in range(0, n):
            if line[i] == '1' and (dgs[pstln] == 1 or  __not_bridge(AdjacencyMatrix, i, pstln)) or line[i] == '1' and len(res) == edgs:
                AdjacencyMatrix.chngedg(i, pstln, '')
                line = AdjacencyMatrix.getLine(i)
                pstln = i
                dgs = AdjacencyMatrix.getdeg()
                break
        res.append(pstln+1)    
    return res

def __roadWeight(weights:array, road:array):
    res = 0
    while len(road)>1:
        res += weights[road[0]-1][road[1]-1]
        road.pop(0)
    return res    
                
def __not_bridge(AdjacencyMatrix:AdjacencyMatrix, idxV1:int, idxV2:int):
    AdjacencyMatrixCopy = copy.deepcopy(AdjacencyMatrix)

    origStateCount = __dfs_access_count(AdjacencyMatrixCopy, idxV2)
    AdjacencyMatrixCopy.chngedg(idxV1, idxV2, '')
    AdjacencyMatrixCopy.resetVisits()
    changedStateCount = __dfs_access_count(AdjacencyMatrixCopy, idxV1)
    return origStateCount == changedStateCount     



def __dfs_access_count(AdjacencyMatrix:AdjacencyMatrix, startIdx:int):
    count = 1
    AdjacencyMatrix.visited[startIdx] = True

    for itemIdx in range(0, AdjacencyMatrix.getverts()):
        if AdjacencyMatrix.edges[startIdx][itemIdx] == '1'  and not AdjacencyMatrix.visited[itemIdx]:
            count += __dfs_access_count(AdjacencyMatrix, itemIdx)
    return count            


