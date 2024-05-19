# ## Pythonスクリプト: 椅子のSTLファイル生成

# 以下に、椅子を立体化したSTLファイルを生成するPythonスクリプトを示します。このスクリプトは、要件定義に基づいています。

# ### 必要なライブラリのインストール

# 以下のコマンドを使用して、必要なライブラリをインストールします。

# ```bash
# pip install numpy numpy-stl
# ```

# ### スクリプト

# ```python
import numpy as np
from stl import mesh

# 椅子の寸法を指定
seat_width = 50
seat_depth = 50
seat_height = 5
backrest_height = 40
leg_height = 45
leg_thickness = 5

# 座面を定義
def create_seat():
    vertices = np.array([
        [0, 0, 0],
        [seat_width, 0, 0],
        [seat_width, seat_depth, 0],
        [0, seat_depth, 0],
        [0, 0, seat_height],
        [seat_width, 0, seat_height],
        [seat_width, seat_depth, seat_height],
        [0, seat_depth, seat_height]
    ])
    
    faces = np.array([
        [0, 1, 2],
        [0, 2, 3],
        [4, 5, 6],
        [4, 6, 7],
        [0, 1, 5],
        [0, 5, 4],
        [1, 2, 6],
        [1, 6, 5],
        [2, 3, 7],
        [2, 7, 6],
        [3, 0, 4],
        [3, 4, 7]
    ])
    
    return vertices, faces

# 背もたれを定義
def create_backrest():
    vertices = np.array([
        [0, 0, seat_height],
        [seat_width, 0, seat_height],
        [seat_width, seat_height, seat_height],
        [0, seat_height, seat_height],
        [0, 0, seat_height + backrest_height],
        [seat_width, 0, seat_height + backrest_height],
        [seat_width, seat_height, seat_height + backrest_height],
        [0, seat_height, seat_height + backrest_height]
    ])
    
    faces = np.array([
        [0, 1, 2],
        [0, 2, 3],
        [4, 5, 6],
        [4, 6, 7],
        [0, 1, 5],
        [0, 5, 4],
        [1, 2, 6],
        [1, 6, 5],
        [2, 3, 7],
        [2, 7, 6],
        [3, 0, 4],
        [3, 4, 7]
    ])
    
    return vertices, faces

# 脚を定義
def create_leg(x_offset, y_offset):
    vertices = np.array([
        [x_offset, y_offset, 0],
        [x_offset + leg_thickness, y_offset, 0],
        [x_offset + leg_thickness, y_offset + leg_thickness, 0],
        [x_offset, y_offset + leg_thickness, 0],
        [x_offset, y_offset, leg_height],
        [x_offset + leg_thickness, y_offset, leg_height],
        [x_offset + leg_thickness, y_offset + leg_thickness, leg_height],
        [x_offset, y_offset + leg_thickness, leg_height]
    ])
    
    faces = np.array([
        [0, 1, 2],
        [0, 2, 3],
        [4, 5, 6],
        [4, 6, 7],
        [0, 1, 5],
        [0, 5, 4],
        [1, 2, 6],
        [1, 6, 5],
        [2, 3, 7],
        [2, 7, 6],
        [3, 0, 4],
        [3, 4, 7]
    ])
    
    return vertices, faces

# メッシュの生成
def create_mesh():
    vertices_list = []
    faces_list = []
    
    seat_vertices, seat_faces = create_seat()
    vertices_list.append(seat_vertices)
    faces_list.append(seat_faces)
    
    backrest_vertices, backrest_faces = create_backrest()
    vertices_list.append(backrest_vertices)
    faces_list.append(backrest_faces)
    
    leg_positions = [
        (0, 0),
        (seat_width - leg_thickness, 0),
        (0, seat_depth - leg_thickness),
        (seat_width - leg_thickness, seat_depth - leg_thickness)
    ]
    
    for x_offset, y_offset in leg_positions:
        leg_vertices, leg_faces = create_leg(x_offset, y_offset)
        vertices_list.append(leg_vertices)
        faces_list.append(leg_faces)
    
    vertices = np.concatenate(vertices_list)
    faces = np.concatenate([faces + i * 8 for i, faces in enumerate(faces_list)])
    
    return vertices, faces

# STLファイルの保存
def save_stl(filename):
    vertices, faces = create_mesh()
    chair_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    
    for i, face in enumerate(faces):
        for j in range(3):
            chair_mesh.vectors[i][j] = vertices[face[j], :]
    
    chair_mesh.save(filename)

# メイン関数
if __name__ == "__main__":
    try:
        save_stl("chair_model.stl")
        print("STLファイルが正常に生成されました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
# ```

# ### スクリプトの実行方法

# 1. 上記のスクリプトを`chair_model.py`という名前で保存します。
# 2. 必要なライブラリをインストールします（上記のインストールコマンドを参照）。
# 3. ターミナルまたはコマンドプロンプトで以下のコマンドを実行します。

# ```bash
# python chair_model.py
# ```

# これにより、`chair_model.stl`という名前のSTLファイルが生成されます。このファイルを3Dプリンタなどで使用することができます。