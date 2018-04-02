# -*- coding: utf-8 -*-
from openerp import models, fields, api, _


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.multi
    def _compute_default_code(self):
        self.ensure_one()

        attributes = [
            attr.code
            for attr in self.attribute_value_ids
            if attr.code
        ]

        prefix = self.product_tmpl_id.sequence_code

        if prefix and len(prefix) > 0:
            attributes.insert(0, prefix)

        self.default_code = '-'.join(attributes)

    @api.model
    def create(self, values):
        res = super(ProductProduct, self).create(values)

        if 'default_code' not in values:
            # We cannot edit values prior to creation because some fields
            # aren't yet populated... For example, default values
            res._compute_default_code()

        return res

    @api.multi
    def refresh_sku(self):
        for obj in self:
            obj._compute_default_code()
