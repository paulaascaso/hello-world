# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderReportXlsx(models.AbstractModel):

    _name = 'report.modulo011.report_sale_order_card'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, sales):
        for obj in sales:
            report_name = obj.name
            # One sheet by sale
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({'bold': True})
            sheet.write(0, 0, 'PRESUPUESTO DE VENTA ' +  obj.name, bold)

            # Some data we want to write to the worksheet.
            field_value = (
                ['Cliente', obj.partner_id.name],
                ['Fecha de presupuesto', obj.date_order],
                ['Total', str(obj.amount_total) + ' €']
            )
            # Start from the second cell.
            row = 1
            col = 0
            # Iterate over the data and write it out row by row.
            for item, value in (field_value):
                sheet.write(row, col, item, bold)
                sheet.write(row, col + 1, value)
                row += 1

            date_format = workbook.add_format({'num_format': 'dd/mm/yyyy'})
            sheet.write(2, 1, obj.date_order, date_format)




#
