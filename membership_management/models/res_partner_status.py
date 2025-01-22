# -*- coding: utf-8 -*-

"""
    Clubmanagement Suite - Master Data and Customizing
    
    Filename: __init__.py
"""

__author__ = "Michael Blickenstorfer <michi@blicki.ch>"
__maintainer__ = "Michael Blickenstorfer <michi@blicki.ch>"
__copyright__ = "Copyright 2024, Clubmanagement Suite Project"
__license__ = "LGPL-3"

from odoo import models, fields, api
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)

class ResPartnerStatus(models.Model):
    _name = 'res.partner.status'
    _description = 'Members will have more than just active and not-active status'
    
    name = fields.Char(string='Name', required=True, readonly=False, index=False, copy=False, store=True)
    sequence=fields.Integer(string='Sequence', required=True, readonly=False, index=False, copy=False, store=True)
    description = fields.Text(string='Description', required=False, readonly=False, index=False, copy=False, store=True)
    color=fields.Char(string='Color', required=False, readonly=False, index=False, copy=False, store=True)
    
    @api.onchange('sequence')
    def _onchange_sequence(self):
        if self.search_count([('sequence', '=', self.sequence)]) > 0:
            raise ValidationError(_("Sequence needs to be unique."))