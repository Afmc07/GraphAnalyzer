import copy
from Classes.adjacencyMatrix import AdjacencyMatrix
from Classes.params import params
import csv
import os

test_message = "Select a Test type\n [H]Hamilton\n [E]Euler\n [B]BFS\n [D]DFS\n [K]Dijkstra\n [F]Bellman Ford\n [W]Floyd Warshall:\n "


def Setup():
    file_type = input("Please select a file input type: [csv]CSV [txt]TXT [special]special: ")

    choice_dir_path = os.path.join(os.path.abspath(os.getcwd()), f'tests\\{file_type}')

    dir_files = [name for name in os.listdir(choice_dir_path) if os.path.isfile(os.path.join(choice_dir_path, name))]
    file_count = len(dir_files)

    file = __fileSelectProcess(file_count, dir_files)

    test_type = input(test_message)

    return params(file_type, file, test_type, dir_files)


def RepeatSetup(past_params: params):
    newparams: params = copy.deepcopy(past_params)
    change_response = input(f'Do you want to change your current file type?({past_params.fileType}) Y/N: ')

    if change_response == 'Y':
        if past_params.fileType == 'txt':
            newparams.fileType = 'csv'
        else:
            newparams.fileType = 'txt'
        print(f'File type changed to {newparams.fileType}')

        choice_dir_path = os.path.join(os.path.abspath(os.getcwd()), f'tests\\{newparams.fileType}')
        newparams.fileList = [name for name in os.listdir(choice_dir_path) if
                              os.path.isfile(os.path.join(choice_dir_path, name))]

    newparams.fileName = __fileSelectProcess(len(newparams.fileList), newparams.fileList)

    newparams.testId = input(test_message)

    return newparams


def __fileSelectProcess(file_count: int, file_list: list):
    message = "Select test file\n"

    for idx in range(file_count):
        message += f'[{idx}]{file_list[idx]}\n'
    message += f'[{file_count}]Test All:\n'

    file_choice = int(input(message))
    file = file_list[file_choice] if file_choice < file_count else "x"

    return file


class Open:
    def CSV(filename: str, graph: AdjacencyMatrix):
        with open(filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            counter = 1
            for row in reader:
                if counter == 1:
                    graph.setLabels(row)
                else:
                    graph.edges.append(row)

    def TXT(filename: str, graph: AdjacencyMatrix):
        dirgraph = input("Is the graph directed? Y/N: ")
        with open(filename, 'r') as file:
            num = int(file.readline())
            graph.txtSetup(num)
            graph.setupWeightsTXT()
            for line in file:
                formated_line = list(line.split(' '))
                if len(formated_line) == 3:
                    command = list(map(int, formated_line))
                    if dirgraph == 'N':
                        graph.chngEdg(command[0] - 1, command[1] - 1, '1')
                        graph.setWeight(command[0] - 1, command[1] - 1, command[2])
                    else:
                        graph.chngDirEdg(command[0] - 1, command[1] - 1, '1')
                        graph.setDirWeight(command[0] - 1, command[1] - 1, command[2])
                else:
                    graph.setLabels(formated_line)

    def special(filename: str, graph: AdjacencyMatrix):
        with open(filename, 'r') as file:
            labels = file.readline().split(' ')
            graph.setLabels(labels)
            for line in file:
                initial = list(line.split(' '))
                formatted_edges = ['' if x == 'I' or x == 'I\n' else '1' for x in initial]
                formatted_weights = [0 if x == 'I' or x == 'I\n' else int(x) for x in initial]
                graph.edges.append(formatted_edges)
                graph.weights.append(formatted_weights)


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
