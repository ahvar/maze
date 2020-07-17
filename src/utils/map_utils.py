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
    def __init__(self, enter: datetime):
        # the time when the player enters the room
        self._enter_room = None
        self.enter_room = enter

        # the time when the player leaves the room
        #self._leave_room = None
        #self.leave_room = None

    @property
    def enter_room(self):
        return self._enter_room

    @enter_room.setter
    def enter_room(self, enter_room):
        if enter_room:
            self._enter_room = enter_room
        else:
            raise Exception('The start time for the Timer could not be set')

    @property
    def leave_room(self):
        return self._leave_room

    @leave_room.setter
    def leave_room(self, leave_room):
        if leave_room:
            self._leave_room = leave_room
        else:
            raise Exception('The leave room time for Timer could not be set')

    def exit(self):
        if self._enter_room and self._leave_room:
            td_enter = datetime.timedelta(days=self.enter_room.date.day,
                                          seconds=self.enter_room.time.second,
                                          microseconds=self.enter_room.time.microsecond,
                                          minutes=self.enter_room.time.minute,
                                          hours=self.enter_room.time.hour)

            td_leave = datetime.timedelta(days=self.leave_room.date.day,
                                          seconds=self.leave_room.time.second,
                                          microseconds=self.leave_room.time.microsecond,
                                          minutes=self.leave_room.time.minute,
                                          hours=self.leave_room.time.hour)

            return td_leave - td_enter
        else:
            raise Exception('time in room error. check enter and leave times')

    def __str__(self):
        return f'{self.enter_room}'
