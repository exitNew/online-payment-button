# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Online Payment Button',
    'version': '1.0.0',
    'category': 'Hidden/Tools',
    'summary': 'Online payment button, instead of scan QR it just go stright to payment link',
    'description': """
    This is created for online payment using Xendit or any Indonesian QRIS
""",
    'author': 'github.com/exitNew',
    'maintainer': 'github.com/exitNew',
    'company': 'github.com/exitNew',
    'website': 'github.com/exitNew',
    'depends': [
      'point_of_sale',
      'pos_online_payment'
    ],
    'assets': {
        'point_of_sale.assets_prod': [
            'online_payment_button/static/src/js/online_payment_popup.js',
            'online_payment_button/static/src/xml/online_payment_popup.xml',
            'online_payment_button/static/src/scss/online_payment_popup.scss',
        ],
    },
    'license': 'LGPLv3',
}
