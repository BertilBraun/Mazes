from src.point import Point
from src.solver.node import Node


class Path:
    def __init__(self, current_node: Node) -> None:
        self.path = []
        p_node = current_node

        while p_node is not None:
            self.path.insert(0, p_node)
            p_node = p_node.parent

    def print(self) -> None:
        for node in self.path:
            print(node)

    def save(self, base_path: str, save_to_path: str) -> None:
        from PIL import Image

        points = []

        for i in range(len(self.path) - 1):
            cur = self.path[i].pos
            nxt = self.path[i + 1].pos

            if cur.y == nxt.y:
                # Ys equal - horizontal line
                for x in range(min(cur.x, nxt.x), max(cur.x, nxt.x) + 1):
                    points.append(Point(x, cur.y))
            elif cur.x == nxt.x:
                # Xs equal - vertical line
                for y in range(min(cur.y, nxt.y), max(cur.y, nxt.y) + 1):
                    points.append(Point(cur.x, y))

        length = len(points)

        colors = []
        for i in range(length):
            r = int((i / length) * 240)
            colors.append((r, 0, 240 - r))

        img = Image.open(base_path)
        rgb_img = Image.new("RGBA", img.size)
        rgb_img.paste(img)

        for i, point in enumerate(points):
            rgb_img.putpixel((point.x, point.y), colors[i])

        rgb_img.save(save_to_path)
