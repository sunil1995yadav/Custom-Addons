# -*- coding: utf-8 -*-
{
    'name': 'POS Payment Ref',
    'version': '10.0.1.0.0',
    'summary': """Allow users to add narration of payment ref from the POS """,
    'category': 'Point Of Sale',
    'license': 'LGPL-3',
    'author': "Knacktechs Solutions",
    'website': "http://knacktechs.com/",
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_payment_ref.xml',
        'views/account_journal_view.xml',
        'views/pos_order_view.xml',
    ],
    'images': [
    ],
    'installable': True,
    'application': True,
    'qweb': ['static/src/xml/pos_payment_ref.xml'],
}
