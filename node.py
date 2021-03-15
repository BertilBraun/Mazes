from point import Point


class Node:
    def __init__(self, x, y) -> None:
        self.pos = Point(x, y)

        self.global_goal = float("inf")
        self.local_goal = float("inf")

        self.neighbours = []
        self.parent = None

    def distance(self, other) -> float:
        return (((self.pos.x - other.pos.x) ** 2) + ((self.pos.y - other.pos.y) ** 2)) ** 0.5

    def heuristic(self, other) -> float:
        return self.distance(other)

    def reset(self):
        self.global_goal = float("inf")
        self.local_goal = float("inf")

    def __repr__(self) -> str:
        return self.pos.__repr__()


