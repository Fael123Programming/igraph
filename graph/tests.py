from graph import Graph
from hamiltonian_path_finder import HamiltonianPathFinder

if __name__ == '__main__':
    g1 = Graph('g1')
    g1.add_vertex('x1')
    g1.add_vertex('x2')
    g1.add_vertex('x3')
    g1.add_vertex('x4')
    g1.create_edge_between('x1', 'x2')
    g1.create_edge_between('x1', 'x3')
    g1.create_edge_between('x4', 'x3')
    g1.create_edge_between('x2', 'x3')
    # print(g1.order())
    # print(g1.size())
    # print(g1.get_smallest_degree())
    # for edge in g1.edges:
    #     print(edge)
    # print(g1.is_eulerian())
    # print(g1.is_hamiltonian())
    hpf = HamiltonianPathFinder(g1)
    print(hpf.find_all_paths())
