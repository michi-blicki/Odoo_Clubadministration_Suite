# -*- encoding: UTF-8 -*-

"""
    Clubmanagement Suite - Master Data and Customizing
    
    Filename: hooks.py
    
    (Un-)Installation Hooks
"""

__author__ = "Michael Blickenstorfer <michi@blicki.ch>"
__maintainer__ = "Michael Blickenstorfer <michi@blicki.ch>"
__copyright__ = "Copyright 2024, Clubmanagement Suite Project"
__license__ = "LGPL-3"

from . import models
from flectra import api, SUPERUSER_ID

import logging
_logger = logging.getLogger(__name__)

def pre_init_hook(cr):
    _logger.debug('pre_init_hook(): Nothing to be done so far prior the module installation')
    
def post_init_hook(cr, registry):
    _logger.debug('pre_init_hook(): Nothing to be done so far prior the module installation')
    
def uninstall_hook(cr, registry):
    _logger.debug('pre_init_hook(): Nothing to be done so far prior the module installation')