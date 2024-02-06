from odoo import models, fields, _
from odoo.http import request


class SwitchUser(models.TransientModel):
    _name = "switch"
    _description = "Switch User"

    user = fields.Char(string='Enter Email-id')
    password = fields.Char(string='Enter Password')

    def switch_user(self):
        data = "demo_new_ban"
        if request.session.authenticate(data, self.user, self.password):
            print("\n\n")
        else:
            print("\n\n")

        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
