##This is the program where vertices are provided first and then edges are provided
## we will modify it just to take edges and the edgelist for it
class Vertex(object):
    def __init__(self, n):
        self.name = n
        self.neighbours = list()

    def add_neighbours(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)


class Graph:
    vertices = {}
    vertices_map = {}
    edge_arr = []

    def check_add_edge(self, edge):
        if not edge in self.vertices_map:
            self.vertices_map[edge.name] = edge
            return True
        else:
            return False

    def add_vertex(self, v):
        if isinstance(v, Vertex) and v.name not in self.vertices:
            self.vertices[v.name] = v
            return True
        else:
            return False

    def add_edge_list(self, edge):
        self.edge_arr.append(edge)
        map(self.check_add_edge,map(Vertex, list(edge)))
        # print self.edge_arr
        # print self.vertices_map


    def build_graph(self):
        for i in range(0,len(self.edge_arr)):
            u,v = list(self.edge_arr[i])
            if u in self.vertices_map and v in self.vertices_map:
                for key, value in self.vertices_map.items():
                    if key == u:
                        value.add_neighbours(v)
                    if key == v:
                        value.add_neighbours(u)

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbours(v)
                if key == v:
                    value.add_neighbours(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print key + str(self.vertices[key].neighbours)

    def print_new_graph(self):
        for key in sorted(list(self.vertices_map.keys())):
            print key + str(self.vertices_map[key].neighbours)


g = Graph()
a = Vertex("A")
g.add_vertex(a)
g.add_vertex(Vertex("B"))

for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

# print g.vertices['A'].neighbours
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()

r = Graph()
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    r.add_edge_list(edge)

r.build_graph()
r.print_new_graph()

