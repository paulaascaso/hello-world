# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    state = fields.Char(string='Estado', size=100, readonly=True)


    def action_state_lead(self):

        for record in self:
            if record.state is False:
                record.state = "Va bien"
            elif record.state == "Va bien":
                record.state = "Necesita refuerzo"
            elif record.state == "Necesita refuerzo":
                record.state = "Va bien"

        return True
