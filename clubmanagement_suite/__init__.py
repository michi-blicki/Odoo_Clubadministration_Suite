# -*- coding: utf-8 -*-

"""
    Clubmanagement Suite - Master Data and Customizing
    
    Filename: __init__.py
"""

__author__ = "Michael Blickenstorfer <michi@blicki.ch>"
__maintainer__ = "Michael Blickenstorfer <michi@blicki.ch>"
__copyright__ = "Copyright 2024, Clubmanagement Suite Project"
__license__ = "LGPL-3"

#
# Import Python-based subfolders
from . import controllers
from . import models

#
# Import (Un-)Installation Hooks
from .hooks import pre_init_hook
from .hooks import post_init_hook
from .hooks import uninstall_hook