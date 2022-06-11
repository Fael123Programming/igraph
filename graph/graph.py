from graph.edge import Edge
from errors import ImpossibleToCreateEdgeError, NonexistentVertexError


class Graph:
    __slots__ = ["_name", "_vertexes", "_edges"]

    def __init__(self, name: str):
        self._name = name
        self._vertexes = []
        self._edges = []

    def add_vertex(self, vertex_name: str):
        self._vertexes.append(vertex_name)

    def delete_vertex(self, vertex_name: str):
        self._vertexes.remove(vertex_name)

    def order(self):
        return len(self._vertexes)

    def size(self):
        return len(self._edges)

    def is_null(self):
        return self.order() == 0  # If there is no vertexes it is null.

    def is_empty(self):
        return self.size() == 0  # If there is no edges it is empty.

    def create_edge_between(self, vertex1: str, vertex2: str):
        if self.order() < 2:
            raise ImpossibleToCreateEdgeError()
        self.check_if_exists(vertex1)  # May raise NonexistentVertexError
        self.check_if_exists(vertex2)  # May raise NonexistentVertexError
        self._edges.append(Edge(vertex1, vertex2))

    def degree_of(self, vertex: str) -> int:
        self.check_if_exists(vertex)  # May raise NonexistentVertexError
        degree = 0
        for edge in self._edges:
            if edge.vertex1 == vertex or edge.vertex2 == vertex:
                degree += 1
        return degree

    def is_eulerian(self) -> bool:
        if self.is_null() or self.is_empty():
            return False
        odd_vertexes = 0
        for vertex in self._vertexes:
            if self.degree_of(vertex) % 2 == 1:
                odd_vertexes += 1
        return odd_vertexes == 2 or odd_vertexes == 0

    def is_hamiltonian(self) -> bool:
        if self.order() < 3:
            return False
        return self.get_smallest_degree() >= self.order() / 2  # Dirac Theorem

    def get_smallest_degree(self) -> int | None:
        if self.is_null():
            return None
        if self.is_empty():
            return 0
        smallest_degree = self.degree_of(self._vertexes[0])
        for i in range(1, len(self._vertexes)):
            current_vertex_degree = self.degree_of(self._vertexes[i])
            if current_vertex_degree < smallest_degree:
                smallest_degree = current_vertex_degree
        return smallest_degree

    def check_if_exists(self, vertex_name: str):
        if self.is_null():
            raise NonexistentVertexError(vertex_name)
        try:
            self._vertexes.index(vertex_name)
        except ValueError:
            raise NonexistentVertexError(vertex_name)

    def get_vertex_by_id(self, vertex_id: int) -> str | None:
        if self.is_null() or vertex_id < 1 or vertex_id > self.order():
            return None
        return self._vertexes[vertex_id - 1]

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
