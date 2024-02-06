from odoo import models, fields, _, api


class SaleOrder(models.Model):
    _inherit = 'purchase.order'

    notes_name_new = fields.Text('Note')
    date = fields.Date(string="New Date")

    # @api.model
    def write(self,vals):
        res = super(SaleOrder,self).write(vals)
        message = "date is updated to "+str(self.date)
        self.message_post(body =message)
        return res








        # self.env['purchase.order'].create(message)

    # def button_validate(self):
    #     res = super(SaleOrder, self)
    #     sale_order = self.env['purchase.order']
    #     responsible_person = sale_order.date.name
    #     self.date = self.env['purchase.order']
    #     display_msg = """ Dear """
    #     responsible_person.message_post(body=display_msg)
    #     return res


    # def _log_merge_operation(self, date):
    #     super(SaleOrder, self)
    #     date.message_post(body='%s %s' % (_("success trial")))








