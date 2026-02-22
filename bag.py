from marble import Marble


class Bag:
    def __init__(self):
        self._marbles = []
        self._counter = 0

    def add(self, marble):
        self._counter += 1
        marble.id = self._counter
        self._marbles.append(marble)
        return marble

    def marbles(self):
        return list(self._marbles)
