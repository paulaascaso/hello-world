# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    profit = fields.Float(string='Beneficio',compute='_compute_profit',store=True,help='Beneficio calculado a partir del Precio de venta y el Coste (calculado).')

    @api.depends('list_price','standard_price')
    def _compute_profit(self):
        for record in self:
            record.profit = record.list_price - record.standard_price
