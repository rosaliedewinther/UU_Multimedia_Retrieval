from numpy.core.fromnumeric import mean
from asyncio import Handle
from gui import HandleGUIEvents, initGUI
import mesh_io
import renderer
import filter_io
import mesh_normalize
import pandas as pd


if __name__ == "__main__":
    meshes = mesh_io.get_all_obj_files("./assets/")  # sets filename_field
    meshes = mesh_io.get_all_meshes(meshes)  # sets trimesh_model field
    meshes = filter_io.output_filter(meshes)  # determine details
    meshes = mesh_normalize.remesh_all_meshes(meshes)  # normalize mesh

    renderer.render_meshes(meshes[:9])

    window = initGUI()

    while True:                             # The Event Loop
        if not HandleGUIEvents(window):
            break

    window.close()
