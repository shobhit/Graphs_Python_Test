class Vertex(object):
    def __init__(self, v):
        self.name = v
        self.neighbours = list()
        self.color = 'black'
        self.distance = 9999

    def add_neighbour(self, n):
        if n not in self.neighbours:
            self.neighbours.extend(n)
