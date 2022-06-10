class HamiltonianPathFinder:
    __slots__ = ['_path']

    def __init__(self):
        self._path = []

    @property
    def path(self):
        return self._path

    def find(self, graph: Graph) -> list | None:
        return []

    def __str__(self):
        result = ''
        path_size = len(self._path)
        for i in range(0, path_size):
            if i < path_size - 1:
                result += f'({self._path[i]})--->'
            else:
                result += f'({self._path[i]})'
