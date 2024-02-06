from odoo import models


class CustomerXlsx(models.AbstractModel):
    _name = 'report.bank.report_customer_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet('success')
        sheet.set_column("B:B", 30)

        format1 = workbook.add_format({'font_size': 11, 'text_wrap': True})

        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})

        format3 = workbook.add_format({'font_size': 15, 'bold': True,'bg_color': '#AAAAAA'})
        sheet.write(3, 1, 'Customer Excel Report', format3)

        format4 = workbook.add_format({'num_format': 'dd/mm/yy'})

        format5 = workbook.add_format({'font_size': 15})
        sheet.write(6, 1, 'Bank customers', format5)

        format6 = workbook.add_format({'font_size': 10})
        sheet.write(8, 1, 'Customers Name', format6)

        # date_from = datetime.strptime(str(self.date_from), '%Y-%m-d').strftime(str(user_date_format))

        sheet.write(8, 4, 'Name', format1)
        sheet.write(10, 1, lines.name_two, format2)

        sheet.write(8, 5, 'Age', format1)
        # sheet.write(8, 7, lines.age, format2)

        sheet.write(8, 6, 'Gender', format1)
        # sheet.write(10, 7, lines.gender, format2)

        # sheet.write(12, 6, 'Number:', format1)
        # sheet.write(12, 7, lines.phone, format2)
        #
        # sheet.write(14, 6, 'Email:', format1)
        # sheet.write(14, 7, lines.email, format2)
        #
        # # sheet.set_column(16,6,'Date:',format4)
        # # sheet.set_column(16,7,20,lines.date,format4)
        # sheet.write(16, 6, 'Date:', format1)
        # sheet.write(16, 7, lines.date, format4)
        #
        # sheet.write(18, 6, 'S Num:', format1)
        # sheet.write(18, 7, lines.seq, format2)

        # sheet.insert_image(‘A1‘,icon.png’)
        # sheet.set_column(0, 2, 20,lines.date,format4)

        # sheet.conditional_format('B3:K12', {'type': 'date',
        #                                     'criteria': '>=',
        #                                     'value': 100,
        #                                     'format': format4})
