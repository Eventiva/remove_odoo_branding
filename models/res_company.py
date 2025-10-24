# -*- coding: utf-8 -*-

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    email_footer = fields.Html(
        string='Email Footer',
        translate=True,
        help="Custom footer text that will appear in all transactional emails "
             "(helpdesk, CRM, sales, event tracks, etc.). This appears after the "
             "company contact details. Supports HTML formatting."
    )

