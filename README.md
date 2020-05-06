# cmcrameri

This is a basic wrapper around Fabio Crameri's perceptually uniform colour maps

http://www.fabiocrameri.ch/colourmaps.php

Current version is based on Scientific Colourmaps Version 6.0.4 (06.01.2020)

**Work in progress** Not ready for public use yet! I haven't made a package before. The eventual aim is for this repo to serve PyPI and anaconda

To use these colourmaps, clone/download the repo, add the folder to your path then:
```python
from cmcrameri import cm
import matplotlib.pyplot as plt
import numpy as mp
plt.pcolor(np.random.rand(10,10), cmap=cm.batlow) # or any of the other colourmaps made by Fabio Crameri
```
