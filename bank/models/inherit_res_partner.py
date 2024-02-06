from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class contacts(models.Model):
    _inherit = 'res.partner'

    partner = fields.Selection([('com_user', 'Commercial User'),
                                     ('partner', 'Partner')],string='Partner Type')
