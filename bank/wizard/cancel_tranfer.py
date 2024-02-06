import io
from odoo import models, fields, _
import csv
import base64


class CancelTransfer(models.TransientModel):
    _name = "cancel.transfer"
    _description = "Bank Customer cancel"

    transfer_id = fields.Many2one("bank.customer", string="Account Holders", domain=[('status', '=', 'draft')])
    file = fields.Binary(string='Upload your Sheet')
    reason = fields.Text(string='Reason')

    def wizard_import(self):
        content_base64 = base64.b64decode(self.file)
        str = io.StringIO(content_base64.decode('utf-8').strip())
        csv_reader = csv.reader(str, delimiter=',')
        str = list(csv_reader)
        str.pop(0)
        print("&*******************", str)
        for record in str:
            name = record[0]
            vals = {
                'name': name,
            }
            self.env['res.users'].create(vals)

    def Delete_account(self):
        for i in self:
            i.transfer_id.unlink()
