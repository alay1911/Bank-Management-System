from odoo import models, fields, api


class Services(models.Model):
    _name = "bank.service"
    _description = "Bank services"

    name = fields.Many2one("bank.deposit", string="Select Account Holders ")
    amount = fields.Float(string="Amount To withdraw")
    net_balance = fields.Float(string="Total Balance in your account", compute='_compute_sum')
    sum = fields.Integer(string="Updated Balance")

    @api.onchange('amount', 'net_balance')
    def _onchange_quantity(self):
        self.sum = self.net_balance - self.amount
        return

    def _compute_sum(self):
        self.net_balance = self.sum
        return

    # @api.onchange('name')
    # def Onchange_record(self):
    #     self.net_balance=self.name
    # vals = {
    #     'sum': self.net_balance
    # }
    # self.env['bank.deposit'].write(vals)
    # print("***********", self.sum)

    # @api.model
    # def create(self, vals):
    #     res = super(Services, self).create(vals)
    #     report = self.env['bank.deposit'].search([('name', '=', res.name.name)]).write({'sum': res.net_balance})
    #     print(res,self,"*****************************")
    #     print(report,'============================report')
    #     return res

    # res.partnrer

    @api.onchange('name')
    def onchange_name(self):
        self.net_balance = self.name.net_balance
