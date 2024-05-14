import numpy as np
from stl import mesh
import os

class InteriorItem:
    def __init__(self, width, depth, height, material):
        self.width = width
        self.depth = depth
        self.height = height
        self.material = material

    def create_mesh(self):
        raise NotImplementedError("Subclasses should implement this method")

    def save_stl(self, filename):
        item_mesh = self.create_mesh()
        item_mesh.save(filename)


class Sofa(InteriorItem):
    def __init__(self, width, depth, height, material, cushion_count, armrest):
        super().__init__(width, depth, height, material)
        self.cushion_count = cushion_count
        self.armrest = armrest

    def create_mesh(self):
        # ソファの詳細なモデル
        vertices = np.array([
            [0, 0, 0], [self.width, 0, 0], [self.width, self.depth, 0], [0, self.depth, 0],  # 底面
            [0, 0, self.height], [self.width, 0, self.height], [self.width, self.depth, self.height], [0, self.depth, self.height],  # 上面
            [0, 0, self.height/2], [self.width, 0, self.height/2], [self.width, self.depth, self.height/2], [0, self.depth, self.height/2],  # 中間面
            [0, self.depth/4, self.height], [self.width, self.depth/4, self.height], [self.width, 3*self.depth/4, self.height], [0, 3*self.depth/4, self.height],  # 背もたれ上面
            [0, self.depth/4, self.height*0.8], [self.width, self.depth/4, self.height*0.8], [self.width, 3*self.depth/4, self.height*0.8], [0, 3*self.depth/4, self.height*0.8]  # 背もたれ中間面
        ])
        faces = np.array([
            [0, 1, 2], [0, 2, 3],  # 底面
            [4, 5, 6], [4, 6, 7],  # 上面
            [0, 1, 5], [0, 5, 4],  # 前面
            [2, 3, 7], [2, 7, 6],  # 後面
            [1, 2, 6], [1, 6, 5],  # 右側面
            [0, 3, 7], [0, 7, 4],  # 左側面
            [8, 9, 10], [8, 10, 11],  # 中間面
            [12, 13, 14], [12, 14, 15],  # 背もたれ上面
            [16, 17, 18], [16, 18, 19]  # 背もたれ中間面
        ])
        return mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype), remove_empty_areas=False)

class Table(InteriorItem):
    def __init__(self, width, depth, height, material, leg_count, top_shape):
        super().__init__(width, depth, height, material)
        self.leg_count = leg_count
        self.top_shape = top_shape

    def create_mesh(self):
        # テーブルの詳細なモデル
        vertices = np.array([
            [0, 0, 0], [self.width, 0, 0], [self.width, self.depth, 0], [0, self.depth, 0],  # 底面
            [0, 0, self.height], [self.width, 0, self.height], [self.width, self.depth, self.height], [0, self.depth, self.height],  # 上面
            [self.width/4, self.depth/4, 0], [3*self.width/4, self.depth/4, 0], [3*self.width/4, 3*self.depth/4, 0], [self.width/4, 3*self.depth/4, 0],  # 脚
            [self.width/2, self.depth/2, self.height]  # 天板中心
        ])
        faces = np.array([
            [0, 1, 2], [0, 2, 3],  # 底面
            [4, 5, 6], [4, 6, 7],  # 上面
            [0, 1, 5], [0, 5, 4],  # 前面
            [2, 3, 7], [2, 7, 6],  # 後面
            [1, 2, 6], [1, 6, 5],  # 右側面
            [0, 3, 7], [0, 7, 4],  # 左側面
            [8, 9, 10], [8, 10, 11],  # 脚
            [4, 5, 12], [5, 6, 12], [6, 7, 12], [4, 7, 12]  # 天板
        ])
        return mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype), remove_empty_areas=False)

