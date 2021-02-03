import re

WORD_SEPARATOR = "\t"


class Graph:

    def __init__(self, graph_matrix, unique_scientists_list):
        self.graph_matrix = graph_matrix
        self.unique_scientists_list = unique_scientists_list


def build_graph(file_names):
    unique_scientists = []
    output_graph = []

    for file_name in file_names:

        file = open(file_name, "r")
        first_line = file.readline()

        for line in file:

            all_scientists = [] # temp list of scientists in current line in right order

            full_name = re.match(r"\w+\s\w+", line) # split name and surname of first scientist
            while full_name is not None:
                full_name = full_name.group(0)
                all_scientists.append(full_name)

                if full_name not in unique_scientists: # we found new scientist, appending him in list and expansing matrix
                    unique_scientists.append(full_name)
                    for column in output_graph:
                        column.append(0)
                    output_graph.append([0] * (len(output_graph) + 1))

                line = line.replace(full_name + WORD_SEPARATOR, "") # split out full_name of processed scientist
                full_name = re.match(r"\w+\s\w+", line)

            for i in all_scientists:
                for j in all_scientists:
                    output_graph[unique_scientists.index(i)][unique_scientists.index(j)] += 1 #  on the main diagonal lay quantity of all discovered sequences for current scientist
            
            # отладочная печать
            # for i in range(len(output_graph)):
            #     print(output_graph[i])
            #     print("\n")

    return output_graph, unique_scientists
