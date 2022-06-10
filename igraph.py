from errors import NonexistentVertexError
from graphic_tool import GraphicTool as gt
from graph.graph import Graph


class IGraph:
    MAIN_MENU_OPTIONS = ['Create graph', 'My Graphs', 'Eulerian Graph', 'Hamiltonian Graph', 'Credits', 'Exit']
    CREATE_GRAPH_MENU_OPTIONS = ['Create Vertex', 'Create Edge', 'Set names', 'See Vertexes', 'See Edges',
                                 'Save', 'Back']
    SET_NAME_MENU_OPTIONS = ['Rename graph', 'Rename vertexes', 'Back']

    @staticmethod
    def start():
        IGraph._main_menu()

    @staticmethod
    def _main_menu():
        while True:
            gt.title('Welcome to iGraph')
            gt.print_menu_options(IGraph.MAIN_MENU_OPTIONS)
            gt.row()
            chosen_opt = input("-> ")
            gt.clean_prompt()
            if IGraph._is_invalid_option(chosen_opt, IGraph.MAIN_MENU_OPTIONS):
                gt.title(f'### Invalid option: {chosen_opt} ###')
                gt.wait()
            else:
                match chosen_opt:
                    case "1":
                        IGraph._create_graph()
                    case "2":
                        IGraph._my_graphs()
                    case "3":
                        IGraph._eulerian_graph()
                    case "4":
                        IGraph._hamiltonian_graph()
                    case "5":
                        IGraph._credits()
                    case "6":
                        IGraph._exit()
            gt.clean_prompt()

    @staticmethod
    def _is_invalid_option(opt: str, menu_options: list) -> bool:
        if not opt.isdigit():
            return True
        casted_opt = int(opt)
        return not (1 <= casted_opt <= len(menu_options))

    @staticmethod
    def _create_graph():
        new_graph = Graph("<unnamed>")
        while True:
            gt.title(f'Create New Graph: {new_graph.name}')
            gt.print_menu_options(IGraph.CREATE_GRAPH_MENU_OPTIONS)
            gt.row()
            chosen_opt = input("-> ")
            gt.clean_prompt()
            if IGraph._is_invalid_option(chosen_opt, IGraph.CREATE_GRAPH_MENU_OPTIONS):
                gt.title("### Invalid option ###")
                gt.wait()
                gt.clean_prompt()
            else:
                match chosen_opt:
                    case '1':
                        vertex_name = IGraph._get_name()
                        gt.clean_prompt()
                        if vertex_name is not None:
                            try:
                                new_graph.check_if_exists(vertex_name)
                            except NonexistentVertexError:
                                new_graph.add_vertex(vertex_name)
                                gt.title(f'Vertex named {vertex_name} created!')
                                gt.wait()
                            else:
                                gt.title(f'A vertex named ({vertex_name}) already exists in the graph')
                                gt.wait()
                            gt.clean_prompt()
                    case '2':
                        if new_graph.order() < 2:
                            gt.title('At least two vertexes must exist in the graph')
                        else:
                            while True:
                                vertex1_name = IGraph._get_name('Create Edge - first vertex')
                                if vertex1_name is not None:
                                    try:
                                        new_graph.check_if_exists(vertex1_name)
                                    except NonexistentVertexError as error:
                                        gt.clean_prompt()
                                        gt.title(error.__str__())
                                        gt.wait(2)
                                        gt.clean_prompt()
                                    else:
                                        break
                                else:
                                    break
                            if vertex1_name is not None:
                                gt.clean_prompt()
                                while True:
                                    vertex2_name = IGraph._get_name('Create Edge - second vertex')
                                    if vertex2_name is not None:
                                        try:
                                            new_graph.check_if_exists(vertex2_name)
                                        except NonexistentVertexError as error:
                                            gt.clean_prompt()
                                            gt.title(error.__str__())
                                            gt.wait(2)
                                            gt.clean_prompt()
                                        else:
                                            break
                                    else:
                                        break
                                if vertex2_name is not None:
                                    gt.clean_prompt()
                                    gt.title(f'Create an edge between ({vertex1_name}) and ({vertex2_name})? [y/n]')
                                    answer = input('-> ').lower()[0]
                                    while answer not in ('y', 'n'):
                                        gt.clean_prompt()
                                        gt.title("### Invalid answer: use 'y' or 'n' ###")
                                        gt.wait()
                                        gt.clean_prompt()
                                        gt.title(f'Create an edge between ({vertex1_name}) and ({vertex2_name})? [y/n]')
                                        answer = input('-> ').lower()[0]
                                    gt.clean_prompt()
                                    if answer == 'y':
                                        new_graph.create_edge_between(vertex1_name, vertex2_name)
                                        gt.title(f'Edge created!')
                                    else:
                                        gt.title('Canceled')
                    case '3':
                        while True:
                            gt.title('Set Names')
                            gt.print_menu_options(IGraph.SET_NAME_MENU_OPTIONS)
                            gt.row()
                            chosen_opt = input('-> ')
                            gt.clean_prompt()
                            if IGraph._is_invalid_option(chosen_opt, IGraph.SET_NAME_MENU_OPTIONS):
                                gt.title("### Invalid option ###")
                                gt.wait()
                                gt.clean_prompt()
                            else:
                                match chosen_opt:
                                    case '1':
                                        new_graph_name = IGraph._get_name(f'Set Graph Name (current: \'{new_graph.name}'
                                                                          f'\')', 'New graph name')
                                        gt.clean_prompt()
                                        if new_graph_name is not None:
                                            gt.clean_prompt()
                                            gt.title(f'Rename graph from ({new_graph.name}) to ({new_graph_name})? [y/n'
                                                     f']')
                                            answer = input('-> ')[0].lower()
                                            while answer not in ('y', 'n'):
                                                gt.clean_prompt()
                                                gt.title("### Invalid answer: use 'y' or 'n' ###")
                                                gt.wait()
                                                gt.clean_prompt()
                                                gt.title(f'Rename graph from ({new_graph.name}) to ({new_graph_name})? '
                                                         f'[y/n]')
                                                answer = input('-> ')[0].lower()
                                            gt.clean_prompt()
                                            if answer == 'y':
                                                new_graph.name = new_graph_name
                                                gt.title(f'Graph renamed!')
                                                gt.wait()
                                            else:
                                                gt.title('Canceled')
                                                gt.wait()
                                            gt.clean_prompt()
                                    case '2':
                                        if new_graph.is_null():
                                            gt.title('The graph does not have any vertex')
                                            gt.wait()
                                            gt.clean_prompt()
                                        else:
                                            while True:
                                                gt.title('Set Vertex Name')
                                                i = 1
                                                print(f"{'Vertex id': <20}{'Vertex Name'}")
                                                gt.row()
                                                for vertex in new_graph.vertexes.values():
                                                    print(f"{i: < 20}{vertex.name}")
                                                    i += 1
                                                gt.row()
                                                vertex_id = input('Enter a vertex id (-1 to cancel): ')
                                                gt.clean_prompt()
                                                if vertex_id == '-1':
                                                    gt.title('Canceled')
                                                    gt.wait()
                                                    gt.clean_prompt()
                                                    break
                                                if not vertex_id.isdigit():
                                                    gt.title('### Enter a valid vertex id or -1 ###')
                                                    gt.wait()
                                                    gt.clean_prompt()
                                                else:
                                                    casted_vertex_id = int(vertex_id)
                                                    if casted_vertex_id < 1 or casted_vertex_id > new_graph.order():
                                                        gt.title('### Enter a valid vertex id or -1 ###')
                                                        gt.wait()
                                                        gt.clean_prompt()
                                                    else:
                                                        vertex = new_graph.get_vertex_by_id(casted_vertex_id)
                                                        vertex_new_name = IGraph._get_name(
                                                            f'Set Vertex Name: {vertex.name}',
                                                            'Enter the new name'
                                                        )
                                                        gt.clean_prompt()
                                                        if vertex_new_name is not None:
                                                            gt.title(f'Rename vertex from ({vertex.name}) to '
                                                                     f'({vertex_new_name})? [y/n]')
                                                            answer = input('-> ')[0].lower()
                                                            gt.clean_prompt()
                                                            while answer not in ('y', 'n'):
                                                                gt.title("### Invalid answer: use 'y' or 'n' ###")
                                                                gt.wait()
                                                                gt.clean_prompt()
                                                                gt.title(f'Rename vertex from ({vertex.name}) to '
                                                                         f'({vertex_new_name})? [y/n]')
                                                                answer = input('-> ')[0].lower()
                                                                gt.clean_prompt()
                                                            if answer == 'y':
                                                                vertex.name = vertex_new_name
                                                                gt.title('Vertex renamed!')
                                                                gt.wait()
                                                                gt.clean_prompt()
                                                            else:
                                                                gt.title('Canceled')
                                                                gt.wait()
                                                                gt.clean_prompt()
                                    case '3':
                                        break
                    case '6':
                        pass
                    case '7':
                        gt.row()
                        print('Are you sure about that?'.center(gt.DEFAULT_SIZE_ROW))
                        print('If you do it without saving your graph'.center(gt.DEFAULT_SIZE_ROW))
                        print('you will lose all your job!'.center(gt.DEFAULT_SIZE_ROW))
                        print('Proceed? [y/n]'.center(gt.DEFAULT_SIZE_ROW))
                        gt.row()
                        answer = input('-> ')[0].lower()
                        gt.clean_prompt()
                        while answer not in ('y', 'n'):
                            gt.title("### Invalid answer: use 'y' or 'n' ###")
                            gt.wait()
                            gt.clean_prompt()
                            gt.row()
                            print('Are you sure about that?'.center(gt.DEFAULT_SIZE_ROW))
                            print('If you do it without saving your graph'.center(gt.DEFAULT_SIZE_ROW))
                            print('you will lose all your job!'.center(gt.DEFAULT_SIZE_ROW))
                            print('Proceed? [y/n]'.center(gt.DEFAULT_SIZE_ROW))
                            gt.row()
                            answer = input('-> ')[0].lower()
                            gt.clean_prompt()
                        if answer == 'y':
                            del new_graph
                            break

    @staticmethod
    def _my_graphs():
        gt.title('My Graphs')
        gt.wait(2)

    @staticmethod
    def _eulerian_graph():
        gt.title('Eulerian Graph')
        gt.wait(2)

    @staticmethod
    def _hamiltonian_graph():
        gt.title('Hamiltonian Graph')
        gt.wait(2)

    @staticmethod
    def _credits():
        gt.title('Credits')
        gt.wait(2)

    @staticmethod
    def _exit():
        gt.title('Exiting...')
        gt.wait(2)
        gt.clean_prompt()
        exit(0)

    @staticmethod
    def _get_name(title_msg='Create Vertex', ask_msg='Vertex name', error_msg='### Invalid name ###') -> str | None:
        gt.title(title_msg)
        name = input(f"{ask_msg} (-1 to cancel): ")
        if name == '-1':
            gt.clean_prompt()
            gt.title('Canceled')
            return None
        while name.isspace() or len(name) == 0:
            gt.clean_prompt()
            gt.title(error_msg)
            gt.wait()
            gt.clean_prompt()
            gt.title(title_msg)
            name = input(f"{ask_msg} (-1 to cancel): ")
            if name == '-1':
                gt.clean_prompt()
                gt.title('Canceled')
                return None
        return name
