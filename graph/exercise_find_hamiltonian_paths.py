from graph import Graph
from hamiltonian_path_finder import HamiltonianPathFinder

if __name__ == '__main__':
    g1 = Graph('g1')
    # Enter the link to see this graph more graphically
    # https://github.com/Fael123Programming/igraph/blob/main/graph/graph_images/g1.png
    g1.add_vertex('1')
    g1.add_vertex('2')
    g1.add_vertex('3')
    g1.add_vertex('4')
    g1.add_vertex('5')
    g1.add_vertex('6')
    g1.add_vertex('7')
    g1.create_edge_between('1', '2')
    g1.create_edge_between('1', '4')
    g1.create_edge_between('1', '3')
    g1.create_edge_between('2', '4')
    g1.create_edge_between('2', '3')
    g1.create_edge_between('4', '5')
    g1.create_edge_between('4', '7')
    g1.create_edge_between('5', '6')
    g1.create_edge_between('7', '6')
    hpf = HamiltonianPathFinder(g1)
    print(hpf.find_all_paths())  # [['1', '3', '2', '4', '5', '6', '7'], ['2', '3', '1', '4', '5', '6', '7'], ['3', '1',
    # '2', '4', '5', '6', '7'], ['3', '2', '1', '4', '5', '6', '7'], ['5', '6', '7', '4', '1', '2', '3'], ['7', '6', '5'
    # , '4', '1', '2', '3']]
    g2 = Graph('g2')
    # Enter the link to see this graph more graphically
    # https://github.com/Fael123Programming/igraph/blob/main/graph/graph_images/g2.png
    g2.add_vertex('1')
    g2.add_vertex('2')
    g2.add_vertex('3')
    g2.add_vertex('4')
    g2.add_vertex('5')
    g2.create_edge_between('1', '2')
    g2.create_edge_between('2', '3')
    g2.create_edge_between('4', '5')
    g2.create_edge_between('1', '4')
    hpf.graph = g2
    print(hpf.find_all_paths())  # [['3', '2', '1', '4', '5'], ['5', '4', '1', '2', '3']]
