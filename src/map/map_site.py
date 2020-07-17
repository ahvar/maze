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
        super(Wall, self).__init__()

    def enter(self):
        pass


class Door(MapSite):
    """
    One of the components used in the maze. A door is either open or closed.
    """
    def __init__(self):
        super(Door, self).__init__()
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
    def __init__(self, x_coordinate: int,
                 y_coordinate: int,
                 sides: [],
                 door: Door):
        super(Room, self).__init__()
        # four sides of the room
        self._sides = None
        self.sides = sides
        # door to the room
        self._door = None
        self.door = door

    def enter(self):
        pass

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, side_walls):
        self._sides = side_walls

    @property
    def door(self):
        return self._door

    @door.setter
    def door(self, room_door):
        self._door = room_door



