# -*- coding: utf-8 -*-
{
    "name": "Contact Experience",
    "description": """
      Contact Experience
      """,
    "version": "13.0.0",
    "website": "",
    "author": "krondon25",
    "license": "AGPL-3",
    "depends": [
        "contacts",'report_xlsx'
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/skill_data.xml",
        "views/res_partner.xml",
        "views/experience_view.xml",
        "report/partner_report.xml",
        
    ],
    'installable': True,
    'auto_install': True
}
