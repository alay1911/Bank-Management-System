from odoo import models, fields, _


class InvoiceInherit(models.TransientModel):
    _name = "invoiceinherit"
    _description = "Reports"

    start = fields.Date(string='Start Date')
    end = fields.Date(string='End Date')
    category_filter = fields.Selection([('com_user', 'Commercial User'),
                                        ('partner', 'Partner')], String='Filter By')
    state = fields.Selection([('draft', 'DRAFT'),
                              ('posted', 'POSTED'),
                              ('paid', 'PAID'),
                              ('posted_paid', 'POSTED AND PAID')], string='State')

    def invoiceinherit_button(self):
        pass
