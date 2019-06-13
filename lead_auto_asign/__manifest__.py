# -*- coding: utf-8 -*-
{
    'name': "lead_auto_asign",

    'summary': """
        
        Asignacion automatica de leads de acuerdo a un registro comparativo.""",

    'description': """
        Modulo que asigna la distribucion de los lead por region y estados.
    """,

    'author': "XMARTS",
    'email': 'desarrollo@xmarts.com',
    'website': "https://xmarts.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website_form', 'website_partner', 'crm', 'website_crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/crm_estado_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
   
}