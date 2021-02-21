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

        colors = []
        for i in range(len(self.path)):
            fract = i / len(self.path)
            colors.append((int(fract * 240), 0, int((1 - fract) * 240)))

        img = Image.open(base_path)
        rgb_img = Image.new("RGBA", img.size)
        rgb_img.paste(img)

        for i, node in enumerate(self.path):
            rgb_img.putpixel((node.pos.x, node.pos.y), colors[i])

        rgb_img.save(save_to_path)
