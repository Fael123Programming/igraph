from vertex import Vertex
from edge import Edge
from errors import ImpossibleToCreateEdgeError, NonexistentVertexError


class Graph:
    __slots__ = ["_name", "_vertexes", "_edges"]

    def __init__(self, name: str):
        self._name = name
        self._vertexes = dict()
        self._edges = []

    def add_vertex(self, vertex_name: str):
        self._vertexes[vertex_name] = Vertex(vertex_name)

    def delete_vertex(self, vertex_name: str):
        del self._vertexes[vertex_name]
        # Deleting a non-existing key may throw a KeyError

    def order(self):
        return len(self._vertexes)

    def size(self):
        return len(self._edges)

    def is_null(self):
        return self.order() == 0  # If there is no vertexes it is null.

    def is_empty(self):
        return self.size() == 0  # If there is no edges it is empty.

    def create_edge_between(self, vertex1_name: str, vertex2_name: str):
        if self.order() < 2:
            raise ImpossibleToCreateEdgeError()
        self._check_if_exists(vertex1_name)  # May raise NonexistentVertexError
        self._check_if_exists(vertex2_name)  # May raise NonexistentVertexError
        self._edges.append(Edge(vertex1_name, vertex2_name))

    def degree_of(self, vertex_name: str) -> int:
        self._check_if_exists(vertex_name)  # May raise NonexistentVertexError
        degree = 0
        for edge in self._edges:
            if edge.vertex1_name == vertex_name or edge.vertex2_name == vertex_name:
                degree += 1
        return degree

    def is_eulerian(self) -> bool:
        if self.is_null() or self.is_empty():
            return False
        odd_vertexes = 0
        for vertex_name in self._vertexes.keys():
            if self.degree_of(vertex_name) % 2 == 1:
                odd_vertexes += 1
        return odd_vertexes == 2 or odd_vertexes == 0

    def check_if_exists(self, vertex_name: str):
        if self.is_null():
            raise NonexistentVertexError(vertex_name)
        try:
            self._vertexes[vertex_name]  # Accessing the referred vertex if it exists...
        except KeyError:  # If vertex_name is not the name of a vertex of the graph
            raise NonexistentVertexError(vertex_name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if new_name.isspace() or len(new_name) == 0:
            return
        self._name = new_name

    @property
    def vertexes(self):
        return self._vertexes

    @property
    def edges(self):
        return self._edges
