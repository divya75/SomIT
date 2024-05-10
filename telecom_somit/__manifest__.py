# -*- coding: utf-8 -*-
{
    'name': 'Telecom Service Consumption Management',
    'version': '16.0.1.0.0',
    'category': 'Telecom',
    'summary': 'Manage telecom service consumptions',
    'author': 'Divya Vyas',
    'website': 'https://www.somit.coop',
    'depends': ['base', 'product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'data/demo_data.xml',
        'views/consumption_view.xml',
        'views/product_category_view.xml',
    ],
    'installable': True,
    'application': True,
}
