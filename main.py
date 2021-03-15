from maze import Maze
from point import Point
from a_star import AStar

w = 100
h = 100

print('Started')

maze = Maze(w, h)
maze.generate(Point.random(w, h))

# TODO input these points
start = Point(1, 1)
end = Point(w * 2 - 1, h * 2 - 1)

path = AStar(maze).solve(start, end)

# path.print()
path.draw(maze)
