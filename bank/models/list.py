from odoo import models, fields


class BankLicustomer(models.Model):
    _name = "list.list"
    _description = "Bank Customer"

    name = fields.Char(string='Name Of Manager')
    user_id = fields.Many2one('res.users','User')

