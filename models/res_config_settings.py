# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    email_footer = fields.Html(
        string='Email Footer',
        related='company_id.email_footer',
        readonly=False,
        help="Custom footer text that will appear in all transactional emails. "
             "This footer will be displayed after the company contact details in "
             "emails sent from helpdesk, CRM, sales, event tracks, and other modules."
    )


