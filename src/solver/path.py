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
        import numpy as np
        from PIL import Image

        array = np.asarray(Image.open(base_path)).copy()
        for node in self.path:
            array[node.pos.x, node.pos.y] = 128

        im = Image.fromarray(array)
        im.save(save_to_path)
