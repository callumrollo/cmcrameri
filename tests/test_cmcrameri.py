"""
Test that the program a) finds the text files and b) creates colourmaps
"""

import matplotlib
from pathlib import Path
import sys
library_dir = Path(__file__).parent.parent.absolute()
print(library_dir)
sys.path.append(str(library_dir))
from cmcrameri import cm

def test_find_files():
    assert len(cm.paths) > 0
    print(f"Number of text files: {len(cm.paths)}")


def test_cmap_import():
    # Loop through all methods in cmcrameri
    no_cmaps = 0
    cmap_names = []
    for name, cmap in vars(cm).items():
        # See if it is a colormap.
        if isinstance(cmap, matplotlib.colors.LinearSegmentedColormap):
            no_cmaps += 1
            cmap_names.append(name)
    # Should be twice as many colour maps as files (original and reversed versions)
    assert no_cmaps == 2*len(cm.paths)
    print(f"Number of colormaps: {no_cmaps}\n"
          f"Names of colourmpas: {cmap_names}")

test_find_files()
test_cmap_import()