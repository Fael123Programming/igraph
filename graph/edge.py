class Edge:
    def __init__(self, vertex1_name: str, vertex2_name: str):
        self._vertex1_name = vertex1_name
        self._vertex2_name = vertex2_name

    @property
    def vertex1_name(self):
        return self._vertex1_name

    @property
    def vertex2_name(self):
        return self._vertex2_name

    def __str__(self):
        return f"({self._vertex1_name})----({self._vertex2_name})"
