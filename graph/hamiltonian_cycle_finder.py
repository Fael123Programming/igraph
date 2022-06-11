from hamiltonian_finder import HamiltonianFinder


class HamiltonianCycleFinder(HamiltonianFinder):
    from graph import Graph

    def __init__(self, underlying_graph: Graph):
        super().__init__(underlying_graph)

    # Override
    def find_all(self) -> list:
        cycles = []
        vertices = self.underlying_graph.vertices
        edges = self.underlying_graph.edges
        for vertex_id in range(len(vertices)):
            current_vertex = vertices[vertex_id]
            for edge_id in range(len(edges)):
                current_edge = edges[edge_id]
                if current_edge.vertex1 == current_vertex or current_edge.vertex2 == current_vertex:
                    path = self.find_permutation(current_vertex, edge_id)
                    path_len = len(path)
                    if path_len == len(vertices) and self.underlying_graph.has_edge_between(path[0], path[path_len - 1]):
                        cycles.append(path + [path[0]])
        return cycles
