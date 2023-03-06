import open3d
from pytorch3d.io import load_ply

mesh_file = "cow.ply"
mesh = open3d.io.read_triangle_mesh(mesh_file)
open3d.visualization.draw_geometries(
    [mesh],
    mesh_show_wireframe=True,
    mesh_show_back_face=True)

vertices, faces = load_ply(mesh_file)