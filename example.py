from funcs.MakeVolume import MakeGrid, GetVolume
from pyvista import wrap, Plotter
import numpy as np

Path = "./DELGT01-C2-15"
Volume = GetVolume(Path, vocal=True)
downsample_factor = 1
if downsample_factor > 1:
    Volume = Volume[
        ::downsample_factor,
        ::downsample_factor,
        ::downsample_factor,
    ]
    print(f"Downsampled volume by factor {downsample_factor}")


# grid = wrap(Volume)
# grid = grid.scale([5.0, 1, 1], inplace=False)

grid = MakeGrid(Volume=Volume, scale=[5.0, 1, 1])
# edges = grid.extract_feature_edges(progress_bar=True)
grid = grid.extract_values(ranges=[1e3, np.inf], include_cells=True)
# edges.plot()
plt = Plotter()
# plt.add_mesh(mesh=edges, cmap="bone")
# plt.add_volume(edges, cmap="bone")
plt.add_mesh_clip_plane(grid, normal="-y", cmap="bone")
# plt.add_mesh_clip_plane(edges, normal="-y", color="red")
plt.add_axes()
plt.show()
