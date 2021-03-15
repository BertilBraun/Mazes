from point import Point
from path import Path
from solver import Solver


class AStar(Solver):

    def __init__(self, path) -> None:
        super().__init__(path)

    def solve(self, start: Point, end: Point) -> Path:
        start_node = self[start.x, start.y]
        end_node = self[end.x, end.y]

        for y in range(self.h):
            for x in range(self.w):
                if self[x, y] is not None:
                    self[x, y].reset()

        start_node.local_goal = 0
        start_node.global_goal = start_node.heuristic(end_node)

        current_node = start_node
        stack = [current_node]

        while len(stack) > 0:
            stack.sort(key=lambda key: key.global_goal)

            current_node = stack.pop()

            if current_node == end_node:
                return Path(current_node)

            for node in current_node.neighbours:
                possibly_lower = current_node.local_goal + current_node.distance(node)

                if possibly_lower < node.local_goal:
                    node.parent = current_node
                    node.local_goal = possibly_lower

                    node.global_goal = node.local_goal + node.heuristic(end_node)

                    if node not in stack:
                        stack.append(node)

        raise Exception("Finished A* Algorithm without finding the end Node!")
