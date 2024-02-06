from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date, datetime


class ArchiveTrial(models.AbstractModel):
    _name = 'archive.trial'
    _description = 'Archive Trial'

    name = fields.Char(string='Name')
    active = fields.Boolean(string='active', default=True)
    archive_this = fields.Boolean("Archive This")

    def archive_this(self, record):
        self.active = False
        return record.active


class BankCustomer(models.Model):
    _name = "bank.customer"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'archive.trial']
    _description = "Bank Customer"
    _rec_name = "name_two"

    name = fields.Char(string='Name')
    name_two = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string="Phone no")
    age = fields.Integer(string="Age", compute="_compute_age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], String='Gender')
    date = fields.Date(string="Date Of Birth")
    amountd = fields.Integer(string="Amount to Deposit")
    adhar = fields.Integer(string="Addhar Card Number")
    pan = fields.Integer(string="Pan Card No")
    de_id = fields.Many2one("dept.dept", string="Department")
    status = fields.Selection([
        ('draft', 'Draft'), ('confirm', 'confirm'), ('cancel', 'Cancel')], default='draft')

    priority = fields.Selection([
        ('1', 'High'), ('2', 'Low'), ('3', 'Medium'), ('4', 'Very High')], String='priority')

    ht = fields.Html(string='html testing')
    image = fields.Image(string="hello")
    seq = fields.Char(string="Sequence No")
    today_date = fields.Date(string="Date Of Account Registration", default=datetime.today())
    progress = fields.Integer(string='Progress', compute='_compute_progress')
    manager = fields.Many2one("list.list", string='Manager')

    # @api.constrains('age')
    # def new_method(self):
    #     for record in self:
    #         if record.age < 18:
    #             raise ValidationError(_('age error'))

    @api.model
    def test_cron_job(self):
        print("\n\n\n\n************\n\n\n\n", self)

    def test(self):
        print("done")

    def process(self):
        for rec in self:
            rec.status = "draft"

    def confirm_button(self):
        for rec in self:
            rec.status = "confirm"

    def list_button(self):

        print("------------------\n\n\n")
        customer = self.env['bank.customer'].search([])
        print("customers.......", customer)

        # customer_count = self.env['bank.customer'].search_count([])
        # print("customers.......", customer_count)

        # Browse
        # browse = self.env['dept.dept'].browse(1)
        # print("browsed data......",browse)
        # print("browsed data......",browse.name)

        # Create
        # vals = {'name_two':'jinaal'}
        # self.env['bank.customer'].create(vals)

        # Write
        # browse_data = self.env['bank.customer'].browse(19)
        # if browse_data.exists():
        #     vals = {'email':'j@gmail.com','phone':'1111111111'}
        #     browse_data.write(vals)

        # Copy
        # data_copy = self.env['bank.customer'].browse(13)
        # data_copy.copy()

        # Unlink
        # data_copy = self.env['bank.customer'].browse(26)
        # data_copy.unlink()

        # name_get and name_search
        # name_get = self.env['bank.customer'].search([('id','=',10)])
        # print("\n\n\n name get record.......",name_get.name_two)
        # print("\n\n\n age get recod......",name_get.age)

        # Filtered
        # filtered_customers = self.env['bank.customer'].search([]).filtered(lambda s:s.gender == 'female')
        # print("\n\n\nfiltered ORM Result.......",filtered_customers)

        # Mapped
        # mapped_customers = self.env['bank.customer'].search([]).mapped('age')
        # print("\n\n\n mapped ORM record.........",mapped_customers)

        # Sorted
        # sorted_customers = self.env['bank.customer'].search([]).sorted(key='age').mapped('age')
        # print("\n\n\nSorted ORM record........",sorted_customers)

        # Sudo
        # customer_sudo = self.env['bank.customer'].sudo().search([('gender','=','female')])
        # print("\n\n Sudo record of ORM......",customer_sudo)

    def cancel(self):
        for rec in self:
            rec.status = "cancel"

    def whatsapp_button(self):
        if not self.phone:
            raise ValidationError(_("Missing number"))
        message = 'Hi {} your gender is {}'.format(self.name_two, self.gender)
        whatsapp_api_url = 'https://api.whatsapp.com/send/?phone=%s&text&type=phone_number&app_absent=0&text=%s' % (
            self.phone, message)
        return {'type': 'ir.actions.act_url', 'target': 'new', 'url': whatsapp_api_url}

    def smart_button(self):
        return {

            'type': 'ir.actions.act_window',
            'res_model': 'board.board',
            'view_mode': 'form',
            'target': 'current'
        }

    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date:
                rec.age = today.year - rec.date.year
            else:
                rec.age = 0

    def done(self):
        message = "Customer Registered Successfully"
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': message,
                'type': 'success',
                'sticky': False,
            }
        }

    def Archive_button(self):
        self.archive_this(self)

    @api.model
    def default_get(self, fields):
        res = super(BankCustomer, self).default_get(fields)
        res['amountd'] = 3500
        return res

    @api.model
    def create(self, vals):
        vals['seq'] = self.env['ir.sequence'].next_by_code('bank.customer')
        return super(BankCustomer, self).create(vals)

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s-%s' % (rec.name_two, rec.seq)))
        return result

    @api.depends('status')
    def _compute_progress(self):
        for rec in self:
            if rec.status == 'draft':
                progress = 50
            elif rec.status == 'confirm':
                progress = 100
            else:
                progress = 0
            rec.progress = progress

    @api.constrains('today_date')
    def check_today_date(self):
        for rec in self:
            if rec.today_date and rec.today_date > fields.Date.today():
                raise ValidationError(_('Entered Date of Account Registration is not Acceptable..!!!'))

    #
    # def context_button(self):
    # return {
    #
    #     'type': 'ir.actions.act_window',
    #     'res_model': 'feedback.feedback',
    #     'view_mode': 'form',
    #     'target': 'current',
    #     'context': {
    #         'default_email': self.email,
    #         'default_phone': self.phone,
    #         'default_name': self.name_two,
    #     }
    # }

    def deposit_button(self):
        return {

            'type': 'ir.actions.act_window',
            'res_model': 'bank.deposit',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_net_balance': self.amountd,
            }
        }
