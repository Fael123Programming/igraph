class Vertex:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if new_name.isspace() or len(new_name) == 0:
            return
        self._name = new_name

    def __str__(self):
        return f"({self._name})"
