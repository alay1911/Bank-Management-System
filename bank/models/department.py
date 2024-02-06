from odoo import models,fields


class BankDecustomer(models.Model):
    _name = "dept.dept"
    _description = "Bank Customer"

    name = fields.Char(string='Name')
    cust_ids = fields.Many2many("bank.customer","de_cust_relation","cust_id","de_id",string="Customer")



