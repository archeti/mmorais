# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class ProductAttributeValue(models.Model):
    _inherit = "product.attribute.value"

    code = fields.Char(string="Code")
