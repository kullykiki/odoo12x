# -*- coding: utf-8 -*-
{
    'name': "Tiny Stock",

    'summary': """
        🤗 Tiny Stock 🏬🌴""",

    'description': """
        Long description of module's purpose
    """,

    'author': "🤖 Odoo Ranger ✨",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/m_item.xml',
        'views/views.xml',
        'views/templates.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}