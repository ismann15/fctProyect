# -*- coding: utf-8 -*-
{
    'name': "fctproyect",

    'summary': """Manage pupils during the FCT""",

    'description': """
        Module for management of fct pupils 
    """,

    'author': "Ismael",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/parthner.xml'
        'views/user.xml',
        'views/fctproyect.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}