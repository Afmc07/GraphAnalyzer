from Classes.model import model
from Classes.params import params
import csv
import os

def Setup():
    file_type = input("Please select a file input type: [csv]CSV [txt]TXT: ")

    choice_dir_path = os.path.join(os.path.abspath(os.getcwd()), f'tests\\{file_type}')

    dir_files = [name for name in os.listdir(choice_dir_path) if os.path.isfile(os.path.join(choice_dir_path, name))]
    file_count = len(dir_files)

    file_select_message = "Select test file "
    for idx in range(file_count):
        file_select_message += f'[{idx}]{dir_files[idx]}, '
    file_select_message += f'[{file_count}]Test All: '       

    file_choice = int(input(file_select_message))
    file = dir_files[file_choice] if file_choice < file_count else "x"

    test_type = input("Provide Test type [H]Hamilton, [E]Euler, [B]BFS, [D]DFS: ")

    return params(file_type, file, test_type, dir_files)

class Open():
    def CSV(filename, graph:model):
        with open(filename, "r") as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        graph.edges.append(row)

    def TXT(filename, graph:model):
        with open(filename,  'r') as file:
            num = int(file.readline())
            graph.txtSetup(num)
            graph.setupWeightsTXT()
            for line in file:
                command = list(map(int, line.split(' ')));
                graph.chngedg(command[0]-1, command[1]-1, '1')
                graph.setWeight(command[0]-1, command[1]-1, command[2])
                

class Affirm():
    def Ham(a):
        match a:
            case True:
                return "Hamiltonian"
            case False:
                return "Unable to make affirmation"
    def Eul(a):
        match a:
            case 1:
                return "Eulerian"
            case 2:
                return "Semi-Eulerian"
            case 0:
                return "Not Eulerian"
