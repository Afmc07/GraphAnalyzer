import copy
import sys
from Classes.adjacencyMatrix import AdjacencyMatrix

def FloydWarshall(weights:list, vert_count:int, labels:list):
    result_dists = copy.deepcopy(weights)
    for line in range(len(result_dists)):
        for idx in range(len(result_dists[line])):
            if result_dists[line][idx] == 0 and line != idx:
                result_dists[line][idx] = sys.maxsize

    for k in range(vert_count):
        for i in range(vert_count):
            for j in range(vert_count):
                result_dists[i][j] = min(result_dists[i][j], result_dists[i][k] + result_dists[k][j])
    print("-------------------------------\n")
    printSolution(result_dists, labels, vert_count)
    print("-------------------------------\n")            

def printSolution(result:list, labels:list, size:int):
    print("Labels\t", end=" ")
    print(*labels, sep="\t", end="\n")
    for i in range(size):
        print(labels[i], end="\t")
        for j in range(size):
            if result[i][j] == sys.maxsize:
                print ("INF\t")
            else:
                print (str(result[i][j]), end='\t')
            if j == size-1:
                print()     

