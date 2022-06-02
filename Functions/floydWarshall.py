import copy
import sys


def FloydWarshall(weights: list, vert_count: int, labels: list):
    result_dists = copy.deepcopy(weights)
    nextArray = copy.deepcopy(weights)
    for line in range(len(result_dists)):
        for idx in range(len(result_dists[line])):
            if result_dists[line][idx] == 0 and line != idx:
                result_dists[line][idx] = sys.maxsize
                nextArray[line][idx] = -1
            elif line != idx:
                nextArray[line][idx] = idx

    for k in range(vert_count):
        for i in range(vert_count):
            for j in range(vert_count):
                cmp1 = result_dists[i][j]
                result_dists[i][j] = min(result_dists[i][j], result_dists[i][k] + result_dists[k][j])
                if cmp1 > result_dists[i][j]:
                    nextArray[i][j] = nextArray[i][k]
    print("-------------------------------\n")
    printSolution(result_dists, labels, vert_count)
    printPaths(nextArray, result_dists, labels)
    print("-------------------------------\n")


def printSolution(result: list, labels: list, size: int):
    print("Distance Matrix:\n")
    print("Labels\t", end=" ")
    print(*labels, sep="\t", end="\n")
    for i in range(size):
        print(labels[i], end="\t")
        for j in range(size):
            if result[i][j] == sys.maxsize:
                print("INF\t")
            else:
                print(str(result[i][j]), end='\t')
            if j == size - 1:
                print()


def printPaths(nxts: list, result: list, labels: list):
    print("\nPaths:\n")
    for vert in range(len(nxts)):
        for dest in range(len(nxts)):
            if vert == dest:
                continue
            else:
                path = constructPath(vert, dest, nxts)
                if len(path) == 1:
                    print(f'{labels[vert]} to {labels[dest]}: No Path Available')
                else:
                    print(f'{labels[vert]} to {labels[dest]}:', end=' ')
                    n = len(path) - 1
                    for i in range(n):
                        print(labels[path[i]], end=" - ")
                    print(f'{labels[path[n]]} | Cost: {result[vert][dest]}')
        print()


def constructPath(startIdx: int, endIdx: int, nxts: list):
    if nxts[startIdx][endIdx] == -1:
        return []
    path = [startIdx]
    current = startIdx
    while current != endIdx:
        current = nxts[current][endIdx]
        path.append(current)
    return path
