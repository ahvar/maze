##=====================================================================================================================
## map_site module
##=====================================================================================================================

from abc import ABC, abstractmethod


class MapSite(ABC):
    """
    The common abstract class for all the components of the maze
    """
    def __init__(self):
        pass

    @abstractmethod
    def enter(self):
        pass


class Wall(MapSite):
    """
    One of the components of the maze.
    """
    def __int__(self):
        pass

    def enter(self):
        pass


class Door(MapSite):
    """
    One of the components used in the maze. A door is either open or closed.
    """
    def __init__(self):
        # the door is closed
        self.is_open = False

    def enter(self):
        """
        If the door is open, the player can move into the adjacent room
        :return:
        """
        if not self.is_open:
            print("you bumped your nose!")
        else:
            # TODO: change to another room
            pass


class Room(MapSite):
    """
    One of the components used in the maze. A room knows its neighbors; possible neighbors are another room, a wall, or
    a door to another room.
    """
    def __init__(self):
        # four sides of the room
        self.sides = [MapSite, MapSite, MapSite, MapSite]

    def enter(self):
        pass



