# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderReport(models.AbstractModel):

    _name = 'report.modulo010.report_sale_order_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('modulo010.report_sale_order_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['sale.order'],
            'docs': self.env['sale.order'].browse(docids)
        }
