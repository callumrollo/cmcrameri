"""
Perceptually uniform colourmaps for geosciences

Packaging of colourmaps created by Fabio Crameri http://www.fabiocrameri.ch/colourmaps.php

Created by Callum Rollo
2020-05-06
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


sequential_cmap_names = (
    "batlow", "batlowW", "batlowK",
    "devon", "lajolla", "bamako",
    "davos", "bilbao", "nuuk",
    "oslo", "grayC", "hawaii", 
    "lapaz", "tokyo", "buda",
    "acton", "turku", "imola",
)

diverging_cmap_names = (
    "broc", "cork", "vik",
    "lisbon", "tofino", "berlin",
    "roma", "bam", "vanimo",
)

multi_sequential_cmap_names = (
    "oleron", "bukavu", "fes",
)


# Find the colormap text files and make a list of the paths
text_file_folder = Path(__file__).parent / 'cmaps'
paths = sorted(text_file_folder.glob('*.txt'))
crameri_cmaps = dict()
crameri_cmaps_r = dict()
crameri_cmaps_s = dict()
for cmap_path in paths:
    # Name of colour map is taken from the text file name
    cmap_name = cmap_path.stem
    is_categorical = cmap_name.endswith("S")

    # Categorize
    cmap_name_base = cmap_name if not is_categorical else cmap_name[:-1]
    is_cyclic = cmap_name_base.endswith("O")
    is_sequential = cmap_name_base in sequential_cmap_names
    is_diverging = cmap_name_base in diverging_cmap_names
    is_multi_sequential = cmap_name_base in multi_sequential_cmap_names
    assert sum(
        [is_cyclic, is_sequential, is_diverging, is_multi_sequential]
    ) == 1, f"{cmap_name} not categorized properly"

    # Load data
    data = np.loadtxt(cmap_path)
    N = data.shape[0]
    N0 = 256 if not is_categorical else 100
    assert N == N0, f"N should be {N0} but is {N}"

    # Make a linear segmented colour map
    if is_categorical:
        crameri_cmaps_s[cmap_name] = LinearSegmentedColormap.from_list(cmap_name, data)
        plt.cm.register_cmap(name='cmc.' + cmap_name, cmap=crameri_cmaps_s[cmap_name])
        continue
    crameri_cmaps[cmap_name] = LinearSegmentedColormap.from_list(cmap_name, data)
    plt.cm.register_cmap(name='cmc.' + cmap_name, cmap=crameri_cmaps[cmap_name])
    # reverse the colour map and add this to the dictionary crameri_cmaps_r, mpt fpr categorical maps
    crameri_cmaps_r[cmap_name + '_r'] = LinearSegmentedColormap.from_list(cmap_name + '_r', data[::-1, :])
    plt.cm.register_cmap(name='cmc.' + cmap_name + '_r', cmap=crameri_cmaps_r[cmap_name + '_r'])


def show_cmaps():
    """
    A rough function for a quick plot of the colourmaps. Nowhere near as pretty as the original
    see http://www.fabiocrameri.ch/colourmaps.php
    """
    x = np.linspace(0, 100, 100)[None, :]
    fig, axs = plt.subplots(int(np.ceil(len(crameri_cmaps) / 7)), 7, figsize=(22, 10))
    fig.subplots_adjust(hspace=.8, wspace=.08)
    axs = axs.ravel()
    for ax in axs:
        ax.axis('off')
    for c, cmap_selected in enumerate(sorted(crameri_cmaps.keys())):
        colourmap = crameri_cmaps[cmap_selected]
        axs[c].pcolor(x, cmap=colourmap)
        axs[c].text(5, -0.3, cmap_selected, fontsize=26)


# So colourmaps can be called in other programs
locals().update(crameri_cmaps)
locals().update(crameri_cmaps_r)
locals().update(crameri_cmaps_s)
