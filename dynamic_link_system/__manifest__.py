# -*- coding: utf-8 -*-
{
    'name': 'dynamic_link_system',
    'version': '15.0.0.1',
    'category': '',
    'summary': 'Dynamic link System',
    'depends': ['base', 'website','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/link_categ.xml',
        'views/external_link_system.xml',
        'views/res_partner.xml',
        'views/membership.xml',
        'views/location_categs.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
