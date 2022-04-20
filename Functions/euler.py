from array import array
from Classes.model import model
import copy

def euler(model:model):
    dgs = model.getdeg()
    cnto = 0
    for x in dgs:
        if (x % 2) != 0:
            cnto+=1
            if cnto > 2:
                break    
    if cnto == 0:
        road = __prinroad(model, False)
        print("Euler Loop: "+str(road))
        print("Weighted: "+str(__roadWeight(model.getWeights(), road)))
        return 1
    elif cnto == 2:
        road = __prinroad(model, True)
        print("Euler Road: "+str(road))
        print("Weighted: "+str(__roadWeight(model.getWeights(), road)))
        return 2
    else:
        return 0                

def __prinroad(model:model, semi:bool):
    n = model.getverts()
    dgs = model.getdeg()
    edgs = model.getedg()
    if semi:
        for x in range(0, len(dgs)):
            if dgs[x]%2 == 1:
                line = model.getLine(x)
                pstln = x
                res = [x+1]
                break
    else:    
        line = model.getLine(0)
        pstln = 0
        res = [1]
    while '1' in line:
        for i in range(0, n):
            if line[i] == '1' and (dgs[pstln] == 1 or  __not_bridge(model, i, pstln)) or line[i] == '1' and len(res) == edgs:
                model.chngedg(i, pstln, '')
                line = model.getLine(i)
                pstln = i
                dgs = model.getdeg()
                break
        res.append(pstln+1)    
    return res

def __roadWeight(weights:array, road:array):
    res = 0
    while len(road)>1:
        res += weights[road[0]-1][road[1]-1]
        road.pop(0)
    return res    
                
def __not_bridge(model:model, idxV1:int, idxV2:int):
    modelCopy = copy.deepcopy(model)

    origStateCount = __dfs_access_count(modelCopy, idxV2)
    modelCopy.chngedg(idxV1, idxV2, '')
    modelCopy.resetVisits()
    changedStateCount = __dfs_access_count(modelCopy, idxV1)
    return origStateCount == changedStateCount     



def __dfs_access_count(model:model, startIdx:int):
    count = 1
    model.visited[startIdx] = True

    for itemIdx in range(0, len(model.edges[startIdx])):
        if model.edges[startIdx][itemIdx] == '1'  and not model.visited[itemIdx]:
            count += __dfs_access_count(model, itemIdx)
    return count            


