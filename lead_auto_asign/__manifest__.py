# -*- coding: utf-8 -*-
{
    'name': "Lead Auto Asign",

    'summary': """
        Asignacion automatica de leads de acuerdo a un registro comparativo""",

    'description': """
        Modulo que asigna la distribucion de los lead por region y estados.
    """,

    'author': "Xmarts",
    'website': "https://xmarts.com",

    'category': 'Sales',
    'version': '1.1',

    'depends': ['base','website_form', 'website_partner', 'crm', 'website_crm' ],

    'data': [
        'security/ir.model.access.csv',
        'views/crm_estado_data.xml',
        'views/webview.xml',
        'views/views.xml',
    ],
}