# -*- coding: utf-8 -*-
{
    'name': "ระบบฝากของของพี่แสงดาว⭐",

    'summary': """
        ระบบฝากของของพี่แสงดาว⭐""",

    'description': """
        ระบบฝากของของพี่แสงดาว⭐
    """,

    'author': "🤖 Odoo Ranger ✨",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        
        'data/lgt_seq.xml',
        'data/sm_status.xml',
        'data/sm_unit.xml',

        'views/views.xml',
        'views/menu.xml',
        'views/templates.xml',
        'views/search.xml',

        'data/lgt_seq.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}