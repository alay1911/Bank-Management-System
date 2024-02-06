from odoo import models, fields, _, api


class NewField(models.Model):
    _inherit = 'sale.order.line'

    new_field = fields.Text('Note')
