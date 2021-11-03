from Graph import Graph

class GraphIterator:

    def __init__(self, graph):
        self.graph = graph
        self.quan_of_sequences_for_sqientists = []
        self.find_seq_quan_for_scientists()
        self.quan_of_sequences_for_sqientists.sort(reverse=True)

    def find_seq_quan_for_scientists(self):
        for i in range(len(self.graph.unique_scientists_list)):
            self.quan_of_sequences_for_sqientists.append(self.graph.graph_matrix[i][i])

    def __next__(self):
        return next(self.quan_of_sequences_for_sqientists), next(self.graph.unique_scientists_list)

    def __iter__(self):
        return self


