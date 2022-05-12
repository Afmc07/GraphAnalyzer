from array import array
from collections import Counter

class model():
    def __init__(self, edges):
        self.edges : array(array(str)) = edges
        self.weights = []
        self.visited = []

    def txtSetup(self, verts:int):
        for idx in range(0, verts):
            self.edges.append([])
            for i in range(0, verts):
                self.edges[idx].append('')

    def setupWeightsCSV(self):
        for row in self.edges:
            waux = []
            for item in row:
                if item != '':
                    aux = item.split('|')
                    x = self.edges.index(row)
                    y = self.edges[x].index(item)
                    self.edges[x][y] = aux[0]
                    waux.append(int(aux[1]))
                else:
                    waux.append(0)    
            self.weights.append(waux)

    def setupWeightsTXT(self):
        for row in self.edges:
            waux = [0] * len(self.edges)
            self.weights.append(waux)

    def setWeight(self, idx1:int, idx2:int, weight:int):
        self.weights[idx1][idx2] = weight
        self.weights[idx2][idx1] = weight

    def setDirWeight(self, idx1:int, idx2:int, weight:int):
        self.weights[idx1][idx2] = weight

    def getWeights(self):
        return self.weights
        
    def getverts(self):
        return len(self.edges)

    def getdeg(self):
        degList = []
        for line in self.edges:
            aux = Counter(line)
            degList.append(aux.get('1'))
        return degList

    def setLine(self, x:int, l:array):
        self.edges[x]= l    

    def getLine(self, x:int) -> array:
        return self.edges[x]

    def chngedg(self, line:int, edg:int, val:str):
        self.edges[line][edg] = val
        self.edges[edg][line] = val

    def chngDirEdg(self, line:int, edg:int, val:str):
        self.edges[line][edg] = val

    def getedg(self):
        cnt = 0;
        for i in range(0, self.getverts()):
            line = self.getLine(i)
            for j in range(i, len(line)):
                if line[j] == '1':
                    cnt += 1
        return cnt            

    def setVisitedArray(self):
        for i in range(0, len(self.edges)):
            self.visited.append(False)

    def setVisited(self, idx:int):
        self.visited[idx] = True    

    def resetVisits(self):
        for idx in range(0, len(self.visited)):
            self.visited[idx] = False    

    def getAdjacentVerts(self, parentIdx:int) -> list:
        return [i for i, x in enumerate(self.edges[parentIdx]) if x == '1']        
