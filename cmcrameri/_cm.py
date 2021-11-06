"""
Perceptually uniform colourmaps for geosciences

Packaging of colourmaps created by Fabio Crameri http://www.fabiocrameri.ch/colourmaps.php

Created by Callum Rollo
2020-05-06
"""
from pathlib import Path
from types import SimpleNamespace

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap


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

categorical_cmap_base_names = tuple(
    name
    for name in sequential_cmap_names
    if name not in {"batlowW", "batlowK"}
)
categorical_cmap_names = tuple(
    f"{name}S"
    for name in categorical_cmap_base_names
)

cyclic_cmap_base_names = (
    "roma", "bam",
    "broc", "cork", "vik",
)
cyclic_cmap_names = tuple(
    f"{name}O"
    for name in cyclic_cmap_base_names
)

cm = SimpleNamespace()  # or NamedTuple?

# Prepended to cmap names when registering
cmap_reg_prefix = "cmc."


# Find the colormap text files and make a list of the paths
cmap_dir = Path(__file__).parent / 'cmaps'
paths = sorted(cmap_dir.glob('*.txt'))
for cmap_path in paths:
    # Name of colour map is taken from the text file name
    cmap_name = cmap_path.stem

    # Categorize
    is_categorical = cmap_name.endswith("S")
    is_cyclic = cmap_name.endswith("O")
    cmap_name_base = cmap_name if not (is_categorical or is_cyclic) else cmap_name[:-1]
    if not is_cyclic:
        is_sequential = cmap_name_base in sequential_cmap_names
        is_diverging = cmap_name_base in diverging_cmap_names
        is_multi_sequential = cmap_name_base in multi_sequential_cmap_names
    else:
        is_sequential = is_diverging = is_multi_sequential = False

    # Check categorization
    assert sum(
        [is_cyclic, is_sequential, is_diverging, is_multi_sequential]
    ) == 1, f"{cmap_name} not categorized properly"
    assert not is_categorical or cmap_name_base in categorical_cmap_base_names
    assert not is_cyclic or cmap_name_base in cyclic_cmap_base_names, cmap_name

    # Load data
    data = np.loadtxt(cmap_path)
    N = data.shape[0]
    N0 = 256 if not is_categorical else 100
    assert N == N0, f"N should be {N0} but is {N}"

    # Create and register colormap
    cmap = ListedColormap(colors=data, name=cmap_name)
    plt.cm.register_cmap(name=f"{cmap_reg_prefix}{cmap.name}", cmap=cmap)
    setattr(cm, cmap.name, cmap)

    # For non-categorical, also create and register reverse version
    if not is_categorical:
        cmap = cmap.reversed()
        plt.cm.register_cmap(name=f"{cmap_reg_prefix}{cmap.name}", cmap=cmap)
        setattr(cm, cmap.name, cmap)


def show_cmaps():
    """
    A rough function for a quick plot of the colourmaps.
    Nowhere near as pretty as the original,
    see https://www.fabiocrameri.ch/colourmaps/
    """
    from itertools import chain

    x = np.linspace(0, 100, 100)[np.newaxis, :]

    # all_names = list(vars(cm))
    n_seq = len(sequential_cmap_names)
    n_div = len(diverging_cmap_names)
    n_mseq = len(multi_sequential_cmap_names)
    n_cyc = len(cyclic_cmap_names)
    # n_cat = len(categorical_cmap_base_names)

    ncols = 7
    nrows = int(np.ceil((n_seq + n_div + n_mseq + n_cyc) / ncols))

    fig, axs = plt.subplots(nrows, ncols, figsize=(22, 10))
    fig.subplots_adjust(hspace=.8, wspace=.08)
    fig.set_tight_layout(False)

    for ax in axs.flat:
        ax.axis('off')

    for ax, cmap_name in zip(
        axs.flat, 
        sorted(chain(
            sequential_cmap_names, diverging_cmap_names, 
            multi_sequential_cmap_names, cyclic_cmap_names,
        ))
    ):
        cmap = getattr(cm, cmap_name)
        ax.pcolor(x, cmap=cmap)
        ax.text(5, -0.3, cmap.name, fontsize=26)
