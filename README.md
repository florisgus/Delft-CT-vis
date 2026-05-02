# Delft-CT-vis

A simple tool to visualise and add some usefull tools for CT scans

# Use

start by cloning this repository by doing:

```bash
git clone git@github.com:florisgus/Delft-CT-vis.git
```

After which change the folder pointed to in example.py to the folder containing your CT-scan.

then run this script in an enviroment where numpy tqdm pyvista and SimpleITK are installed.

watchout with how big the scan is this tend to require a lot of memory, however it is possible to reduce the required memory by downsampeling the grid/volume using the code in example.py, this script automatically filters out air (for my test case)
