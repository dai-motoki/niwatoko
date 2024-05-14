import numpy as np
from stl import mesh
import argparse

# インテリアアイテムの基本クラス
class InteriorItem:
    def __init__(self, width, depth, height, material):
        self.width = width
        self.depth = depth
        self.height = height
        self.material = material

    def modeling(self):
        raise NotImplementedError("サブクラスで実装してください！")

# ソファクラス
class Sofa(InteriorItem):
    def __init__(self, width, depth, height, material, cushion_count, armrest):
        super().__init__(width, depth, height, material)
        self.cushion_count = cushion_count
        self.armrest = armrest

    def modeling(self):
        # シンプルな長方形のソファモデル
        vertices = np.array([
            [0, 0, 0],
            [self.width, 0, 0],
            [self.width, self.depth, 0],
            [0, self.depth, 0],
            [0, 0, self.height],
            [self.width, 0, self.height],
            [self.width, self.depth, self.height],
            [0, self.depth, self.height]
        ])

        faces = np.array([
            [0, 1, 2],
            [0, 2, 3],
            [4, 5, 6],
            [4, 6, 7],
            [0, 1, 5],
            [0, 5, 4],
            [2, 3, 7],
            [2, 7, 6],
            [1, 2, 6],
            [1, 6, 5],
            [0, 3, 7],
            [0, 7, 4]
        ])

        return vertices, faces

# テーブルクラス
class Table(InteriorItem):
    def __init__(self, width, depth, height, material, leg_count, tabletop_shape):
        super().__init__(width, depth, height, material)
        self.leg_count = leg_count
        self.tabletop_shape = tabletop_shape

    def modeling(self):
        # シンプルな長方形のテーブルモデル
        vertices = np.array([
            [0, 0, 0],
            [self.width, 0, 0],
            [self.width, self.depth, 0],
            [0, self.depth, 0],
            [0, 0, self.height],
            [self.width, 0, self.height],
            [self.width, self.depth, self.height],
            [0, self.depth, self.height]
        ])

        faces = np.array([
            [0, 1, 2],
            [0, 2, 3],
            [4, 5, 6],
            [4, 6, 7],
            [0, 1, 5],
            [0, 5, 4],
            [2, 3, 7],
            [2, 7, 6],
            [1, 2, 6],
            [1, 6, 5],
            [0, 3, 7],
            [0, 7, 4]
        ])

        return vertices, faces

# チェアクラス
class Chair(InteriorItem):
    def __init__(self, width, depth, height, material, backrest_height, seat_shape):
        super().__init__(width, depth, height, material)
        self.backrest_height = backrest_height
        self.seat_shape = seat_shape

    def modeling(self):
        # シンプルな長方形のチェアモデル
        vertices = np.array([
            [0, 0, 0],
            [self.width, 0, 0],
            [self.width, self.depth, 0],
            [0, self.depth, 0],
            [0, 0, self.height],
            [self.width, 0, self.height],
            [self.width, self.depth, self.height],
            [0, self.depth, self.height]
        ])

        faces = np.array([
            [0, 1, 2],
            [0, 2, 3],
            [4, 5, 6],
            [4, 6, 7],
            [0, 1, 5],
            [0, 5, 4],
            [2, 3, 7],
            [2, 7, 6],
            [1, 2, 6],
            [1, 6, 5],
            [0, 3, 7],
            [0, 7, 4]
        ])

        return vertices, faces

