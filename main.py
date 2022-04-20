from Classes.model import model
from Functions.hamilton import Dirac, Ore, Bondy
from Functions.euler import euler
from Functions.search import BFS, DFS
from controller import Open, Affirm, Setup
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

def Idx_Start_pick(graph:model, test:str):
    while True:
            startIDX = int(input(f'Provide starting index for {test}: '))
            if startIDX > len(graph.edges) or startIDX < 1:
                print(f'Invalid index, max index = {len(graph.edges)} | min index = 1')
            else:
                return startIDX

def Dfs_process_Select():
    while True:
        process_select = input("Select your DFS process Recursive[R] Stack[S]: ")
        if process_select == 'R' or process_select == 'S':
            break
        else:
            print("Invalid input, please provide a valid choice.")  
    return process_select        


def test(graph:model, testFileName:str, type:str):
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
            BFS(graph, startIDX-1)
        case 'D':
            startIDX = Idx_Start_pick(graph,"DFS")
            process_select = Dfs_process_Select()
            print("\nDFS test Results "+str(testFileName))
            DFS(graph, startIDX-1, process_select)    

def TestHandler(fileType:str, name:int, testType:str):
    if fileType == 'csv':
         filename = f'./tests/{fileType}/{name}'
         graph = model([])
         Open.CSV(filename, graph)
         graph.setupWeightsCSV()
         graph.setVisitedArray()
         #clearConsole()
         test(graph, name, testType)
    else:
        filename = f'./tests/{fileType}/{name}'
        graph = model([])
        Open.TXT(filename, graph)
        graph.setVisitedArray()
        #clearConsole()
        test(graph, name, testType)

   
print(" ------------------------------------ ")
print("|                                    |")
print("| Welcome to Graph Datatype Tester!", end="  |\n")
print("|                                    |")
print(" ------------------------------------ \n")
while True:

    params = Setup()
    if params.fileName in params.fileList:
        TestHandler(params.fileType, params.fileName, params.testId)
    else:
        for x in range(0,len(params.fileList)):
            TestHandler(params.fileType, params.fileList[x], params.testId)

    resp = input("Do you wish to continue? Y/N\n")
    if resp == 'N':
        clearConsole()
        print('\nGoodbye!\n')
        break
    else:
        clearConsole()

             


            