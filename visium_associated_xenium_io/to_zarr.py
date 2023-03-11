##
from spatialdata_io import visium
import spatialdata as sd

##
from pathlib import Path

##
def main():
    ##
    path = Path().resolve()
    # luca's workaround for pycharm
    if not str(path).endswith("xenium_io"):
        path /= "xenium_io"
        assert path.exists()
    path_read = path / "data/visium/"
    path_write = path / "data_visium.zarr"
    ##
    sdata_visium = visium(str(path_read))
    sdata_visium.write(str(path_write))
    print("done")
    ##
    print(f'view with "python -m spatialdata view data_visium.zarr"')
    print("read")
    sdata = sd.SpatialData.read(path_write)
    print(sdata)
    ##


if __name__ == "__main__":
    main()