class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return str(self.x) + "x " + str(self.y) + "y"

    @staticmethod
    def random(a: int, b: int):
        import random

        x = random.randint(0, a - 1)
        y = random.randint(0, b - 1)
        return Point(x, y)
