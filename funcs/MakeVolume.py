import SimpleITK as sitk
import pyvista as pv


def GetVolume(Path: str, vocal: bool = False):
    """
    input:
    Path: path to the Folder where CT scan data is stored

    returns:
    SimpleITK Volume

    """

    reader = sitk.ImageSeriesReader()
    dicom_files = reader.GetGDCMSeriesFileNames(Path)
    if vocal:
        print("read files")
    reader.SetFileNames(dicom_files)
    if vocal:
        print("file names set")
    image = reader.Execute()
    volume_data = sitk.GetArrayFromImage(image)
    return volume_data


def MakeGrid(Volume, scale=[1.0, 1.0, 1.0], vocal=False):
    """
    input:
    Volume object
    *optional*
    Scale float:[x,y,z]


    Output:
    pyvista grid object

    """
    grid = pv.wrap(Volume)
    grid = grid.scale(scale, inplace=False)
    return grid
