from odoo import models, fields, _


class CustomerReport(models.TransientModel):
    _name = "customer.reports"
    _description = "Reports"

    start = fields.Date(string='Start Date')
    end = fields.Date(string='End Date')

    def action_print(self):
        data = {
            "ids": "self.ids",
            "model": "bank.customer",
            "form": self.read(["start", "end"])[0],
        }

        records = self.env['bank.customer'].search(
            [('today_date', '>', self.start), ('today_date', '<', self.end)])
        print('\n\n\n\n\n\n\n', records)
        cus_data = []
        for i in records:
            print("\n\n----------------------", i.name_two)
            cus_data.append({'name_two': i.name_two, 'today_date': i.today_date,'gender': i.phone,'phone': i.gender,'email': i.email})
            print(cus_data)

        data.update({
            'records': cus_data,

        })
        print('\n\n\n\n\n\n\n', data)
        return self.env.ref('bank.first_half').report_action(self, data=data)
