from asyncio.windows_events import NULL
from Classes.adjacencyMatrix import AdjacencyMatrix
from Functions.dijkstra import dijkstra
from Functions.hamilton import Dirac, Ore, Bondy
from Functions.euler import euler
from Functions.search import BFS, DFS
from Functions.bellmanFord import bellmanFord
from controller import Open, Affirm, Setup, RepeatSetup
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

def Idx_Start_pick(graph:AdjacencyMatrix, test:str):
    vert_count = graph.getverts()
    if len(graph.labels) > 0:
        while True:
            startIDX = input(f'Provide starting vertice for {test}: ')
            if startIDX not in graph.labels:
                print(f'\nInvalid index, Available vertices: {graph.labels}\n')
            else:
                return graph.labels.index(startIDX)
    else:     
        while True:
            startIDX = int(input(f'Provide starting index for {test}: '))
            if startIDX > vert_count or startIDX < 1:
                print(f'Invalid index, max index = {vert_count} | min index = 1')
            else:
                return startIDX-1

def Dfs_process_Select():
    while True:
        process_select = input("Select your DFS process [R]Recursive, [S]Stack: ")
        if process_select == 'R' or process_select == 'S':
            break
        else:
            print("Invalid input, please provide a valid choice.")  
    return process_select        


def test(graph:AdjacencyMatrix, testFileName:str, type:str):
    match type:
        case 'H':
            print("\n")        
            print("Hamilton Test Results File "+str(testFileName))        
            print("------------------------------")        
            print("Dirac: "+Affirm.Ham(Dirac(graph)))
            print("Ore: "+Affirm.Ham(Ore(graph)))
            print("Bondy & Chvatal: "+Affirm.Ham(Bondy(graph)))
            print("------------------------------\n")
        case 'E':
            print("\n")
            print("Euler Test Results File "+str(testFileName))        
            print("------------------------------")
            print("Result: "+Affirm.Eul(euler(graph))) 
            print("------------------------------\n") 
        case 'B':
            startIDX = Idx_Start_pick(graph, "BFS")
            print("\nBFS test Results "+str(testFileName))
            BFS(graph, startIDX)
        case 'D':
            startIDX = Idx_Start_pick(graph,"DFS")
            process_select = Dfs_process_Select()
            print("\nDFS test Results "+str(testFileName))
            DFS(graph, startIDX, process_select)
        case 'K':
            startIDX = Idx_Start_pick(graph,"Dijkstra")
            print("\nDijkstra test Results "+str(testFileName))
            dijkstra(graph, startIDX)
        case 'F':
            startIDX = Idx_Start_pick(graph,"Bellman Ford")
            print("\nBellman Ford test Results "+str(testFileName))
            bellmanFord(graph, startIDX)              

def TestHandler(fileType:str, name:int, testType:str):
    filename = f'./tests/{fileType}/{name}'
    graph = AdjacencyMatrix([])
    if fileType == 'csv':
         Open.CSV(filename, graph)
         graph.setupWeightsCSV()
         graph.setVisitedArray()
         test(graph, name, testType)
    else:  
        Open.TXT(filename, graph)
        graph.setVisitedArray()
        test(graph, name, testType)

   
print(" ------------------------------------ ")
print("|                                    |")
print("| Welcome to Graph Datatype Tester!", end="  |\n")
print("|                                    |")
print(" ------------------------------------ \n")

params = NULL
while True:
    if not params:
        params = Setup()
    if params.fileName in params.fileList:
        TestHandler(params.fileType, params.fileName, params.testId)
    else:
        for x in range(0,len(params.fileList)):
            TestHandler(params.fileType, params.fileList[x], params.testId)

    resp = input("Do you wish to continue? Y/N\n")
    if resp == 'N':
        clearConsole()
        print('\nGoodbye!')
        break
    else:
        clearConsole()
        params = RepeatSetup(params)
