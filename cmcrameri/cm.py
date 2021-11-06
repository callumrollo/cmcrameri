"""
Perceptually uniform colourmaps for geosciences

Packaging of colourmaps created by Fabio Crameri http://www.fabiocrameri.ch/colourmaps.php

Created by Callum Rollo
2020-05-06
"""
import matplotlib.pyplot as plt
import numpy as np


_cmap_names_sequential = (
    "batlow", "batlowW", "batlowK",
    "devon", "lajolla", "bamako",
    "davos", "bilbao", "nuuk",
    "oslo", "grayC", "hawaii", 
    "lapaz", "tokyo", "buda",
    "acton", "turku", "imola",
)

_cmap_names_diverging = (
    "broc", "cork", "vik",
    "lisbon", "tofino", "berlin",
    "roma", "bam", "vanimo",
)

_cmap_names_multi_sequential = (
    "oleron", "bukavu", "fes",
)

_cmap_base_names_categorical = tuple(
    name
    for name in _cmap_names_sequential
    if name not in {"batlowW", "batlowK"}
)
_cmap_names_categorical = tuple(
    f"{name}S"
    for name in _cmap_base_names_categorical
)

_cmap_base_names_cyclic = (
    "roma", "bam",
    "broc", "cork", "vik",
)
_cmap_names_cyclic = tuple(
    f"{name}O"
    for name in _cmap_base_names_cyclic
)

def _load_cmaps():
    from pathlib import Path
    from matplotlib.colors import ListedColormap

    # Prepended to cmap names when registering
    cmap_reg_prefix = "cmc."

    cmaps = {}

    def register(cmap):
        # Register in Matplotlib
        plt.cm.register_cmap(name=f"{cmap_reg_prefix}{cmap.name}", cmap=cmap)
        # Add to dict
        cmaps[cmap.name] = cmap

    # Find the colormap text files and make a list of the paths
    cmap_data_dir = Path(__file__).parent / 'cmaps'
    paths = sorted(cmap_data_dir.glob('*.txt'))
    for cmap_path in paths:
        # Name of colour map is taken from the text file name
        cmap_name = cmap_path.stem

        # Categorize
        is_categorical = cmap_name.endswith("S")
        is_cyclic = cmap_name.endswith("O")
        cmap_name_base = cmap_name if not (is_categorical or is_cyclic) else cmap_name[:-1]
        if not is_cyclic:
            is_sequential = cmap_name_base in _cmap_names_sequential
            is_diverging = cmap_name_base in _cmap_names_diverging
            is_multi_sequential = cmap_name_base in _cmap_names_multi_sequential
        else:
            is_sequential = is_diverging = is_multi_sequential = False

        # Check categorization
        assert sum(
            [is_cyclic, is_sequential, is_diverging, is_multi_sequential]
        ) == 1, f"{cmap_name} not categorized properly"
        assert not is_categorical or cmap_name_base in _cmap_base_names_categorical
        assert not is_cyclic or cmap_name_base in _cmap_base_names_cyclic, cmap_name

        # Load data
        data = np.loadtxt(cmap_path)
        N = data.shape[0]
        N0 = 256 if not is_categorical else 100
        assert N == N0, f"N should be {N0} but is {N}"

        # Create and register colormap
        cmap = ListedColormap(colors=data, name=cmap_name)
        register(cmap)

        # For non-categorical, also create and register reverse version
        if not is_categorical:
            register(cmap.reversed())

    return paths, cmaps


paths, cmaps = _load_cmaps()

# Add all cmaps to the `cmcrameri.cm` namespace
locals().update(cmaps)


def show_cmaps():
    """
    A rough function for a quick plot of the colourmaps.
    Nowhere near as pretty as the original,
    see https://www.fabiocrameri.ch/colourmaps/
    """
    from itertools import chain

    x = np.linspace(0, 100, 100)[np.newaxis, :]

    n_all = len(cmaps)
    n_seq = len(_cmap_names_sequential)
    n_div = len(_cmap_names_diverging)
    n_mseq = len(_cmap_names_multi_sequential)
    n_cyc = len(_cmap_names_cyclic)
    n_cat = len(_cmap_base_names_categorical)

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
            _cmap_names_sequential, _cmap_names_diverging,
            _cmap_names_multi_sequential, _cmap_names_cyclic,
        ))
    ):
        cmap = globals()[cmap_name]
        ax.pcolor(x, cmap=cmap)
        ax.text(5, -0.3, cmap.name, fontsize=26)
