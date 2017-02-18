#Here are two versions where first version is Adding vertices first and then adding edges
#Second part is where only edges are added and everything is managed by the program
from __future__ import print_function


class Vertex(object):
    def __init__(self, name):
        self.name = name


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    vertices_map = {}
    edge_indices_map = {}
    edges_array = []

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex

            for row in self.edges:
                row.append(0)

            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = ord(vertex.name) % 65
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end='')
            print(' ')

    def manage_edge(self, edge):
        if edge.name not in self.vertices_map:
            self.edge_indices_map[edge.name] = ord(edge.name) % 65
            self.vertices_map[edge.name] = edge
            for row in self.edges_array:
                row.extend([0])
            self.edges_array.append([0] * (len(self.edges_array) + 1))

    def add_edges(self, edge):
        map(self.manage_edge,map(Vertex,list(edge)))

    def build_graph(self, edges):
        for k in edges:
            u, v = list(k)
            if u in self.vertices_map and v in self.vertices_map:
                self.edges_array[self.edge_indices_map[u]][self.edge_indices_map[v]] = 1
                self.edges_array[self.edge_indices_map[v]][self.edge_indices_map[u]] = 1

    def print_new_graph(self):
        for v, i in sorted(self.edge_indices_map.items()):
            print(v, self.edges_array[i])


g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('G')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()

r = Graph()
edges = ["AB", "BD", "DE", "DC", "CF"]
for edge in edges:
    r.add_edges(edge)

r.build_graph(edges)
r.print_new_graph()
