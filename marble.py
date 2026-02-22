class Marble:
    __slots__ = ('id', 'name', 'stage')

    def __init__(self, name=""):
        self.id = 0
        self.name = name
        self.stage = "raw"

    def __repr__(self):
        return f"Marble(id={self.id}, name={self.name!r}, stage={self.stage!r})"
