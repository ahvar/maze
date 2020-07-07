#!/Users/arthurvargas/dev/src/git/maze/envs/bin/python

import map
from maze.maze import Maze
from utils import map_utils


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
    timer = map_utils.Timer()
    print(f'Print start time: {timer.start_time}')
    print(f'Print timer:  {timer}')


if __name__ == "__main__":
    main()