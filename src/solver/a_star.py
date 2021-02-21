from PIL import Image
import numpy as np

from src.point import Point
from src.solver.node import Node
from src.solver.path import Path


class AStar:

    def __init__(self, path) -> None:

        array = np.asarray(Image.open(path))

        self.nodes = []
        self.h = array.shape[0]
        self.w = array.shape[1]

        for y in range(self.h):
            for x in range(self.w):
                self.nodes.append(Node(y, x, array[y, x] == 0))

        for y in range(self.h):
            for x in range(self.w):
                if y > 0:
                    self[x, y].neighbours.append(self[x, y - 1])
                if y < self.h - 1:
                    self[x, y].neighbours.append(self[x, y + 1])
                if x > 0:
                    self[x, y].neighbours.append(self[x - 1, y])
                if x < self.w - 1:
                    self[x, y].neighbours.append(self[x + 1, y])

    def solve(self, start: Point, end: Point) -> Path:
        start_node = self[start.x, start.y]
        end_node = self[end.x, end.y]

        for y in range(self.h):
            for x in range(self.w):
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

                    if node not in stack and not node.obstacle:
                        stack.append(node)

    def __getitem__(self, item: tuple) -> Node:
        return self.nodes[self.idx(item[0], item[1])]

    def idx(self, x_idx, y_idx) -> int:
        return x_idx + y_idx * self.w
