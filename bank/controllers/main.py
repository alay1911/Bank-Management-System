from odoo import http
from odoo.http import request
import json


class Bank(http.Controller):

    @http.route('/bank/customer/', website=True, auth='public')
    def bank_customer_new(self):
        # return "Controller test successfully done"
        customers = request.env['sale.order'].sudo().search([])
        return request.render("bank.controller_template", {
            'customers': customers
        })

    @http.route('/bank/menu/', website=True, auth='public')
    def bank_menu(self):
        return http.request.render('bank.create_customer', {})

    @http.route('/bank/thanks/', website=True, auth='public')
    def bank_thanks(self, **kw):
        print("\n\n\n\n****************\n\n\n\n", kw)
        request.env['bank.customer'].sudo().create(kw)
        return request.render("bank.customer_thanks", {})

    @http.route('/product', type='http', auth="public", website=True)
    def get_product(self, **kw):
        prod = request.env['product.product'].search([])
        return json.dumps(prod.read(['name']))

    @http.route('/product/<int:id>', type='http', auth="public")
    def ProductId(self, id):
        # ids = [('id', '=', int(ids))]
        pid = request.env['product.product'].browse(id).read()
        return json.dumps(pid, default=str)
