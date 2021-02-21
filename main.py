from src.maze import Maze
from src.point import Point
from src.solver.a_star import AStar


def main():
    w = 100
    h = 100

    maze = Maze(w, h)
    maze.generate(Point.random(w, h))
    # maze.print()
    maze.save('Maze.png')

    a_star = AStar('Maze.png')
    path = a_star.solve(Point(1, 1), Point(w * 2 - 1, h * 2 - 1))

    # path.print()
    path.save('Maze.png', 'MazePath.png')


if __name__ == '__main__':
    main()
