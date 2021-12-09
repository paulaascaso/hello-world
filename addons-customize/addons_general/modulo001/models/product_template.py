# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    family = fields.Selection([('A', 'Alimentación'), ('B', 'Bebidas'), ('C', 'Menaje y limpieza')], string='Familia', required=True)
    subfamily = fields.Char(string='Subfamilia', size=150)
