from edge import Edge
from errors import ImpossibleToCreateEdgeError, NonexistentVertexError


class Graph:
    __slots__ = ["_name", "_vertices", "_edges"]

    def __init__(self, name: str):
        self._name = name
        self._vertices = []
        self._edges = []

    def add_vertex(self, vertex_name: str):
        self._vertices.append(vertex_name)

    def delete_vertex(self, vertex_name: str):
        self._vertices.remove(vertex_name)

    def order(self):
        return len(self._vertices)

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
        odd_vertices = 0
        for vertex in self._vertices:  # It is executed n times, where n is the quantity of vertices
            if self.degree_of(vertex) % 2 == 1:  # It brings a cost of k where k is the quantity of edges.
                odd_vertices += 1
        return odd_vertices == 2 or odd_vertices == 0

    def is_hamiltonian(self) -> bool:
        from hamiltonian_cycle_finder import HamiltonianCycleFinder
        if self.order() < 3:
            return False
        if self.get_smallest_degree() >= self.order() / 2:  # Dirac's theorem
            return True
        hcf = HamiltonianCycleFinder(self)
        return len(hcf.find_all()) >= 1

    def get_smallest_degree(self) -> int | None:
        if self.is_null():
            return None
        if self.is_empty():
            return 0
        smallest_degree = self.degree_of(self._vertices[0])
        for i in range(1, len(self._vertices)):
            current_vertex_degree = self.degree_of(self._vertices[i])
            if current_vertex_degree < smallest_degree:
                smallest_degree = current_vertex_degree
        return smallest_degree

    def check_if_exists(self, vertex_name: str):
        if self.is_null():
            raise NonexistentVertexError(vertex_name)
        try:
            self._vertices.index(vertex_name)
        except ValueError:
            raise NonexistentVertexError(vertex_name)

    def get_vertex_by_id(self, vertex_id: int) -> str | None:
        if self.is_null() or vertex_id < 1 or vertex_id > self.order():
            return None
        return self._vertices[vertex_id - 1]

    def has_edge_between(self, vertex1: str, vertex2: str) -> bool:
        for edge in self._edges:
            if edge.vertex1 == vertex1 and edge.vertex2 == vertex2 or edge.vertex1 == vertex2 and edge.vertex2 == vertex1:
                return True
        return False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if new_name.isspace() or len(new_name) == 0:
            return
        self._name = new_name

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges
