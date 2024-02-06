from odoo import models, fields


class BankFcustomer(models.Model):
    _name = "feedback.feedback"
    _description = "Bank Customer"

    name = fields.Many2one("bank.customer", string="Select Account Holders ", domain=[('status', '=', 'confirm')])
    email = fields.Char(string='Email')
    phone = fields.Char(string="Phone no")
    feedback = fields.Text(string='Feedback')
    rating = fields.Selection([('good', 'Good'), ('better', 'Better'), ('best', 'Best')], String='Rating')


