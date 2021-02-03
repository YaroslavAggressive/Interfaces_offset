import pytest

from DirReader import DirReader
from Graph import build_graph, Graph
from GraphIterator import GraphIterator

file_name = "test_data.txt"

def test1(): # testing function of filling in graph matrix
    graph_matrix, unique_scientists = build_graph([file_name])
    test_list = ["Yarik Tyrykin", "Yampil Darizhapov", "Antonov Aleksei"]
    for i in test:
        assert(i not in unique_scientists)

