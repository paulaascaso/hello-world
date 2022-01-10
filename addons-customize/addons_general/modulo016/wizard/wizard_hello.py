# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SayHelloWizard(models.TransientModel):
    _name = 'product.template.hello.wizard'
    _description = 'Say Hello'

    def hello_wizard(self):
        return True
