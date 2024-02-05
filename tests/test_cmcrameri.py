"""
Test that the program a) finds the text files and b) creates colormaps
"""

import sys
from pathlib import Path

import numpy as np
from matplotlib.colors import Colormap
from matplotlib.pyplot import get_cmap

library_dir = Path(__file__).parent.parent.absolute()
sys.path.append(str(library_dir))
from cmcrameri import cm


def test_find_files():
    assert len(cm.paths) > 0


def test_cmap_import():
    # Loop through all methods in cmcrameri
    no_cmaps = 0
    cmap_names = []
    for name, cmap in vars(cm).items():
        increment = 1
        # See if it is a colormap.
        if isinstance(cmap, Colormap):
            if name[-1] != "S":
                increment = 0.5
            no_cmaps += increment
            cmap_names.append(name)
    # Should be as many colormaps as files plus reversed for non categorical ones
    assert int(no_cmaps) == len(cm.paths)


def test_get_cmap():
    for name, cmap in vars(cm).items():
        # See if it is a colormap.
        if isinstance(cmap, Colormap):
            # if cmap hasn't been correctly registered as
            # cmc.name, it will raise a ValueError
            alt_cmap = get_cmap("cmc." + name)
            # alt_cmap returned by get_cmap should be the same as cmap
            assert (np.array(cmap.colors) == np.array(alt_cmap.colors)).all()


if __name__ == "__main__":
    test_find_files()
    test_cmap_import()
    test_get_cmap()
