if __name__ == '__main__':
    from graph import Graph
    from hamiltonian_cycle_finder import HamiltonianCycleFinder
    g3 = Graph('g3')
    # Go to the following link to see this graph more graphically
    # https://github.com/Fael123Programming/igraph/blob/main/graph/graph_images/g3.png
    g3.add_vertex('1')
    g3.add_vertex('2')
    g3.add_vertex('3')
    g3.add_vertex('4')
    g3.add_vertex('5')
    g3.add_vertex('6')
    g3.create_edge_between('1', '2')
    g3.create_edge_between('2', '3')
    g3.create_edge_between('3', '4')
    g3.create_edge_between('4', '5')
    g3.create_edge_between('5', '1')
    g3.create_edge_between('1', '6')
    g3.create_edge_between('5', '6')
    hcf = HamiltonianCycleFinder(g3)
    print(hcf.find_all())
    print(f'{g3.name} is ', end='')
    if g3.is_hamiltonian():
        print('hamiltonian!')
    else:
        print('not hamiltonian!')
