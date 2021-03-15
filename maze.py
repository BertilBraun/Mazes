from point import Point


class Maze:
    PATH_N = 0x01
    PATH_E = 0x02
    PATH_S = 0x04
    PATH_W = 0x08
    VISITED = 0x10

    def __init__(self, w, h) -> None:
        self.w = w
        self.h = h
        self.grid = [0] * (w * h)
        self.repr = None

    def generate(self, start: Point, draw) -> None:
        import random

        stack = [start]
        self[start.x, start.y] = Maze.VISITED
        draw(start.x, start.y)

        def offset(ox, oy) -> tuple:
            return stack[-1].x + ox, stack[-1].y + oy

        def draw_offset(ox, oy):
            draw(stack[-1].x * 2 + 1 + ox, stack[-1].y * 2 + 1 + oy)

        while len(stack) > 0:
            neighbours = []

            draw_offset(0, 0)

            if stack[-1].y > 0 and self[offset(0, -1)] & Maze.VISITED == 0:
                neighbours.append(0)
            if stack[-1].x < self.w - 1 and self[offset(1, 0)] & Maze.VISITED == 0:
                neighbours.append(1)
            if stack[-1].y < self.h - 1 and self[offset(0, 1)] & Maze.VISITED == 0:
                neighbours.append(2)
            if stack[-1].x > 0 and self[offset(-1, 0)] & Maze.VISITED == 0:
                neighbours.append(3)

            if len(neighbours) == 0:
                stack.pop()
            else:
                next_dir = random.choice(neighbours)

                if next_dir == 0:
                    self[offset(0, -1)] |= Maze.VISITED | Maze.PATH_S
                    self[offset(0, 0)] |= Maze.PATH_N
                    stack.append(Point(stack[-1].x + 0, stack[-1].y - 1))
                    draw_offset(0, -1)
                elif next_dir == 1:
                    self[offset(+1, 0)] |= Maze.VISITED | Maze.PATH_W
                    self[offset(0, 0)] |= Maze.PATH_E
                    stack.append(Point(stack[-1].x + 1, stack[-1].y + 0))
                    draw_offset(1, 1)
                elif next_dir == 2:
                    self[offset(0, +1)] |= Maze.VISITED | Maze.PATH_N
                    self[offset(0, 0)] |= Maze.PATH_S
                    stack.append(Point(stack[-1].x + 0, stack[-1].y + 1))
                    draw_offset(0, 1)
                elif next_dir == 3:
                    self[offset(-1, 0)] |= Maze.VISITED | Maze.PATH_E
                    self[offset(0, 0)] |= Maze.PATH_W
                    stack.append(Point(stack[-1].x - 1, stack[-1].y + 0))
                    draw_offset(-1, 0)

    def __setitem__(self, item: tuple, value) -> None:
        self.grid[self.idx(item[0], item[1])] = value

    def __getitem__(self, item: tuple) -> int:
        return self.grid[self.idx(item[0], item[1])]

    def idx(self, x_idx, y_idx) -> int:
        return x_idx + y_idx * self.w

    def get_repr(self):
        if self.repr == None:
            self.repr = self._gen_repr()
        return self.repr

    def _gen_repr(self):
        data = []
        line = [0] * (self.w * 2 + 1)
        data.append(line)
        for y in range(self.h):
            line = [0]
            for x in range(self.w):
                if self.grid[self.idx(x, y)] & Maze.PATH_E:
                    line.append(1)
                    line.append(1)
                else:
                    line.append(1)
                    line.append(0)

            data.append(line)
            line = [0]
            for x in range(self.w):
                if self.grid[self.idx(x, y)] & Maze.PATH_S:
                    line.append(1)
                    line.append(0)
                else:
                    line.append(0)
                    line.append(0)

            data.append(line)

        return data