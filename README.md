![Python package](https://github.com/callumrollo/cmcrameri/workflows/Python%20package/badge.svg)

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)]()
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)]()
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)]()
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)]()

[![Downloads](https://pepy.tech/badge/cmcrameri)](https://pepy.tech/project/cmcrameri)     (PyPI)

[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/cmcrameri.svg)](https://anaconda.org/conda-forge/cmcrameri) (conda-forge)

# cmcrameri

This is a Python wrapper around Fabio Crameri's perceptually uniform colour maps.

<https://www.fabiocrameri.ch/colourmaps/>

All credit for creating the colour maps to Fabio.
Any errors in the Python implementation of colour maps are my own.

This version is based on *Scientific colour maps* [version 7.0](https://zenodo.org/record/4491293) (02.02.2021).

### Install

With `pip`:
```
pip install cmcrameri
```

With `conda`:
```
conda install -c conda-forge cmcrameri
```

### Usage example

```python
import cmcrameri.cm as cmc
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100, 100)[np.newaxis, :]  

plt.imshow(x, aspect='auto', cmap=cmc.batlow)
plt.axis('off')
plt.show()
```
Alternatively, the registered name string can be used.
```python
import cmrameri  # required in order to register the colour maps
...
plt.imshow(x, aspect='auto', cmap='cmc.batlow')
```

### Extra instructions

You can access all the core colourmaps from Fabio Crameri's list by `cmcrameri.cm.<colormapname>`.

You can use tab autocompletion on `cm` if your editor supports it.

For a reversed colourmap, append `_r` to the colourmap name.

Categorical colormaps have the suffix `S`.

For an image of all the available colourmaps without leaving the comfort of your Python session:
```python
from cmcrameri import show_cmaps

show_cmaps()
```
![Figure demonstrating colour maps](cmcrameri/colormaps.png)

To make the underlying RGB values available, the original text files are shipped as part of the package.
Find them on your system with:
```python
from cmcrameri import paths

paths
```

### License
This work is licensed under an [MIT license](https://mit-license.org/).
