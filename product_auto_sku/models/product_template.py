# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning


class ProductTemplate(models.Model):
    _inherit = "product.template"

    sequence_code = fields.Char(string='Sequence Code')

    @api.model
    def create(self, values):

        if (
            'sequence_code' not in values or
            not values.get('sequence_code', '') and
            'categ_id' in values
        ):
            values['sequence_code'] = self.next_sequence_code(
                values['categ_id'])

        res = super(ProductTemplate, self).create(values)

        return res

    @api.model
    def next_sequence_code(self, categ_id):
        cat_obj = self.env['product.category']
        category = cat_obj.browse(categ_id)
        sequence = category.sequence_id

        if not sequence:
            raise Warning(
                _('The Internal Category must have a sequence defined')
            )

        return sequence.next_by_id()

    def regenerate_default_code(self):
        self.sequence_code = self.next_sequence_code(self.categ_id.id)
        self.product_variant_ids.refresh_sku()
