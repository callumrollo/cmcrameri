"""
cmcrameri is a package of perceptually uniform colourmaps for the geosciences
This is mererly a wrapper for previosuly created colour maps. All credit to Fabio Crameri
http://www.fabiocrameri.ch/colourmaps.php
See README.md for an overview and instructions
"""

from __future__ import absolute_import
from . import cm


__authors__ = ['Callum Rollo <c.rollo@outlook.com>']

try:
    from ._version import __version__
except ImportError:
    __version__ = "unknown"

__scm_version__ = "7.0"
