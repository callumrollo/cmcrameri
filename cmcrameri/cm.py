"""
Perceptually uniform colourmaps for geosciences

Packaging of colourmaps created by Fabio Crameri http://www.fabiocrameri.ch/colourmaps.php

Created by Callum Rollo
2020-05-06
"""

import numpy as np
from pathlib import Path
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import os
# Find the colormap text files and make a list of the paths
text_file_folder = os.path.join(os.path.dirname(__file__), 'cmaps')
paths = list(Path(text_file_folder).glob('*.txt'))
crameri_cmaps = dict()
crameri_cmaps_r = dict()
crameri_cmaps_s = dict()
for cmap_path in paths:
    # Name of colour map taken from text file
    cmap_name = os.path.split(cmap_path)[1][:-4]
    cm_data = np.loadtxt(str(cmap_path))
    # Make a linear segmented colour map
    if cmap_name[-1] == 'S':
        crameri_cmaps_s[cmap_name] = LinearSegmentedColormap.from_list(cmap_name, cm_data)
        plt.cm.register_cmap(name='cmc.' + cmap_name, cmap=crameri_cmaps_s[cmap_name])
        continue
    crameri_cmaps[cmap_name] = LinearSegmentedColormap.from_list(cmap_name, cm_data)
    plt.cm.register_cmap(name='cmc.' + cmap_name, cmap=crameri_cmaps[cmap_name])
    # reverse the colour map and add this to the dictionary crameri_cmaps_r, mpt fpr categorical maps
    crameri_cmaps_r[cmap_name + '_r'] = LinearSegmentedColormap.from_list(cmap_name + '_r', cm_data[::-1, :])
    plt.cm.register_cmap(name='cmc.' + cmap_name + '_r', cmap=crameri_cmaps_r[cmap_name + '_r'])


def show_cmaps():
    """
    A rough function for a quick plot of the colourmaps. Nowhere near as pretty as the original
    see http://www.fabiocrameri.ch/colourmaps.php
    :return:
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