class Chair(InteriorItem):
    def __init__(self, width, depth, height, material, backrest_height, seat_shape):
        super().__init__(width, depth, height, material)
        self.backrest_height = backrest_height
        self.seat_shape = seat_shape

    def create_mesh(self):
        # 椅子の詳細なモデル
        vertices = np.array([
            [0, 0, 0], [self.width, 0, 0], [self.width, self.depth, 0], [0, self.depth, 0],  # 底面
            [0, 0, self.height], [self.width, 0, self.height], [self.width, self.depth, self.height], [0, self.depth, self.height],  # 上面
            [0, 0, self.backrest_height], [self.width, 0, self.backrest_height], [self.width, self.depth, self.backrest_height], [0, self.depth, self.backrest_height],  # 背もたれ上面
            [self.width/4, self.depth/4, self.height/2], [3*self.width/4, self.depth/4, self.height/2], [3*self.width/4, 3*self.depth/4, self.height/2], [self.width/4, 3*self.depth/4, self.height/2]  # 座面
        ])
        faces = np.array([
            [0, 1, 2], [0, 2, 3],  # 底面
            [4, 5, 6], [4, 6, 7],  # 上面
            [0, 1, 5], [0, 5, 4],  # 前面
            [2, 3, 7], [2, 7, 6],  # 後面
            [1, 2, 6], [1, 6, 5],  # 右側面
            [0, 3, 7], [0, 7, 4],  # 左側面
            [8, 9, 10], [8, 10, 11],  # 背もたれ上面
            [12, 13, 14], [12, 14, 15]  # 座面
        ])
        return mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype), remove_empty_areas=False)

class Lamp(InteriorItem):
    def __init__(self, width, depth, height, material, shade_shape, lamp_height):
        super().__init__(width, depth, height, material)
        self.shade_shape = shade_shape
        self.lamp_height = lamp_height

    def create_mesh(self):
        # ランプの詳細なモデル
        vertices = np.array([
            [0, 0, 0], [self.width, 0, 0], [self.width, self.depth, 0], [0, self.depth, 0],  # 底面
            [0, 0, self.height], [self.width, 0, self.height], [self.width, self.depth, self.height], [0, self.depth, self.height],  # 上面
            [self.width/2, self.depth/2, 0], [self.width/2, self.depth/2, self.lamp_height],  # ランプ支柱
            [self.width/4, self.depth/4, self.lamp_height], [3*self.width/4, self.depth/4, self.lamp_height], [3*self.width/4, 3*self.depth/4, self.lamp_height], [self.width/4, 3*self.depth/4, self.lamp_height]  # ランプシェード
        ])
        faces = np.array([
            [0, 1, 2], [0, 2, 3],  # 底面
            [4, 5, 6], [4, 6, 7],  # 上面
            [0, 1, 5], [0, 5, 4],  # 前面
            [2, 3, 7], [2, 7, 6],  # 後面
            [1, 2, 6], [1, 6, 5],  # 右側面
            [0, 3, 7], [0, 7, 4],  # 左側面
            [8, 9, 9],  # ランプ支柱
            [10, 11, 12], [10, 12, 13]  # ランプシェード
        ])
        return mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype), remove_empty_areas=False)

class Shelf(InteriorItem):
    def __init__(self, width, depth, height, material, shelf_count):
        super().__init__(width, depth, height, material)
        self.shelf_count = shelf_count

    def create_mesh(self):
        # 棚の詳細なモデル
        vertices = np.array([
            [0, 0, 0], [self.width, 0, 0], [self.width, self.depth, 0], [0, self.depth, 0],  # 底面
            [0, 0, self.height], [self.width, 0, self.height], [self.width, self.depth, self.height], [0, self.depth, self.height]  # 上面
        ])
        faces = np.array([
            [0, 1, 2], [0, 2, 3],  # 底面
            [4, 5, 6], [4, 6, 7],  # 上面
            [0, 1, 5], [0, 5, 4],  # 前面
            [2, 3, 7], [2, 7, 6],  # 後面
            [1, 2, 6], [1, 6, 5],  # 右側面
            [0, 3, 7], [0, 7, 4]  # 左側面
        ])
        
        # 棚板を追加
        for i in range(1, self.shelf_count):
            shelf_height = i * self.height / self.shelf_count
            vertices = np.vstack((vertices, [
                [0, 0, shelf_height], [self.width, 0, shelf_height], [self.width, self.depth, shelf_height], [0, self.depth, shelf_height]
            ]))
            faces = np.vstack((faces, [
                [len(vertices)-4, len(vertices)-3, len(vertices)-2], [len(vertices)-4, len(vertices)-2, len(vertices)-1]
            ]))

        return mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype), remove_empty_areas=False)

def main():
    sofa = Sofa(200, 100, 90, 'fabric', 4, True)
    table = Table(150, 75, 75, 'wood', 4, 'rectangular')
    chair = Chair(50, 50, 100, 'wood', 50, 'square')
    lamp = Lamp(30, 30, 150, 'metal', 'round', 150)
    shelf = Shelf(80, 20, 180, 'wood', 5)

    sofa.save_stl('sofa.stl')
    table.save_stl('table.stl')
    chair.save_stl('chair.stl')
    lamp.save_stl('lamp.stl')
    shelf.save_stl('shelf.stl')

if __name__ == "__main__":
    main()