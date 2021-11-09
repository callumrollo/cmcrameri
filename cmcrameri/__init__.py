"""
cmcrameri is a package of perceptually uniform colormaps for the geosciences.
This is merely a wrapper for previously created colormaps,
all credit to Fabio Crameri
https://www.fabiocrameri.ch/colourmaps/

See README.md for an overview and instructions.
"""
from __future__ import absolute_import

from . import cm
from .cm import show_cmaps


__all__ = (
    "cm",
    "show_cmaps",
)


__authors__ = ['Callum Rollo <c.rollo@outlook.com>']

try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"

__scm_version__ = "7.0"
