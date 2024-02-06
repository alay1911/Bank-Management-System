from odoo import models


class CustomerXlsx(models.AbstractModel):
    _name = 'report.bank.mrp_report_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet('success')
        sheet.set_column("B:B", 30)
        sheet.set_column("C:C", 18)

        format1 = workbook.add_format({'font_size': 11, 'text_wrap': True})

        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})

        format3 = workbook.add_format({'font_size': 15, 'bold': True, 'bg_color': '#AAAAAA', 'border': 1})
        sheet.write(3, 1, 'Manufacturing Orders', format3)

        # format4 = workbook.add_format({'num_format': 'dd/mm/yy'})

        format5 = workbook.add_format({'font_size': 10, 'bold': True, 'border': 1})
        format7 = workbook.add_format({'font_size': 10, 'bold': True, 'border': 1})
        sheet.write(9, 1, 'Responsible:', format5)
        sheet.write('B12:D12', 'Finished Product:', format5)
        sheet.write(11, 2, 'Quantity to Produce:', format5)
        sheet.merge_range('B17:E17', 'Product:', format7)
        sheet.write(16, 5, 'Quantity:', format7)

        format6 = workbook.add_format({'font_size': 15})
        sheet.write(14, 1, 'Consumed Products:', format6)

        # sheet.write(8, 1, 'Customers Name', format6)

        # date_from = datetime.strptime(str(self.date_from), '%Y-%m-d').strftime(str(user_date_format))

        # active_id = self.env.context.get('active_id')
        # records = self.env['mrp.production'].with_context({'active_id':self.id})
        # records = self.env['mrp.production'].search([('active', '=', True)]).ids
        # # records = self.env['mrp.production'].browse(active_id)
        # print("(\n\n\n*****************",self._context)
        # print("\n\n\n\n\n@@@@@@@@@@@@@@@",records)
        print("\n\n\n\n\n@@@@@@@@@@@@@@@", data)
        print("\n\n\n\n\n@@@@@@@@@@@@@@@", lines)
        # print("(\n\n\n*****************",active_id)
        # print("(\n\n\n*****************",self.id)
        for rec in lines:
            sheet.write(7, 1, rec.name, format6)
            sheet.write(10, 1, rec.user_id.name, format2)
            sheet.write(12, 1, rec.product_id.name, format2)
            sheet.write(12, 2, str(rec.product_qty) + 'Units', format2)
            i = 17
            for lines in rec.move_raw_ids:
                sheet.write(i, 1, lines.product_id.name, format2)
                sheet.write(i, 5, str(lines.product_uom_qty) + 'Units', format2)
                i += 1

            # sheet.write(8, 4, 'Name', format1)

        # sheet.write(8, 5, 'Age', format1)
        # sheet.write(8, 7, lines.age, format2)

        # sheet.write(8, 6, 'Gender', format1)
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
