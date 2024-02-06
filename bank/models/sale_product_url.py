from odoo import fields, models, api, tools


class SaleProduct(models.Model):
    _inherit = 'product.template'

    url_links = fields.Text(string='Paste URL Links')

    def get_extra_images(self):
        pass
