from errors import NonexistentVertexError
from graphic_tool import GraphicTool as gt
from graph import Graph


class IGraph:
    MAIN_MENU_OPTIONS = ['Create graph', 'My Graphs', 'Eulerian Graph', 'Hamiltonian Graph', 'Credits', 'Exit']
    CREATE_GRAPH_MENU_OPTIONS = ['Create Vertex', 'Create Edge', 'Set names', 'See Vertexes', 'See Edges',
                                 'Create Graph', 'Main Menu']

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
            gt.title('Create New Graph')
            gt.print_menu_options(IGraph.CREATE_GRAPH_MENU_OPTIONS)
            gt.row()
            chosen_opt = input("-> ")
            gt.clean_prompt()
            if IGraph._is_invalid_option(chosen_opt, IGraph.CREATE_GRAPH_MENU_OPTIONS):
                gt.title(f"### Invalid option: {chosen_opt} ###")
            else:
                match chosen_opt:
                    case "1":
                        vertex_name = IGraph._get_vertex_name('Create Vertex')
                        if vertex_name is None:  # User has given up creating a new vertex
                            break
                        new_graph.add_vertex(vertex_name)
                        gt.title(f'Vertex named {vertex_name} created!')
                    case "2":
                        if new_graph.order() < 2:
                            gt.title('At least two vertexes must exist in the graph')
                            break
                        while True:
                            vertex1_name = IGraph._get_vertex_name('Create Edge')
                            if vertex1_name is None:
                                break
                            try:
                                new_graph.check_if_exists(vertex1_name)
                            except NonexistentVertexError as error:
                                gt.title(error.__str__())
                                gt.wait()
                                gt.clean_prompt()
                            else:
                                break
                        if vertex1_name is None:
                            break
                        while True:
                            vertex2_name = IGraph._get_vertex_name('Create Edge')
                            if vertex2_name is None:
                                break
                            try:
                                new_graph.check_if_exists(vertex2_name)
                            except NonexistentVertexError as error:
                                gt.title(error.__str__())
                                gt.wait()
                                gt.clean_prompt()
                            else:
                                break
                        if vertex2_name is None:
                            break
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
                            gt.title('Canceled!')
                    case "7":
                        return
            gt.wait()
            gt.clean_prompt()

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
        gt.title('Closing program...')
        gt.wait(2)
        gt.clean_prompt()
        exit(0)

    @staticmethod
    def _get_vertex_name(title_msg: str) -> str|None:
        gt.title(title_msg)
        vertex_name = input("Vertex name (-1 to cancel): ")
        if vertex_name == '-1':
            gt.clean_prompt()
            gt.title('Canceled!')
            return None
        while vertex_name.isspace() or len(vertex_name) == 0:
            gt.clean_prompt()
            gt.title('### Invalid vertex name ###')
            gt.wait()
            gt.clean_prompt()
            gt.title(title_msg)
            vertex_name = input("Vertex name (-1 to cancel): ")
            if vertex_name == '-1':
                gt.clean_prompt()
                gt.title('Canceled!')
                return None
        gt.clean_prompt()
        return vertex_name

