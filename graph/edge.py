class Edge:
    def __init__(self, vertex1: str, vertex2: str):
        self._vertex1 = vertex1
        self._vertex2 = vertex2

    @property
    def vertex1(self):
        return self._vertex1

    @property
    def vertex2(self):
        return self._vertex2

    def __str__(self):
        return f"({self._vertex1})----({self._vertex2})"
