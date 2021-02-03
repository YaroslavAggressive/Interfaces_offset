from DirReader import DirReader
from Graph import build_graph, Graph
from GraphIterator import GraphIterator
import os

myPath = "C:\\Users\\Yaroslav\\Desktop\\YaroslavAggressive\\data"
print(os.listdir(myPath)) # проверка пути


correct_file_names = []
with DirReader(myPath) as file_names:
    for file_name in file_names:
        correct_file_names.append(file_name)

print(correct_file_names)

graph_matrix, unique_scientists = build_graph(correct_file_names)

G = Graph(graph_matrix, unique_scientists)

for science_name, count_seq in GraphIterator(G):
    print("Scientist name: " + science_name + "Number of sequnece: " + count_seq)