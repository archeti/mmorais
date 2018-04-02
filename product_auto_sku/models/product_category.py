# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class ProductCategory(models.Model):
    _inherit = "product.category"

    sequence_id = fields.Many2one('ir.sequence', string="Sequence")
