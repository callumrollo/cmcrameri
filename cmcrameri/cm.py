"""
Packaging of colormaps created by Fabio Crameri
https://www.fabiocrameri.ch/colourmaps/

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

    # Load data and generate Colormap objects
    for cmap_path in paths:
        # Name of colormap is taken from the text file name
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
        assert not is_categorical or cmap_name_base in _cmap_base_names_categorical, cmap_name
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


def show_cmaps(*, ncols=6, figwidth=8):
    """
    For the original, see
    https://www.fabiocrameri.ch/colourmaps/
    """
    import math

    x = np.linspace(0, 1, 256)[np.newaxis, :]

    groups = (
        ("Sequential", _cmap_names_sequential),
        ("Diverging", _cmap_names_diverging),
        ("Multi-sequential", _cmap_names_multi_sequential),
        ("Cyclic", _cmap_names_cyclic),
    )

    nrows = 1
    istarts = []
    for group_name, group in groups:
        n = len(group)
        istarts.append(nrows)
        nrows += math.ceil(n / ncols)
        if group_name != groups[-1][0]:
            nrows += 1  # group spacer row

    nrows_titles = len(groups)
    nrows_cmaps = nrows - nrows_titles

    hrel_spacer = 0.3  # spacer height relative cmap row height
    hratios = [1 for _ in range(nrows)]
    for i in istarts:
        hratios[i-1] = hrel_spacer  # group spacer row

    hrow = 0.4  # size of cmap row
    hspace = 0.7  # hspace, relative to `hrow`
    hbottom = 0.2
    htop = 0.05
    figheight = (
        hbottom + 
        htop + 
        hrow*nrows_cmaps + 
        hrow*hrel_spacer*nrows_titles + 
        hrow*hspace*(nrows - 1)
    )

    fig, axs = plt.subplots(nrows, ncols,
        figsize=(figwidth, figheight),
        gridspec_kw=dict(
            left=0.01, right=0.99,
            top=1 - htop/figheight,
            bottom=hbottom/figheight,
            hspace=hspace/np.mean(hratios),
            wspace=0.08,
            height_ratios=hratios
        )
    )
    fig.set_tight_layout(False)

    for ax in axs.flat:
        ax.set_axis_off()

    for istart, (group_name, group) in zip(istarts, groups):

        # Group label
        ax0 = axs[istart, 0]
        ax0.text(0.01, 1.02, group_name, size=24, c="0.4", style="italic", 
            va="bottom", ha="left", transform=ax0.transAxes)

        for ax, cmap_name in zip(axs[istart:].flat, group):

            cmap = cmaps[cmap_name]
            ax.imshow(x, cmap=cmap, aspect="auto")
            ax.text(0.01 * ncols/6, -0.03, cmap_name, size=14, color="0.2",
                va="top", transform=ax.transAxes)


if __name__ == "__main__":
    show_cmaps()
    plt.savefig("colormaps.png", dpi=200)
