from Vertex import Vertex
from BreadthFirstSearch import BFS

class Graph(object):
    """
    The init fuction initialises the vertices_dict and edge_Array
    All the vertices |V| will be mapped to vertices dict
    All the Edges will be maintained in Edge Array
    Overall we are using EdgeList
    """

    def __init__(self):
        self.vertices_dict = dict()
        self.edge_array = list()

    def add_vertex(self, v):
        if isinstance(v, Vertex) and v.name not in self.vertices_dict:
            self.vertices_dict[v.name] = v
        else:
            pass

    def add_edge(self, e):
        # since e is in form of string we have split it into two variables
        u, v = list(e)
        if u in self.vertices_dict and v in self.vertices_dict:
            for each_item, each_val in self.vertices_dict.items():
                if each_item == u:
                    each_val.add_neighbour(v)
                if each_item == v:
                    each_val.add_neighbour(u)

    def print_graph(self):
        for i, j in self.vertices_dict.items():
            print i, j.neighbours,j.distance


g = Graph()
a = Vertex("A")
g.add_vertex(a)
g.add_vertex(Vertex("B"))

for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

# print g.vertices['A'].neighbours
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge)

bfs = BFS(g.vertices_dict,a)
g.print_graph()
