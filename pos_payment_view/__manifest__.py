# -*- coding: utf-8 -*-
{
    "name": "POS Payment View",
    "version": "11.0",
    "website": "knacktechs.com",
    "category": "POS",
    "depends": [
        'web','point_of_sale',
    ],
    "description": "This module fixed the bugs in payment window of Point Of Sale",
    "data": [
        'views/pos_view.xml'
    ],
    "qweb": ['static/src/xml/pos.xml',
    ],
    "auto_install": False,
    "installable": True,
    'certificate': '',
}
