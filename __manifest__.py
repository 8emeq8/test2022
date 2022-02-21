# -*- coding: utf-8 -*-
# Powered by Kanak Infosystems LLP.
# © 2020 Kanak Infosystems LLP. (<https://www.kanakinfosystems.com>).

{
    'name': 'Journal Entries Maker Approver kanak',
    'version': '15.0.1.0',
    'description': """
    """,
    'summary': 'This module allow to manage journal entries in invoicing.',
    'category': 'Accounting/Accounting',
    'license': 'OPL-1',
    'author': 'Kanak Infosystems LLP.',
    'website': 'https://www.kanakinfosystems.com',
    'depends': ['base', 'account'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/account_move.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'sequence': 1,
    'installable': True,
    'application': True,
    'currency': 'EUR',
    'live_test_url': 'https://youtu.be/RLaX_FRK0hs',
}
