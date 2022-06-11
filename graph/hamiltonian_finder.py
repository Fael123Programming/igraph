from abc import ABC, abstractmethod
import graph as gh


class HamiltonianFinder(ABC):
    __slots__ = ['_underlying_graph', '_path']

    def __init__(self, underlying_graph: gh.Graph):
        self._underlying_graph = underlying_graph
        self._path = []

    @property
    def underlying_graph(self):
        return self._underlying_graph

    @underlying_graph.setter
    def underlying_graph(self, underlying_graph: gh.Graph):
        if underlying_graph is None or not isinstance(underlying_graph, gh.Graph):
            return
        self._underlying_graph = underlying_graph

    @abstractmethod
    def find_all(self) -> list:
        pass

    def find_permutation(self, starting_vertex: str, id_starting_edge: int) -> list | None:
        starting_edge = self._underlying_graph.edges[id_starting_edge]
        if starting_vertex != starting_edge.vertex1 and starting_vertex != starting_edge.vertex2:
            # If starting_vertex does not belong to starting edge.
            return None
        self._find_path(starting_vertex, id_starting_edge)
        result = self._path.copy()
        self._path.clear()
        return result

    def _find_path(self, vertex: str, edge_id: int):
        self._path.append(vertex)
        next_vertex = self._find_next_vertex(vertex, edge_id)
        next_edge_id = self._find_next_edge_id(next_vertex)
        if next_edge_id == -1:
            self._path.append(next_vertex)
            return
        self._find_path(next_vertex, next_edge_id)

    def _find_next_edge_id(self, vertex: str) -> int:
        edges = self._underlying_graph.edges
        for i in range(0, len(edges)):
            current_edge = edges[i]
            vertex1 = current_edge.vertex1
            vertex2 = current_edge.vertex2
            if vertex == vertex1 and vertex2 not in self._path or vertex == vertex2 and vertex1 not in self._path:
                return i
        return -1

    def _find_next_vertex(self, vertex: str, edge_id: id) -> str | None:
        current_edge = self._underlying_graph.edges[edge_id]
        vertex1 = current_edge.vertex1
        if vertex1 != vertex:
            return vertex1
        vertex2 = current_edge.vertex2
        if vertex2 != vertex:
            return vertex2
        return None
