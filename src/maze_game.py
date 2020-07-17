#!/Users/arthurvargas/dev/src/git/maze/envs/bin/python

import map
from maze.maze import Maze
from utils import map_utils
import datetime


class MazeGame:
    """
        The MazeGame creates the maze.
    """
    def __init__(self):
        pass

    def create_maze(self):
        new_maze = Maze
        #room1 = Room
        #room2 = Room
        #door1 = Door
        #new_maze.add_room(room1)

        pass


def main():
    player = 'Arthur'
    now = datetime.datetime.today()
    print(f'{player} is entering the room at {str(now)}')
    timer = map_utils.Timer(now)



if __name__ == "__main__":
    main()