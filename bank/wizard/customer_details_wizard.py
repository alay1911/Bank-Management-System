from odoo import models, fields, _


class CustomerDetailsWizard(models.TransientModel):
    _name = "details"
    _description = "Bank Customer details"

    details_id = fields.Many2one("bank.customer", string="Select Account Holders ", domain=[('status', '=', 'confirm')])

    def details_button(self):
        pass
