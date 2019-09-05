# -*- coding: utf-8 -*-
{
    'name': "Stop Sale on Website",
    'summary': """Sale only available products on Website""",
    'version': '1.0.0',
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    'license': 'LGPL-3',
    'category': 'eCommerce',
    "support": "apps@it-projects.info",
    'website': 'https://yelizariev.github.io',
    'images': ['images/available.png'],
    'price': 9.00,
    'currency': 'EUR',
    'depends': [
        'website_sale',
        'stock',
        'delivery',
    ],
    'data': [
        'views/website_sale_available_views.xml',
    ],
    'installable': True,
}
