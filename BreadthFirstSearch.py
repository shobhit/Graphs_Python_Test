class BFS(object):
    def __init__(self, vertices, vert):
        self.vertices = vertices
        self.vert = vert
        self.bfs(self.vert)

    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.color = 'red'
        for v in vert.neighbours:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)
        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbours:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1