# ランプクラス
class Lamp(InteriorItem):
    def __init__(self, width, depth, height, material, shade_shape):
        super().__init__(width, depth, height, material)
        self.shade_shape = shade_shape

    def modeling(self):
        # シンプルな長方形のランプモデル
        vertices = np.array([
            [0, 0, 0],
            [self.width, 0, 0],
            [self.width, self.depth, 0],
            [0, self.depth, 0],
            [0, 0, self.height],
            [self.width, 0, self.height],
            [self.width, self.depth, self.height],
            [0, self.depth, self.height]
        ])

        faces = np.array([
            [0, 1, 2],
            [0, 2, 3],
            [4, 5, 6],
            [4, 6, 7],
            [0, 1, 5],
            [0, 5, 4],
            [2, 3, 7],
            [2, 7, 6],
            [1, 2, 6],
            [1, 6, 5],
            [0, 3, 7],
            [0, 7, 4]
        ])

        return vertices, faces

# シェルフクラス
class Shelf(InteriorItem):
    def __init__(self, width, depth, height, material, shelf_count):
        super().__init__(width, depth, height, material)
        self.shelf_count = shelf_count

    def modeling(self):
        # シンプルな長方形のシェルフモデル
        vertices = np.array([
            [0, 0, 0],
            [self.width, 0, 0],
            [self.width, self.depth, 0],
            [0, self.depth, 0],
            [0, 0, self.height],
            [self.width, 0, self.height],
            [self.width, self.depth, self.height],
            [0, self.depth, self.height]
        ])

        faces = np.array([
            [0, 1, 2],
            [0, 2, 3],
            [4, 5, 6],
            [4, 6, 7],
            [0, 1, 5],
            [0, 5, 4],
            [2, 3, 7],
            [2, 7, 6],
            [1, 2, 6],
            [1, 6, 5],
            [0, 3, 7],
            [0, 7, 4]
        ])

        return vertices, faces

# STLファイルを保存する関数
def save_stl(vertices, faces, filename, binary=True):
    data = np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype)
    for i, f in enumerate(faces):
        for j in range(3):
            data['vectors'][i][j] = vertices[f[j],:]

    m = mesh.Mesh(data)
    if binary:
        m.save(filename, mode=mesh.Mode.BINARY)
    else:
        m.save(filename, mode=mesh.Mode.ASCII)
    print(f"STLファイル '{filename}' を保存しました。")

# メイン関数
def main():
    parser = argparse.ArgumentParser(description='インテリアアイテムのSTLファイルを生成します。')
    parser.add_argument('--item', required=True, choices=['sofa', 'table', 'chair', 'lamp', 'shelf'], help='インテリアアイテムの種類')
    parser.add_argument('--width', type=float, required=True, help='アイテムの幅')
    parser.add_argument('--depth', type=float, required=True, help='アイテムの奥行き')
    parser.add_argument('--height', type=float, required=True, help='アイテムの高さ')
    parser.add_argument('--material', type=str, required=True, help='アイテムの素材')
    parser.add_argument('--filename', type=str, required=True, help='出力するSTLファイル名')
    parser.add_argument('--binary', action='store_true', help='STLファイルをバイナリ形式で保存')

    # 特定のアイテムに対する追加引数
    parser.add_argument('--cushion_count', type=int, help='ソファのクッションの数')
    parser.add_argument('--armrest', type=bool, help='ソファのアームレスト')
    parser.add_argument('--leg_count', type=int, help='テーブルの脚の数')
    parser.add_argument('--tabletop_shape', type=str, help='テーブルの天板の形状')
    parser.add_argument('--backrest_height', type=float, help='チェアの背もたれの高さ')
    parser.add_argument('--seat_shape', type=str, help='チェアの座面の形状')
    parser.add_argument('--shade_shape', type=str, help='ランプのシェードの形状')
    parser.add_argument('--shelf_count', type=int, help='シェルフの棚の数')

    args = parser.parse_args()

    if args.item == 'sofa':
        if args.cushion_count is None or args.armrest is None:
            print("ソファのクッションの数とアームレストの有無を指定してください。")
            return
        sofa = Sofa(args.width, args.depth, args.height, args.material, args.cushion_count, args.armrest)
        vertices, faces = sofa.modeling()
        save_stl(vertices, faces, args.filename, args.binary)

if __name__ == "__main__":
    main()
