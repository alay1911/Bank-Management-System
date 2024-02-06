from odoo import models, fields


class BankNcustomer(models.Model):
    _name = "net.net"
    _description = "Bank Customer"

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string="Phone no")
    age = fields.Integer(string="Age")
    accountno = fields.Integer(string="Account Number")
    addharphoto = fields.Binary(string="Addhar card")
    date = fields.Date(string="Date")


    def email_button(self):
        template = self.env.ref('bank.mail_template_bank')
        for rec in self:
            template.send_mail(rec.id, force_send=True)
        print("***************************", rec.id)

