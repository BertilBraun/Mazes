
import random
from maze import Maze


def main():
    w = 50
    h = 50

    sx = random.randint(0, w - 1)
    sy = random.randint(0, h - 1)

    maze = Maze(w, h)
    maze.generate(sx, sy)
    # maze.print()
    maze.save('Maze.png')


if __name__ == '__main__':
    main()
