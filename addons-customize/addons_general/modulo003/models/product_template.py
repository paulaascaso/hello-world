# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    blue = fields.Char(readonly=True)


    @api.model
    def create(self, vals):

        if vals['sale_ok'] == True and vals['purchase_ok'] == True :
            vals['blue'] = 'Puede ser vendido y comprado'

        elif vals['sale_ok'] == True :
            vals['blue'] = 'Puede ser vendido'

        elif vals['purchase_ok'] == True :
            vals['blue'] = 'Puede ser comprado'

        return super().create(vals)
