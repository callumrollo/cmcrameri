![Python package](https://github.com/callumrollo/cmcrameri/workflows/Python%20package/badge.svg)
# cmcrameri

This is a basic Python wrapper around Fabio Crameri's perceptually uniform colour maps

http://www.fabiocrameri.ch/colourmaps.php

All credit for creating the colourmaps to Fabio. Any errors in the Python implementation of said colourmaps are my own.

Current version is based on Scientific Colourmaps Version 6.0.4 (06.01.2020)

**Work in progress** Not ready for public use yet! I haven't shipped a package before. The eventual aim is for this repo to serve PyPi and conda

### Install
`pip install cmcrameri`

### Basic use example

```python
from cmcrameri import cm
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 100, 100)[None, :]  
plt.imshow(x, aspect='auto', cmap=cm.batlow) # or any of the other colourmaps made by Fabio Crameri
plt.axis('off')
plt.show()
```
### Extra instructions
You can access all the core colourmaps from Fabio Crameri's list by `cm.<colormapname>`

You can also use tab autocompletion on `cm` if your editor supports it

For a reversed colourmap, append `_r` to the colourmap name

For a sample of all the available colourmaps without leaving the comfort of your Python session
```python
from cmcrameri.cm import show_cmaps 
show_cmaps()
```
