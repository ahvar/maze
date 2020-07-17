##=====================================================================================================================
## class Maze
##=====================================================================================================================
from map.map_site import Room, Door, Wall


class Maze:
    """
    Description
    -----------
    A maze is defined as a 2D matrix of rooms.

    Notes
    -----
        1. Creation of a multidimensional list in python
        2. You could use an extension like NumPy, which has a matrix datatype to do
        the same thing, and this probably more robust


    :param width: the number of rooms in each sequence
    :param height: the number of sequences of rooms

    """
    def __init__(self, width: int, height: int):
        self._width = None
        self.width = width

        self._height = None
        self.height = height

        self._maze = None
        self.maze = [[Room] * self.width for i in range(self.height)]

    def add_room(self, room: Room):
        pass

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, lg):
        self._width = lg

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, ht):
        self._height = ht

    @property
    def maze(self):
        return self._maze

    @maze.setter
    def maze(self, mz: []):
        self._maze = mz


