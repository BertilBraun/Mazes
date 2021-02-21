
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return str(self.x) + "x " + str(self.y) + "y"
