from hamiltonian_finder import HamiltonianFinder


class HamiltonianPathFinder(HamiltonianFinder):
    from graph import Graph

    def __init__(self, underlying_graph: Graph):
        super().__init__(underlying_graph)

    # Override
    def find_all(self) -> list:
        paths = []
        vertices = self.underlying_graph.vertices
        edges = self.underlying_graph.edges
        for vertex_id in range(len(vertices)):  # n
            current_vertex = vertices[vertex_id]
            for edge_id in range(len(edges)):  # k
                current_edge = edges[edge_id]
                if current_edge.vertex1 == current_vertex or current_edge.vertex2 == current_vertex:
                    path = self.find_permutation(current_vertex, edge_id)  # n*k
                    if len(path) == len(vertices):
                        paths.append(path)
        return paths
