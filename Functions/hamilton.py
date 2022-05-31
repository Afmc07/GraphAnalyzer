from Classes.adjacencyMatrix import AdjacencyMatrix
from collections import Counter

def Dirac(model:AdjacencyMatrix):
    n = model.getverts()
    if n > 3:
        res = n/2
        degs = model.getdeg()

        for deg in degs:
            if res >= deg:
                return False
        return True        
    else:
        return False

def Ore(model:AdjacencyMatrix):
    vert_count = model.getverts()
    degs = model.getdeg()

    for i in  range(0, len(degs)-1):
        adjI = model.getLine(i)
        for j in range(i+1, vert_count):
            if adjI[j]!='1':
                cmp = degs[i] + degs[j]
                if vert_count > cmp:
                    return False
            else:
                continue        
    return True 

def Bondy(model:AdjacencyMatrix):
    n = model.getverts()

    while(True):
        preChav = model.getdeg()
        __andChav(model, n)
        if model.getdeg() == preChav:
            break

    Fdegs = model.getdeg()
    if Counter(Fdegs).get(n-1) == n:
        return True
    else:
        return False    

def __andChav(model, n):
    for i in range(0,n):
        degs = model.getdeg()
        lineI = model.getLine(i)
        for j in range(0,n):
            lineJ = model.getLine(j)
            if lineI[j]!='1' and j!=i:
                cmp = degs[i] + degs[j]
                if n > cmp:
                    continue
                else:
                    lineI[j] = '1'
                    lineJ[i] = '1'
                    model.setLine(i, lineI)
                    model.setLine(j, lineJ)
                    degs = model.getdeg()
            else:
                continue 