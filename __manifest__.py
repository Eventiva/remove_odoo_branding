# -*- coding: utf-8 -*-
{
    'name': 'Remove Odoo Branding',
    'version': '1.0',
    'category': 'Technical',
    'summary': 'Remove "Powered by Odoo" branding from emails',
    'author': 'Eventiva',
    'website': 'www.eventiva.com',
    'description': """
Remove Odoo Branding
====================
This module removes "Powered by Odoo" footer text from email templates.
    """,
    'depends': [
        'mail',
    ],
    'data': [
        'data/mail_template_layouts.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'Other proprietary',
}

