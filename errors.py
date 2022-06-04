class BaseGraphError(RuntimeError):
    pass


class ImpossibleToCreateEdgeError(BaseGraphError):
    def __init__(self):
        super().__init__("There is either no vertexes or only one in the graph")


class NonexistentVertexError(BaseGraphError):
    def __init__(self, vertex_name: str):
        super().__init__(f"{vertex_name} was not found in the set of vertexes of the graph")
