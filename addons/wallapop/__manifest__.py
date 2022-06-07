# -*- coding: utf-8 -*-
{
    'name': "Wallapop",
    'summary': "",
    'description': """
        wallapop module to manage laptop sales:
    """,
    'author': "Casado",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Examen',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'vistas/estudiante.xml', 'vistas/portatil.xml', 'vistas/menu.xml'
    ],
}