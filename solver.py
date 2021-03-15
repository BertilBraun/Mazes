import abc
from point import Point
from node import Node
from path import Path
from maze import Maze


class Solver:
    __metaclass__ = abc.ABCMeta

    def __init__(self, maze: Maze) -> None:

        array = maze.get_repr()

        self.h = len(array)
        self.w = len(array[0])
        self._nodes = [None] * (self.w * self.h)

        top_nodes = [None] * self.w

        for y in range(1, self.h - 1):
            cur = False
            nxt = array[y][1]

            left_node: Node = None

            for x in range(1, self.w - 1):
                prv = cur
                cur = nxt
                nxt = array[y][x + 1]

                if not cur:
                    # ON WALL
                    continue

                node = None

                if prv:
                    if nxt:
                        # PATH PATH PATH
                        # Create node only if paths above or below
                        if array[y - 1][x] or array[y + 1][x]:
                            node = Node(x, y)
                            left_node.neighbours.append(node)
                            node.neighbours.append(left_node)
                            left_node = node
                    else:
                        # PATH PATH WALL
                        # Create path at end of corridor
                        node = Node(x, y)
                        left_node.neighbours.append(node)
                        node.neighbours.append(left_node)
                        left_node = None
                else:
                    if nxt:
                        # WALL PATH PATH
                        # Create path at start of corridor
                        node = Node(x, y)
                        left_node = node
                    else:
                        # WALL PATH WALL
                        # Create node only if in dead end
                        if not array[y - 1][x] or not array[y + 1][x]:
                            node = Node(x, y)

                if node is not None:
                    self[x, y] = node

                    if array[y - 1][x]:
                        top_nodes[x].neighbours.append(node)
                        node.neighbours.append(top_nodes[x])

                    top_nodes[x] = node if array[y + 1][x] > 0 else None

    @abc.abstractmethod
    def solve(self, start: Point, end: Point) -> Path:
        pass

    def __setitem__(self, item: tuple, value) -> None:
        self._nodes[self._idx(item[0], item[1])] = value

    def __getitem__(self, item: tuple) -> Node:
        return self._nodes[self._idx(item[0], item[1])]

    def _idx(self, x_idx: int, y_idx: int) -> int:
        return x_idx + y_idx * self.w
