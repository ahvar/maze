from enum import Enum
import datetime


class CardinalDirections(Enum):
    """
    We use this enumeration to specify the cardinal directions corresponding to sides of the room.
    """
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


class Timer:
    """
    The Timer class provides useful methods for working with times
    """
    def __init__(self):
        # the timer start time
        self._start_time = None
        self.start_time = datetime.datetime.today()

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        if start_time:
            self._start_time = start_time
        else:
            raise Exception('The start time for the Timer could not be set')

    def __str__(self):
        return f'{self.start_time}'
