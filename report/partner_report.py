# -*- coding: utf-8 -*-
from odoo import models


class AccountReport(models.AbstractModel):
    _name = 'report.contact_experience.partner_report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, obj):
        sheet = workbook.add_worksheet('Contactos')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, 'Nombre Contactos:', bold)
        sheet.write(0, 1, 'Nro habilidades', bold)
        row = 1
        
        for record in obj:
            if record.number_skills > 3:
                sheet.write(row, 0, record.name)
                sheet.write(row, 1, record.number_skills)
                row += 1
                
