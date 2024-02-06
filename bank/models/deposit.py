from odoo import models, fields, api


class Services(models.Model):
    _name = "bank.deposit"
    _description = "Bank services"

    name = fields.Many2one("bank.customer", string="Select Account Holders ", domain=[('status', '=', 'confirm')])
    amount = fields.Integer(string="Amount To Deposit")
    net_balance = fields.Integer(string="Total Balance in your account", compute="_compute_sum")
    sum = fields.Integer(string="Updated Balance")

    @api.onchange('amount', 'net_balance')
    def _onchange_quantity(self):
        self.sum = self.net_balance + self.amount
        return

    def _compute_sum(self):
        self.net_balance = self.sum
        return

    @api.onchange('name')
    def onchange_name(self):
        self.net_balance = self.name.amountd
